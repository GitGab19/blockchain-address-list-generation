import datetime
import bitcoin
import mysql.connector
import AddressGeneration


t0 = datetime.datetime.now()

with open("Luck.txt", "a") as f:
    print(t0, file=f)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bcash"
)

# Parameters

u = 0
env = 0

file_name = '../secp256k1_keys.txt'

fh = open(file_name, 'rt')
line0 = fh.readline()
line = fh.readline()


while line:
    chunks = line.split('\t')
    public_key = AddressGeneration.CompressedPublicKeyComputation(chunks[2], chunks[3])
    public_key = public_key.split('\n')
    private_key = chunks[1]

    pub = AddressGeneration.BCashAddressComputation(public_key[0])

    mycursor = mydb.cursor()
    sql = "SELECT * FROM address_bch WHERE address='" + pub + "';"

    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if myresult:
        body = 'Private key= {pkwif}  \r\n Address = {address} \r\n -----------------------'
        Message = body.format(pkwif=private_key, address=pub)
        with open("Luck.txt", "a") as f:
            print(Message, file=f)
    u = u + 1
    line = fh.readline()
fh.close()
print(u)
with open("Luck.txt", "a") as f:
    print((datetime.datetime.now() - t0).seconds, file=f)