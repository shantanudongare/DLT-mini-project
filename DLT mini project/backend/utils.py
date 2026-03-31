"""
Utility functions for the DLT mini project
"""
import hashlib
import json
from datetime import datetime


def calculate_hash(data):
    """
    Calculate SHA-256 hash of data
    
    Args:
        data: Dictionary or string to hash
        
    Returns:
        String: SHA-256 hash
    """
    if isinstance(data, dict):
        data = json.dumps(data, sort_keys=True)
    elif not isinstance(data, str):
        data = str(data)
    
    return hashlib.sha256(data.encode()).hexdigest()


def get_timestamp():
    """Get current timestamp"""
    return datetime.now().isoformat()


def format_transaction(sender, receiver, amount):
    """
    Format transaction data
    
    Args:
        sender: Sender name
        receiver: Receiver name
        amount: Transaction amount
        
    Returns:
        Dictionary: Formatted transaction
    """
    return {
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "timestamp": get_timestamp()
    }


def validate_transaction(transaction):
    """
    Validate transaction structure
    
    Args:
        transaction: Transaction dictionary
        
    Returns:
        Boolean: True if valid, False otherwise
    """
    required_fields = ["sender", "receiver", "amount"]
    
    if not isinstance(transaction, dict):
        return False
    
    for field in required_fields:
        if field not in transaction:
            return False
    
    try:
        amount = float(transaction["amount"])
        if amount <= 0:
            return False
    except (ValueError, TypeError):
        return False
    
    return True
