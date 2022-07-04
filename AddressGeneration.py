# This script generate addresses for all the blockchain we have chosen to examine
# (Bitcoin, Ethereum, Litecoin, Dogecoin, Bitcoin Cash, Dash, Zcash)

from ecdsa import SigningKey, SECP256k1
import sha3
from binascii import unhexlify
import hashlib
from base58 import b58encode
import bech32
from cashaddress import convert


# Computation of the private keys in the subgroup (see the paper for more details)
def PrivateKeyComputation(p1: int, p2: int, p3: int, base: int, n: int):
    order = (2 ** 6) * 3 * 149 * 631 * p1 * p2 * p3
    prod = p1 * p2 * p3
    g = pow(base, prod, order + 1)
    privateSet = [None] * n

    for i in range(n):
        if i == 0:
            privateSet[0] = hex(g)
        else:
            k = (g * int(privateSet[i - 1], 16)) % (order + 1)
            privateSet[i] = hex(k)

    return privateSet


# Computation of the private keys in the seven cosets (see the paper for more details)
def CosetPrivateKeyComputation(p1: int, p2: int, p3: int, base: int, n: int):
    prod = p1 * p2 * p3
    h = (2 ** 6) * 3 * 149 * 631
    order = h * prod
    g = pow(base, prod, order + 1)
    privateSet = [None] * n * 8

    for i in range(n):
        if i == 0:
            privateSet[0] = hex(g)
        else:
            k = (g * int(privateSet[i - 1], 16)) % (order + 1)
            privateSet[i] = hex(k)

    pows = [h, h*p1, h*p2, h*p3, h*p1*p2, h*p1*p3, h*p2*p3]

    for j in range(len(pows)):
        g = pow(base, pows[j], order + 1)
        for i in range(n):
            value = (g * int(privateSet[i], 16)) % (order + 1)
            privateSet[(j+1)*h+i] = hex(value)

    return privateSet


# Copy the private keys + corresponding public keys of the subgroup in a .txt file
# The file will have around 18M rows
def KeysFile(n: int, privateSet):
    f = open("secp256k1_keys.txt", "r+")
    f.seek(0)
    f.write('\t\tPrivateKey  \t\t\t\t\t\t\t\t\t\t  PublicKey-x \t\t\t\t\t\t\t\t\t\t   PublicKey-y  \n')

    for i in range(n):
        k = int(privateSet[i], 16).to_bytes(32, "big")
        k = SigningKey.from_string(k, curve=SECP256k1)
        K = k.get_verifying_key().to_string()

        f.write(str(i) + ')\t' + privateSet[i] + '\t' + K.hex()[0:64] + '\t' + K.hex()[64:128] + '\n')
    f.truncate()
    f.close()


# Copy all the private keys + corresponding public keys (subgroup + seven cosets) in a .txt file
# The file will be around 144M rows
def CosetKeysFile(n: int, privateSet):
    f = open("secp256k1_keys.txt", "r+")
    f.seek(0)
    f.write('\t\tPrivateKey  \t\t\t\t\t\t\t\t\t\t  PublicKey-x \t\t\t\t\t\t\t\t\t\t   PublicKey-y  \n')

    for i in range(8*n):
        k = int(privateSet[i], 16).to_bytes(32, "big")
        k = SigningKey.from_string(k, curve=SECP256k1)
        K = k.get_verifying_key().to_string()

        f.write(str(i) + ')\t' + privateSet[i] + '\t' + K.hex()[0:64] + '\t' + K.hex()[64:128] + '\n')

    f.truncate()
    f.close()


# Public key encoding (uncompressed)
def UncompressedPublicKeyComputation(x, y):
    publicKey = '04' + str(x) + str(y)
    return publicKey


# Public key encoding (compressed)
def CompressedPublicKeyComputation(x, y):
    if int(y, 16) % 2 == 0:
        publicKey = '02' + str(x)
    else:
        publicKey = '03' + str(x)

    return publicKey


# Address checksum computation
def checksum_computation(string: str) -> hex:
    cs = hashlib.sha256(hashlib.sha256(unhexlify(string)).digest()).hexdigest()
    checksum = cs[:8]
    return checksum


# Computation of a Bitcoin address (P2PKH)
def BitcoinClassicAddressComputation(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    hash2_temp = ripemd160.hexdigest()

    hash3_temp = '00' + hash2_temp

    checksum = checksum_computation(hash3_temp)

    hash_final = hash3_temp + str(checksum)
    hash_final_bytes = unhexlify(hash_final)
    address = b58encode(hash_final_bytes).decode("utf-8")
    return address


# Computation of a Bitcoin address (segwit)
def BitcoinSegwitAddress(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    witness_program = ripemd160.hexdigest()
    witness_program_bytes = unhexlify(witness_program)
    address = bech32.encode('bc', 0, witness_program_bytes)

    return address


# Computation of a Ethereum address + checksum
def EthereumAddressComputation(publicKey):
    keccak = sha3.keccak_256()
    keccak.update(unhexlify(publicKey[2:130]))
    hash = keccak.hexdigest()
    address = '0x' + hash[24:]

    checksum = ""
    address = address.replace('0x', '')

    keccak2 = sha3.keccak_256()
    keccak2.update(address.encode())
    mask = keccak2.hexdigest()[:40]

    for j, digit in enumerate(address):
        if digit in '0123456789':
              checksum += digit
        elif digit in 'abcdef':
            if int(mask[j], 16) > 7:
                checksum += digit.upper()
            else:
                checksum += digit
    address = '0x' + checksum

    return address


# Computation of a Dogecoin address
def DogecoinAddressComputation(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    hash2_temp = ripemd160.hexdigest()

    hash3_temp = '1E' + hash2_temp

    checksum = checksum_computation(hash3_temp)

    hash_final = hash3_temp + str(checksum)
    hash_final_bytes = unhexlify(hash_final)
    address = b58encode(hash_final_bytes).decode("utf-8")
    return address


# Computation of a Litecoin address (P2PKH)
def LitecoinAddressComputation(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    hash2_temp = ripemd160.hexdigest()

    hash3_temp = '30' + hash2_temp

    checksum = checksum_computation(hash3_temp)

    hash_final = hash3_temp + str(checksum)
    hash_final_bytes = unhexlify(hash_final)
    address = b58encode(hash_final_bytes).decode("utf-8")
    return address


# Computation of a Litecoin address (segwit)
def LitecoinSegwitAddress(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    witness_program = ripemd160.hexdigest()
    witness_program_bytes = unhexlify(witness_program)
    address = bech32.encode('ltc', 0, witness_program_bytes)

    return address


# Computation of a Bitcoin Cash address (CashAddress encoding)
def BCashAddressComputation(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    hash2_temp = ripemd160.hexdigest()

    hash3_temp = '00' + hash2_temp

    checksum = checksum_computation(hash3_temp)

    hash_final = hash3_temp + str(checksum)
    hash_final_bytes = unhexlify(hash_final)
    address = b58encode(hash_final_bytes).decode("utf-8")
    address = convert.to_cash_address(address)[12:]
    return address


# Computation of a Dash address
def DashAddressComputation(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    hash2_temp = ripemd160.hexdigest()

    hash3_temp = '4c' + hash2_temp

    checksum = checksum_computation(hash3_temp)

    hash_final = hash3_temp + str(checksum)
    hash_final_bytes = unhexlify(hash_final)
    address = b58encode(hash_final_bytes).decode("utf-8")
    return address


# Computation of a Zcash address
def ZCashAddressComputation(publicKey):
    public_key_bytes = unhexlify(publicKey)

    sha256 = hashlib.sha256()
    sha256.update(public_key_bytes)
    hash_temp = sha256.digest()

    ripemd160 = hashlib.new('Ripemd160')
    ripemd160.update(hash_temp)
    hash2_temp = ripemd160.hexdigest()

    hash3_temp = '1cb8' + hash2_temp

    checksum = checksum_computation(hash3_temp)

    hash_final = hash3_temp + str(checksum)
    hash_final_bytes = unhexlify(hash_final)
    address = b58encode(hash_final_bytes).decode("utf-8")
    return address







