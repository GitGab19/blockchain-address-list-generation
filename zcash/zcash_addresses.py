import subprocess
from sys import stdout
import json

for x in range(0,1677816):
    with open('./zcash_counter.txt', 'w') as fp:
        fp.write(str(x)+'\n')
    percentage = (x/(1677816))*100
    print("block number "+str(x)+" --> "+str(percentage)+"%")
    with open('./zcash_addresses.txt', 'a') as f:
        block = subprocess.run(["../zcash/src/zcash-cli", "getblock", str(x), "2"], capture_output=True)
        block_string = block.stdout.decode('utf-8')
        block_dict = json.loads(block_string)
        txs = block_dict['tx']
        for tx in txs: 
            v_outs = tx['vout']
            for v_out in v_outs:
                if v_out['scriptPubKey']:
                    scriptPubKey = v_out['scriptPubKey']
                    if scriptPubKey['type'] != 'nulldata':
                        addresses = v_out['scriptPubKey']['addresses']
                        for address in addresses:
                            f.write(str(address)+'\n')
    x += 1