import hashlib
import time
import json

class TsarBlock:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f'{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}'
        return hashlib.sha256(block_string.encode()).hexdigest()

def create_genesis_block():
    return TsarBlock(0, "0", time.time(), "Да будет ЦарьКоин!")

def create_next_block(previous_block, data=""):
    index = previous_block.index + 1
    timestamp = time.time()
    new_block = TsarBlock(index, previous_block.hash, timestamp, data)
    return new_block

# Тест создания блоков
blockchain = [create_genesis_block()]
for i in range(1, 5):
    block = create_next_block(blockchain[-1], f"Блок номер {i}")
    blockchain.append(block)
    print(json.dumps(block.__dict__, indent=4))
