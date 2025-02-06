import hashlib
import json
import time

class BlockchainLogger:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        """
        Create a new block in the blockchain.

        Args:
            previous_hash (str): The hash of the previous block.

        Returns:
            dict: The newly created block.
        """
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
        """
        Generate a SHA-256 hash of a block.

        Args:
            block (dict): The block to hash.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_data(self, data):
        """
        Add data to the latest block in the blockchain.

        Args:
            data (str): The data to add.
        """
        self.chain[-1]['data'].append(data)
        self.chain[-1]['hash'] = self.hash_block(self.chain[-1])

    def log_event(self, event):
        """
        Log an event by adding it to the blockchain.

        Args:
            event (str): The event to log.
        """
        self.add_data(event)

    def verify_chain(self):
        """
        Verify the integrity of the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            if current_block['hash'] != self.hash_block(current_block):
                return False
        return True

    def get_chain(self):
        """
        Get the entire blockchain.

        Returns:
            list: The blockchain.
        """
        return self.chain
