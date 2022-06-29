import http.client
import requests
import time

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

def main():
    start_block = 0
    initial_block = start_block
    end_block = 741389
    counter = 0
    apiKey = "INSERT YOUR TATUM API KEY HERE"
    headers = { 'x-api-key': str(apiKey) }

    while start_block < end_block:
        counter +=1
        time.sleep(0.1)
        endpoint = "https://api-eu1.tatum.io/v3/bcash/block/"+str(start_block)
        response = requests.get(endpoint, headers=headers)
        data = response.json()
        block = data
        percentage = start_block/(end_block-initial_block+start_block)*100
        transactions_list = block['tx']
        print(str(block['height']) + ' ---> ' + str(round(percentage,2)) + '%')
        with open('./bch_last_block_.txt', 'w') as f:
            f.write(str(block['height']))
        with open('./bch_addresses_list.txt', 'a') as f:
            for transaction in transactions_list:
                v_outs = transaction['vout']
                for v_out in v_outs:
                    addresses = []
                    type_check = v_out['scriptPubKey']['type']
                    if (type_check == 'nulldata') or (type_check == 'nonstandard'):
                        #print("INVALID transaction!")
                        continue
                    if "addresses" in v_out['scriptPubKey']:
                        addresses = v_out['scriptPubKey']['addresses']
                    if (addresses != []):
                        for address in addresses:
                            f.write(str(address))
                            f.write('\n')

        # Keep on iterating
        start_block += 1 

if __name__ == "__main__":
    main()