from tracemalloc import start
from web3 import Web3
import time
import threading


class myThread (threading.Thread):
   def __init__(self, threadID, name, startBlock, endBlock):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.startBlock = startBlock
      self.endBlock = endBlock
   def run(self):
      print ("Starting " + str(self.threadID))
      getAddressesThreadFunction(self.name, self.startBlock, self.endBlock)
      print ("Exiting " + str(self.name))


# Define a function for the thread
def getAddressesThreadFunction(name, startBlock, endBlock):
    start_block = startBlock
    initial_block =start_block
    end_block = endBlock
    counter = 0

    # HTTPProvider:
    w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
    res = w3.isConnected()
    print('Connected ==> ',res)
    print(start_block)
    print(end_block)

    while start_block < end_block:
        counter += 1
        block = w3.eth.get_block(start_block, True)
        transactions_list = block.transactions
        percentage = counter/(end_block-initial_block)*100
        with open('./block_counter_'+name+'.txt', 'w') as f:
            f.write('['+name.upper()+'] last block downloaded --> '+str(block.number))
        print('['+name.upper()+']' + str(block.number) + ' ---> ' + str(round(percentage,2))+'%')
        with open('./eth_addresses_'+name+'.txt', 'a') as f:
            f.write(str(block.miner).lower()) #write of miner address
            f.write('\n')
            for transaction in transactions_list:
                f.write(str(transaction.to).lower()) #write of every receiver address 
                f.write('\n')

        # Keep on iterating
        start_block += 1


# Create new threads
thread0 = myThread(0, "part0", 0, 1235848) 
thread1 = myThread(1, "part1", 1235848, 2471696)
thread2 = myThread(2, "part2", 2471696, 3707544) 
thread3 = myThread(3, "part3", 3707544, 4943392)
thread4 = myThread(4, "part4", 4943392, 6179240)  
thread5 = myThread(5, "part5", 6179240, 7415088)
thread6 = myThread(6, "part6", 7415088, 8650936)
thread7 = myThread(7, "part7", 8650936, 9886784)
thread8 = myThread(8, "part8", 9886784, 11122632) 
thread9 = myThread(9, "part9", 11122632, 12358480)
thread10 = myThread(10, "part10", 12358480, 13594328)
thread11 = myThread(11, "part11", 13594328, 14830178)

# Start new Threads
thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()