import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block: 
    
    data=" "
    hash=" "
    prev_hash=" "
    
    def __init__(self, data, hash, prev_hash) :
        self.data=data 
        self.hash=hash
        self.prev_hash=prev_hash
        

class Blockchain: 
    def __init__(self):
        hashlast=hashGenerator('gen_last')
        hashstart=hashGenerator('gen_hash')
        
        genesis=Block('gen_data',hashstart,hashlast)
        self.chain=[genesis]
        
    def add_block(self, data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)
        
bc=Blockchain()
bc.add_block('I am Fahim, I have 100 taka')
bc.add_block('Jaoyad has no money')

for block in bc.chain: 
    print(block.__dict__)
        
        #testing
        