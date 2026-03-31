"""
Centralized System: Single server handles all transactions
"""
import time
from utils import validate_transaction, get_timestamp


class CentralizedSystem:
    """Simulates a centralized transaction processing system"""
    
    def __init__(self):
        """Initialize the centralized system"""
        self.transactions = []  # All transactions stored here
        self.is_server_running = True  # Server status
        self.processing_times = []  # Track processing times
    
    def process_transaction(self, sender, receiver, amount):
        """
        Process a single transaction
        
        Args:
            sender: Sender name
            receiver: Receiver name
            amount: Transaction amount
            
        Returns:
            Dictionary: Result with success status and time taken
        """
        start_time = time.time()
        
        if not self.is_server_running:
            return {
                "success": False,
                "message": "Server is down. Transaction failed.",
                "time_taken": 0
            }
        
        # Validate transaction
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        
        if not validate_transaction(transaction):
            return {
                "success": False,
                "message": "Invalid transaction data",
                "time_taken": 0
            }
        
        # Process transaction (simulate processing time)
        time.sleep(0.01)  # Simulate 10ms processing time
        
        # Store transaction
        transaction["id"] = len(self.transactions) + 1
        transaction["timestamp"] = get_timestamp()
        transaction["status"] = "confirmed"
        self.transactions.append(transaction)
        
        end_time = time.time()
        time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
        self.processing_times.append(time_taken)
        
        return {
            "success": True,
            "message": f"Transaction {transaction['id']} processed successfully",
            "transaction_id": transaction["id"],
            "time_taken": round(time_taken, 2)
        }
    
    def get_transactions(self):
        """
        Get all transactions
        
        Returns:
            List: All transactions
        """
        return self.transactions.copy()
    
    def get_transaction_count(self):
        """Get total number of transactions"""
        return len(self.transactions)
    
    def simulate_server_failure(self):
        """Simulate server failure"""
        self.is_server_running = False
        return {"status": "Server is now DOWN"}
    
    def restore_server(self):
        """Restore server from failure"""
        self.is_server_running = True
        return {"status": "Server is now UP"}
    
    def get_system_status(self):
        """Get current system status"""
        return {
            "server_running": self.is_server_running,
            "total_transactions": len(self.transactions),
            "status_message": "Server is UP" if self.is_server_running else "Server is DOWN"
        }
    
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
        """Clear all transactions (for testing)"""
        self.transactions = []
        self.processing_times = []
        return {"status": "Data cleared"}
