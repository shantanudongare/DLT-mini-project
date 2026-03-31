"""
Flask Backend Application for Centralized vs Decentralized System Simulation
"""
from flask import Flask, render_template, request, jsonify
from centralized import CentralizedSystem
from decentralized import DecentralizedSystem

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Initialize systems
centralized_system = CentralizedSystem()
decentralized_system = DecentralizedSystem(num_nodes=3)


# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')


# ============================================================================
# CENTRALIZED SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/centralized/add_transaction', methods=['POST'])
def centralized_add_transaction():
    """Add a transaction to centralized system"""
    data = request.json
    
    try:
        sender = data.get('sender', '').strip()
        receiver = data.get('receiver', '').strip()
        amount = float(data.get('amount', 0))
        
        if not sender or not receiver:
            return jsonify({"success": False, "message": "Sender and receiver required"})
        
        if amount <= 0:
            return jsonify({"success": False, "message": "Amount must be positive"})
        
        result = centralized_system.process_transaction(sender, receiver, amount)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route('/api/centralized/get_logs', methods=['GET'])
def centralized_get_logs():
    """Get transaction logs from centralized system"""
    transactions = centralized_system.get_transactions()
    return jsonify({
        "transactions": transactions,
        "total": len(transactions)
    })


@app.route('/api/centralized/simulate_failure', methods=['POST'])
def centralized_simulate_failure():
    """Simulate server failure"""
    result = centralized_system.simulate_server_failure()
    status = centralized_system.get_system_status()
    return jsonify({**result, **status})


@app.route('/api/centralized/restore', methods=['POST'])
def centralized_restore():
    """Restore server from failure"""
    result = centralized_system.restore_server()
    status = centralized_system.get_system_status()
    return jsonify({**result, **status})


@app.route('/api/centralized/status', methods=['GET'])
def centralized_status():
    """Get centralized system status"""
    return jsonify(centralized_system.get_system_status())


@app.route('/api/centralized/performance', methods=['GET'])
def centralized_performance():
    """Get performance statistics"""
    return jsonify(centralized_system.get_performance_stats())


@app.route('/api/centralized/clear', methods=['POST'])
def centralized_clear():
    """Clear all data"""
    result = centralized_system.clear_data()
    return jsonify(result)


# ============================================================================
# DECENTRALIZED SYSTEM ENDPOINTS
# ============================================================================

@app.route('/api/decentralized/add_transaction', methods=['POST'])
def decentralized_add_transaction():
    """Add a transaction to decentralized system"""
    data = request.json
    
    try:
        sender = data.get('sender', '').strip()
        receiver = data.get('receiver', '').strip()
        amount = float(data.get('amount', 0))
        
        if not sender or not receiver:
            return jsonify({"success": False, "message": "Sender and receiver required"})
        
        if amount <= 0:
            return jsonify({"success": False, "message": "Amount must be positive"})
        
        result = decentralized_system.process_transaction(sender, receiver, amount)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


@app.route('/api/decentralized/get_logs', methods=['GET'])
def decentralized_get_logs():
    """Get transaction logs from decentralized system"""
    transactions = decentralized_system.get_all_transactions()
    return jsonify({
        "transactions": transactions,
        "total": len(transactions)
    })


@app.route('/api/decentralized/simulate_failure', methods=['POST'])
def decentralized_simulate_failure():
    """Simulate node failure"""
    data = request.json
    node_id = data.get('node_id', 0)
    
    result = decentralized_system.simulate_node_failure(node_id)
    status = decentralized_system.get_network_status()
    return jsonify({**result, **status})


@app.route('/api/decentralized/restore', methods=['POST'])
def decentralized_restore():
    """Restore a failed node"""
    data = request.json
    node_id = data.get('node_id', 0)
    
    result = decentralized_system.restore_node(node_id)
    status = decentralized_system.get_network_status()
    return jsonify({**result, **status})


@app.route('/api/decentralized/status', methods=['GET'])
def decentralized_status():
    """Get decentralized system status"""
    return jsonify(decentralized_system.get_network_status())


@app.route('/api/decentralized/blockchain_validity', methods=['GET'])
def decentralized_blockchain_validity():
    """Check blockchain validity on all nodes"""
    return jsonify(decentralized_system.get_blockchain_validity())


@app.route('/api/decentralized/tamper_block', methods=['POST'])
def decentralized_tamper_block():
    """Tamper with a block on a node"""
    data = request.json
    node_id = data.get('node_id', 0)
    block_index = data.get('block_index', 1)
    
    decentralized_system.tamper_block_on_node(node_id, block_index)
    
    validity = decentralized_system.get_blockchain_validity()
    return jsonify({
        "message": f"Block {block_index} tampered on Node {node_id}",
        "blockchain_validity": validity
    })


@app.route('/api/decentralized/performance', methods=['GET'])
def decentralized_performance():
    """Get performance statistics"""
    return jsonify(decentralized_system.get_performance_stats())


@app.route('/api/decentralized/clear', methods=['POST'])
def decentralized_clear():
    """Clear all data"""
    result = decentralized_system.clear_data()
    return jsonify(result)


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
