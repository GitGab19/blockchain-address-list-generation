import subprocess
from sys import stdout
import json

for x in range(0,1675747):
    with open('./dash_counter.txt', 'w') as fp:
        fp.write(str(x)+'\n')
    percentage = (x/(1653370))*100
    print("block number "+str(x)+" --> "+str(percentage)+"%")
    with open('./dash_addresses.txt', 'a') as f:
        block_hash = subprocess.run(["../dash/dashcore-0.17.0/bin/dash-cli", "getblockhash", str(x)], capture_output=True)
        block_hash_string = block_hash.stdout.decode('utf-8')
        block = subprocess.run(["../dash/dashcore-0.17.0/bin/dash-cli", "getblock", str(block_hash_string), "2"], capture_output=True)
        block_string = block.stdout.decode('utf-8')
        block_dict = json.loads(block_string)
        txs = block_dict['tx']
        for tx in txs: 
            v_outs = tx['vout']
            for v_out in v_outs:
                if v_out['scriptPubKey']:
                    scriptPubKey = v_out['scriptPubKey']
                    if (scriptPubKey['type'] != 'nulldata' and scriptPubKey['type'] != 'nonstandard') :
                        addresses = v_out['scriptPubKey']['addresses']
                        for address in addresses:
                            f.write(str(address)+'\n')
    x += 1