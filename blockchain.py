import hashlib #hashlib library for cryptographic hashing
import time


class Block:
    def __init__(self, index, PrevHash, TimeStamp, trans):
        self.index = index #position of the block in the blockchain
        self.PrevHash = PrevHash
        self.TimeStamp = TimeStamp #TimeStamp indicating when the block was created
        self.trans = trans #list of trans or data included in the block
        self.curr_hash = self.calculateHash()#hash of the block itself

    #method calculates the hash of the block 
    def calculateHash(self):
     return hashlib.sha256(
         # It concatenates the block's attributes
        str(self.index).encode() +
        str(self.PrevHash).encode() +
        str(self.TimeStamp).encode() +
        str(self.trans).encode()
    ).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

# creates the genesis block with index 0, a previous hash of "0," 
# a TimeStamp based on the current time
    def createGenesisBlock(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

# adds a new block to the blockchain. It sets the previous hash of 
# the new block to the current hash of the last block in the chain 
# and recalculates the current hash of the new block.
    def addBlock(self, new_block):
        new_block.PrevHash = self.chain[-1].curr_hash
        new_block.curr_hash = new_block.calculateHash()
        self.chain.append(new_block)

