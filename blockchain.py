import time
from block import Block

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block")

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.difficulty = 4  

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block):
        while block.hash[:self.difficulty] != "0" * self.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined: {block.hash}")
