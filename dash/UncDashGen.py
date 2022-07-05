# This script computes the Dash uncompressed addresses  for our starting set and checks if they ever appeared on
# the blockchain. The whole list of existing addresses must be loaded in advance on a SQL database

import datetime
import bitcoin
import mysql.connector
import sys
sys.path.append('../')
import AddressGeneration


t0 = datetime.datetime.now()

with open("Luck.txt", "a") as f:
    print(t0, file=f)

# Link with the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dash" # database name
)

# Parameters

u = 0
env = 0

# Name of the file with the 144M keys of our subsets
file_name = 'secp256k1Keys.txt'

fh = open(file_name, 'rt')
line0 = fh.readline()
line = fh.readline()

#SELECT * FROM address_eth WHERE address='0xB410674D5BB2C7a3c28eeb8a4013D1533A42BC10';

while line:
    chunks = line.split('\t')
    public_key = AddressGeneration.UncompressedPublicKeyComputation(chunks[2], chunks[3])
    public_key = public_key.split('\n')
    private_key = chunks[1]

    pub = AddressGeneration.DashAddressComputation(public_key[0])
    mycursor = mydb.cursor()
    # search in the database: SELECT * FROM tableName WHERE attributeName =
    sql = "SELECT * FROM address_dash WHERE address='" + pub + "';"

    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if myresult:
        cuerpo = 'Private key= {pkwif}  \r\n Address = {address} \r\n -----------------------'
        Message = cuerpo.format(pkwif=private_key, address=pub)
        with open("Luck.txt", "a") as f:
            print(Message, file=f)
    line = fh.readline()

fh.close()
print(u)
with open("Luck.txt", "a") as f:
    print((datetime.datetime.now() - t0).seconds, file=f)
