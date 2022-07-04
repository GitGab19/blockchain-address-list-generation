# Bitcoin Cash
This folder contains the scripts needed to generate and check the presence of the generated address (starting from the private/public key sets) in the list of addresses extracted from the Bitcoin Cash blockchain.
<br>
- In order to generate the *compressed* addresses, run the *CompBcashGen.py* script
- In order to generate the *uncompressed* addresses, run the *UncBcashGen.py* script
<br><br>

**BEWARE**<br>
Before running them, you need to have:
- A .txt file containing the private+public keys (let's have a look at our's *secp256k1_keys.txt* example file.
- A database implementing *mysql* fulfilled with the list of addresses extracted from the blockchain (let's have a look at our *address_extraction_from_blockchain* folder).
