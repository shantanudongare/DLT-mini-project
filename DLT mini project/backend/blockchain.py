"""
Simple Blockchain implementation for Decentralized System
"""
from utils import calculate_hash, get_timestamp, validate_transaction


class Block:
    """Represents a single block in the blockchain"""
    
    def __init__(self, index, transactions, previous_hash):
        """
        Initialize a block
        
        Args:
            index: Block index/position
            transactions: List of transactions
            previous_hash: Hash of previous block
        """
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = get_timestamp()
        self.hash = self.calculate_block_hash()
    
    def calculate_block_hash(self):
        """Calculate hash of this block"""
        block_data = {
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp
        }
        return calculate_hash(block_data)
    
    def to_dict(self):
        """Convert block to dictionary"""
        return {
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "hash": self.hash
        }


class Blockchain:
    """Manages the blockchain"""
    
    def __init__(self):
        """Initialize blockchain with genesis block"""
        self.chain = []
        self.pending_transactions = []
        self.mining_difficulty = 2  # Not used for this simple version
        
        # Create genesis block
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        """Get the last block in the chain"""
        return self.chain[-1]
    
    def add_transaction(self, transaction):
        """
        Add a transaction to pending transactions
        
        Args:
            transaction: Transaction dictionary
            
        Returns:
            Boolean: True if added successfully
        """
        if not validate_transaction(transaction):
            return False
        
        self.pending_transactions.append(transaction)
        return True
    
    def mine_block(self):
        """
        Mine a new block with pending transactions
        
        Returns:
            Block: The newly created block
        """
        if not self.pending_transactions:
            return None
        
        prev_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions.copy(),
            previous_hash=prev_block.hash
        )
        
        self.chain.append(new_block)
        self.pending_transactions = []
        
        return new_block
    
    def is_chain_valid(self):
        """
        Validate the entire blockchain
        
        Returns:
            Boolean: True if valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify current block hash
            if current_block.hash != current_block.calculate_block_hash():
                return False
            
            # Verify link to previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def get_chain(self):
        """Get all blocks in the chain"""
        return [block.to_dict() for block in self.chain]
    
    def get_all_transactions(self):
        """Get all transactions from all blocks (excluding genesis)"""
        transactions = []
        for block in self.chain[1:]:  # Skip genesis block
            transactions.extend(block.transactions)
        return transactions
    
    def tamper_block(self, block_index):
        """
        Tamper with a block (for testing detection)
        
        Args:
            block_index: Index of block to tamper with
        """
        if 0 <= block_index < len(self.chain):
            block = self.chain[block_index]
            if block.transactions:
                # Modify the first transaction's amount
                block.transactions[0]["amount"] = block.transactions[0].get("amount", 0) * 2
            # Hash will not be updated, creating a tamper
