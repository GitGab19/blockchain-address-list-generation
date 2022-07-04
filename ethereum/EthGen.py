# This script computes the Ethereum addresses for our starting set and checks if they ever appeared on
# the blockchain. The whole list of existing addresses must be loaded in advance on a SQL database

import AddressGeneration
import datetime
import mysql.connector

t0 = datetime.datetime.now()

# Luck.txt is the file where the private keys corresponding to existing addresses get saved
with open("Luck.txt", "a") as f:
    print(t0, file=f)

# Link with the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ethereum"  # database name
)

# Parameters
u = 0
env = 0

# Name of the file with the 144M keys of our subsets
file_name = 'cosetSecp256k1Keys.txt'

fh = open(file_name, 'rt')
line0 = fh.readline()
line = fh.readline()


while line:
    chunks = line.split('\t')
    public_key = AddressGeneration.UncompressedPublicKeyComputation(chunks[2], chunks[3])
    public_key = public_key.split('\n')
    private_key = chunks[1]

    pub = AddressGeneration.EthereumAddressComputation(public_key[0])

    mycursor = mydb.cursor()
    # search in the database: SELECT * FROM tableName WHERE attributeName =
    sql = "SELECT * FROM addresseth WHERE address='" + pub + "';"

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
