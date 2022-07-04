import datetime
import bitcoin
import mysql.connector
import sys
sys.path.append('../')
sys.path.append('/Users/antonio/AppData/Local/Programs/Python/Python39/Lib/site-packages')
# sys.path.append('/Users/antonio/AppData/Local/Programs/Python/Python39/Lib/site-packages')
import AddressGeneration


t0 = datetime.datetime.now()

with open("Luck.txt", "a") as f:
    print(t0, file=f)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zcash"
)

# Parameters

u = 0
env = 0

file_name = '../cosetSecp256k1Keys.txt'

fh = open(file_name, 'rt')
line0 = fh.readline()
line = fh.readline()


while line:
    chunks = line.split('\t')
    public_key = AddressGeneration.CompressedPublicKeyComputation(chunks[2], chunks[3])
    public_key = public_key.split('\n')
    private_key = chunks[1]

    pub = AddressGeneration.ZCashAddressComputation(public_key[0])

    mycursor = mydb.cursor()
    sql = "SELECT * FROM address_zcash WHERE address='" + pub + "';"

    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if myresult:
        cuerpo = 'Private key= {pkwif}  \r\n Address = {address} \r\n -----------------------'
        Message = cuerpo.format(pkwif=private_key, address=pub)
        with open("Luck.txt", "a") as f:
            print(Message, file=f)
    u = u + 1
    line = fh.readline()
fh.close()
print(u)
with open("Luck.txt", "a") as f:
    print((datetime.datetime.now() - t0).seconds, file=f)