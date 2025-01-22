import hashlib
import json
import time

class BlockchainLogger:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': [],
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        return block

    def hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_data(self, data):
        self.chain[-1]['data'].append(data)
        self.chain[-1]['hash'] = self.hash_block(self.chain[-1])

    def log_event(self, event):
        self.add_data(event)

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            if current_block['hash'] != self.hash_block(current_block):
                return False
        return True

    def get_chain(self):
        return self.chain

    def integrate_with_new_components(self, new_component_data):
        self.add_data(new_component_data)
        return self.chain

    def ensure_compatibility(self, existing_data, new_component_data):
        self.add_data(existing_data)
        self.add_data(new_component_data)
        return self.chain
