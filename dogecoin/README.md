# Dogecoin <img align="center" src="https://cryptologos.cc/logos/dogecoin-doge-logo.png?v=022" width="40" height="40">
This folder contains the scripts needed to generate and check the presence of the generated address (starting from the private/public key sets) in the list of addresses exctracted from the Dogecoin blockchain.
<br>
- In order to generate the *compressed* addresses, run the *CompDogeGen.py* script
- In order to generate the *uncompressed* addresses, run the *UncDogeGen.py* script
<br><br>

**BEWARE**<br>
Before running them, you need to have:
- A .txt file containing the private+public keys (let's have a look at our's *secp256k1_keys.txt* example file.
- A database implementing *mysql* fulfilled with the list of addresses extracted from the blockchain (let's have a look at our *address_extraction_from_blockchain* folder).
