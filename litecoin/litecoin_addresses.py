import http.client
import requests
import time

conn = http.client.HTTPSConnection("api-eu1.tatum.io")

def main():
    start_block = 0
    initial_block = start_block
    end_block = 4236364
    counter = 0
    apiKey = "INSERT YOUR TATUM API KEY HERE"
    headers = { 'x-api-key': str(apiKey) }

    while start_block < end_block:
        counter +=1
        time.sleep(0.1)
        endpoint = "https://api-eu1.tatum.io/v3/litecoin/block/"+str(start_block)
        response = requests.get(endpoint, headers=headers)
        data = response.json()
        block = data
        percentage = start_block/(end_block-initial_block+start_block)*100
        transactions_list = block['txs']
        print(str(block['height']) + ' ---> ' + str(round(percentage,2)) + '%')
        with open('./litecoin_last_block.txt', 'w') as f:
            f.write(str(block['height']))
        with open('./litecoin_addresses_list.txt', 'a') as f:
            for transaction in transactions_list:
                outputs = transaction['outputs']
                for output in outputs:
                    addresses = []
                    if "address" in output:
                        if (output['address'] is None):
                            continue
                        addresses = output['address']
                        if (addresses != []):
                            f.write(str(addresses))
                            f.write('\n')

        # Keep on iterating
        start_block += 1 

if __name__ == "__main__":
    main()