import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = (str(self.index) + self.previous_hash + str(self.timestamp) +
                         str(self.data) + str(self.nonce))
        return hashlib.sha256(block_content.encode()).hexdigest()
