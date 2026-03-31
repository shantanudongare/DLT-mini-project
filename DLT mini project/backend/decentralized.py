"""
Decentralized System: Multiple nodes with consensus mechanism
"""
import time
from blockchain import Blockchain
from utils import validate_transaction, get_timestamp


class Node:
    """Represents a single node in the decentralized network"""
    
    def __init__(self, node_id):
        """
        Initialize a node
        
        Args:
            node_id: Unique identifier for the node
        """
        self.node_id = node_id
        self.blockchain = Blockchain()
        self.is_active = True  # Node active status
    
    def validate_transaction(self, transaction):
        """
        Validate transaction at this node
        
        Args:
            transaction: Transaction to validate
            
        Returns:
            Boolean: True if valid
        """
        if not self.is_active:
            return False
        return validate_transaction(transaction)
    
    def add_transaction(self, transaction):
        """Add transaction to the node's blockchain"""
        if self.is_active:
            self.blockchain.add_transaction(transaction)
    
    def mine_block(self):
        """Mine a new block"""
        if self.is_active:
            return self.blockchain.mine_block()
        return None
    
    def get_blockchain(self):
        """Get the blockchain"""
        return self.blockchain


class DecentralizedSystem:
    """Simulates a decentralized transaction processing system with consensus"""
    
    def __init__(self, num_nodes=3):
        """
        Initialize the decentralized system
        
        Args:
            num_nodes: Number of nodes in the network (default 3)
        """
        self.num_nodes = num_nodes
        self.nodes = [Node(i) for i in range(num_nodes)]
        self.consensus_threshold = (num_nodes // 2) + 1  # Majority needed
        self.transaction_pool = []  # Pending transactions
        self.processing_times = []  # Track processing times
        self.failed_nodes = set()  # Track failed nodes
    
    def process_transaction(self, sender, receiver, amount):
        """
        Process transaction with consensus
        
        Args:
            sender: Sender name
            receiver: Receiver name
            amount: Transaction amount
            
        Returns:
            Dictionary: Result with success status and time taken
        """
        start_time = time.time()
        
        # Create transaction
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": get_timestamp()
        }
        
        if not validate_transaction(transaction):
            return {
                "success": False,
                "message": "Invalid transaction data",
                "time_taken": 0
            }
        
        # Get active nodes
        active_nodes = [node for node in self.nodes if node.is_active]
        
        if len(active_nodes) < self.consensus_threshold:
            return {
                "success": False,
                "message": f"Not enough active nodes. Need {self.consensus_threshold}, have {len(active_nodes)}",
                "time_taken": 0
            }
        
        # Validate with active nodes
        valid_votes = 0
        for node in active_nodes:
            if node.validate_transaction(transaction):
                valid_votes += 1
        
        # Check consensus
        if valid_votes < self.consensus_threshold:
            return {
                "success": False,
                "message": "Consensus failed. Transaction rejected.",
                "time_taken": 0
            }
        
        # Distribute transaction to all active nodes
        for node in active_nodes:
            node.add_transaction(transaction)
        
        # Mine block on all nodes
        time.sleep(0.02)  # Simulate mining time
        for node in active_nodes:
            node.mine_block()
        
        end_time = time.time()
        time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
        self.processing_times.append(time_taken)
        
        return {
            "success": True,
            "message": "Transaction processed and mined with consensus",
            "active_nodes": len(active_nodes),
            "time_taken": round(time_taken, 2)
        }
    
    def simulate_node_failure(self, node_id):
        """
        Simulate failure of a specific node
        
        Args:
            node_id: ID of node to fail (0 to num_nodes-1)
            
        Returns:
            Dictionary: Result status
        """
        if 0 <= node_id < self.num_nodes:
            self.nodes[node_id].is_active = False
            self.failed_nodes.add(node_id)
            return {
                "success": True,
                "message": f"Node {node_id} is now DOWN",
                "active_nodes": len([n for n in self.nodes if n.is_active])
            }
        return {"success": False, "message": "Invalid node ID"}
    
    def restore_node(self, node_id):
        """
        Restore a failed node
        
        Args:
            node_id: ID of node to restore
            
        Returns:
            Dictionary: Result status
        """
        if 0 <= node_id < self.num_nodes:
            self.nodes[node_id].is_active = True
            self.failed_nodes.discard(node_id)
            return {
                "success": True,
                "message": f"Node {node_id} is now UP",
                "active_nodes": len([n for n in self.nodes if n.is_active])
            }
        return {"success": False, "message": "Invalid node ID"}
    
    def get_all_transactions(self):
        """Get all transactions from all active nodes"""
        # Use first active node as reference
        for node in self.nodes:
            if node.is_active:
                return node.blockchain.get_all_transactions()
        return []
    
    def get_network_status(self):
        """Get network status"""
        active_count = len([n for n in self.nodes if n.is_active])
        
        return {
            "total_nodes": self.num_nodes,
            "active_nodes": active_count,
            "inactive_nodes": self.num_nodes - active_count,
            "consensus_threshold": self.consensus_threshold,
            "network_healthy": active_count >= self.consensus_threshold,
            "node_status": [
                {"node_id": i, "status": "UP" if self.nodes[i].is_active else "DOWN"}
                for i in range(self.num_nodes)
            ]
        }
    
    def get_blockchain_validity(self):
        """Check if blockchains are valid on all active nodes"""
        validity_results = {}
        
        for node in self.nodes:
            if node.is_active:
                is_valid = node.blockchain.is_chain_valid()
                validity_results[f"Node_{node.node_id}"] = {
                    "valid": is_valid,
                    "blocks": len(node.blockchain.chain)
                }
        
        return validity_results
    
    def tamper_block_on_node(self, node_id, block_index):
        """
        Tamper with a block on a specific node
        
        Args:
            node_id: ID of node
            block_index: Index of block to tamper with
        """
        if 0 <= node_id < self.num_nodes:
            self.nodes[node_id].blockchain.tamper_block(block_index)
    
    def get_performance_stats(self):
        """Get performance statistics"""
        if not self.processing_times:
            return {
                "total_transactions": 0,
                "average_time_ms": 0,
                "min_time_ms": 0,
                "max_time_ms": 0,
                "total_time_ms": 0
            }
        
        return {
            "total_transactions": len(self.processing_times),
            "average_time_ms": round(sum(self.processing_times) / len(self.processing_times), 2),
            "min_time_ms": round(min(self.processing_times), 2),
            "max_time_ms": round(max(self.processing_times), 2),
            "total_time_ms": round(sum(self.processing_times), 2)
        }
    
    def clear_data(self):
        """Clear all data (for testing)"""
        self.__init__(self.num_nodes)
        return {"status": "Data cleared"}
