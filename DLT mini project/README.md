# Centralized vs Decentralized System Simulation

A comprehensive mini project demonstrating the differences between **centralized** and **decentralized** transaction processing systems using Python Flask and vanilla JavaScript.

## 📋 Project Overview

This project simulates and compares:
- **Centralized System**: Single server handling all transactions
- **Decentralized System**: Multiple nodes with consensus-based validation

### Key Features

✅ **Transaction Processing**: Add and process transactions in both systems
✅ **Real-time Monitoring**: Live dashboard with performance metrics
✅ **Failure Simulation**: Simulate server failure (centralized) and node failures (decentralized)
✅ **Blockchain Implementation**: Simple blockchain with SHA-256 hashing
✅ **Tampering Detection**: Modified block detection and validation
✅ **Performance Comparison**: Track and compare processing times
✅ **Consensus Mechanism**: Majority-based consensus for decentralized system
✅ **Clean UI**: Responsive, colorful interface with no heavy dependencies

## 📁 Project Structure

```
DLT mini project/
├── backend/
│   ├── app.py                 # Flask application & API endpoints
│   ├── centralized.py         # Centralized system implementation
│   ├── decentralized.py       # Decentralized system with nodes & consensus
│   ├── blockchain.py          # Blockchain & block classes
│   └── utils.py               # Utility functions (hashing, validation)
└── frontend/
    ├── templates/
    │   └── index.html         # Main HTML page
    └── static/
        ├── style.css          # Styling (responsive, colorful)
        └── script.js          # Frontend logic & API calls
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Clone or Download the Project

```bash
cd "C:\Users\Shantanu Dongre\OneDrive\Desktop\DLT mini project"
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install flask
```

That's it! This project only requires Flask. No heavy dependencies.

## 🎮 Running the Project

### Start the Flask Server

```bash
# Navigate to backend directory
cd backend

# Run the Flask app
python app.py
```

You'll see output like:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Access the Web Interface

Open your browser and go to:
```
http://localhost:5000
```

Or simply click: `http://127.0.0.1:5000`

## 📖 How to Use

### 1. **Adding Transactions**

1. Select the system: **Centralized** or **Decentralized**
2. Enter:
   - **Sender**: Name of the sender
   - **Receiver**: Name of the receiver
   - **Amount**: Transaction amount (must be positive)
3. Click **"Add Transaction"**
4. Transaction is processed and displayed in logs

### 2. **Monitoring Performance**

Both system panels display:
- **Total Time**: Sum of all transaction processing times
- **Avg Time/Tx**: Average processing time per transaction
- **Min/Max**: Minimum and maximum processing times

**Note**: The decentralized system typically takes longer due to consensus mechanism.

### 3. **Simulating Failures**

#### Centralized System:
- Click **"Simulate Failure"** → Server goes DOWN
- New transactions will fail with: "Server is down"
- Click **"Restore System"** → Server comes UP

#### Decentralized System:
- Click **"Fail Node 0/1/2"** → Individual nodes go DOWN
- If majority of nodes are down, transactions will fail
- Nodes continue operating independently when active

### 4. **Tampering Detection**

1. Add at least 2 transactions to decentralized system
2. Go to **"Blockchain Integrity & Tampering Detection"**
3. Select a **Node** and **Block**
4. Click **"Tamper Block"**
5. The block is modified, and blockchain validity is checked
6. Invalid blocks are marked with **✗ INVALID**

**How it works**: 
- Each block is hashed based on its contents
- When data is modified, the hash changes
- The blockchain detects the mismatch and marks it invalid

### 5. **Transaction Logs**

Both systems display the last 10 transactions with:
- Sender and receiver names
- Transaction amount
- Timestamp

### 6. **System Comparison**

Scroll down to see the **System Comparison Summary** table showing:
- Single point of failure
- Processing speed
- Consensus requirements
- Tampering detection strength
- Scalability
- Trust model

## 📊 API Endpoints

### Centralized System

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/centralized/add_transaction` | POST | Add a transaction |
| `/api/centralized/get_logs` | GET | Get all transactions |
| `/api/centralized/simulate_failure` | POST | Fail the server |
| `/api/centralized/restore` | POST | Restore the server |
| `/api/centralized/status` | GET | Get server status |
| `/api/centralized/performance` | GET | Get performance stats |
| `/api/centralized/clear` | POST | Clear all data |

### Decentralized System

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/decentralized/add_transaction` | POST | Add a transaction |
| `/api/decentralized/get_logs` | GET | Get all transactions |
| `/api/decentralized/simulate_failure` | POST | Fail a node |
| `/api/decentralized/restore` | POST | Restore a node |
| `/api/decentralized/status` | GET | Get network status |
| `/api/decentralized/blockchain_validity` | GET | Check blockchain validity |
| `/api/decentralized/tamper_block` | POST | Tamper with a block |
| `/api/decentralized/performance` | GET | Get performance stats |
| `/api/decentralized/clear` | POST | Clear all data |

## 🔧 Key Implementation Details

### Centralized System (`backend/centralized.py`)

```python
# Features:
- Single server handles all transactions
- Instant processing (with 10ms simulation)
- Single point of failure
- No consensus needed
- Easy tampering (no detection)
```

### Decentralized System (`backend/decentralized.py`)

```python
# Features:
- 3 nodes with independent blockchains
- Transactions validated by all active nodes
- Majority consensus (2 out of 3 nodes)
- Longer processing time (with mining)
- Tamper detection across nodes
```

### Blockchain (`backend/blockchain.py`)

```python
# Features:
- Block structure: index, transactions, hashes
- Genesis block (index 0)
- SHA-256 hashing
- Chain validation
- Tamper detection
```

### Consensus Mechanism

Transactions are validated when:
1. At least 2 (majority) active nodes approve
2. Transaction structure is valid
3. Transaction is mined into a new block

If majority fails, transaction is rejected.

## 📈 Performance Observations

### Typical Results:

**Centralized System:**
- Avg time: ~10-15ms per transaction
- No failure handling
- Instant when server is down → error

**Decentralized System:**
- Avg time: ~20-30ms per transaction (due to consensus)
- Survives up to 1 node failure (2 nodes remain active)
- Fault-tolerant architecture

## 🛡️ Security Features

1. **Input Validation**: All transactions validated
2. **Hash Verification**: SHA-256 hashing prevents tampering
3. **Consensus**: Prevents single node from corrupting data
4. **Blockchain Immutability**: Changing past blocks is detected
5. **Distributed Trust**: No single authority

## 🐛 Troubleshooting

### Port 5000 Already in Use

```bash
# On Windows, find process using port 5000:
netstat -ano | findstr :5000

# On macOS/Linux:
lsof -i :5000

# Then kill the process or use a different port by editing app.py:
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)  # Changed to 5001
```

### Module Not Found (Flask)

```bash
pip install flask
```

### Frontend Not Loading

- Ensure Flask is running
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console for errors (F12)

### Transactions Not Appearing

- Check browser console for JS errors
- Ensure backend is running
- Refresh the page

## 📚 Understanding the Flow

### Adding a Transaction - Centralized:

```
Frontend → POST /api/centralized/add_transaction
        → Validate inputs
        → Process immediately (if server running)
        → Store in list
        → Return success/failure
        → Frontend updates display
```

### Adding a Transaction - Decentralized:

```
Frontend → POST /api/decentralized/add_transaction
        → Get all active nodes
        → Request validation from all nodes (consensus)
        → If majority approves:
            → Add to all nodes' pending pool
            → Mine block on all nodes
            → Return success
        → Else return failure
        → Frontend updates display
```

## 🎓 Learning Outcomes

After using this project, you'll understand:

1. ✅ **Centralized Systems**: Fast but fragile, single point of failure
2. ✅ **Decentralized Systems**: Slower but robust, distributed trust
3. ✅ **Blockchain Basics**: Hashing, blocks, chains, immutability
4. ✅ **Consensus Mechanisms**: How agreement is reached distributively
5. ✅ **Failure Handling**: System behavior under degraded conditions
6. ✅ **Tampering Detection**: How blockchain detects modifications
7. ✅ **Trade-offs**: Speed vs. security, centralization vs. decentralization

## 📝 Code Quality

- ✅ Clean, readable code
- ✅ Modular architecture
- ✅ Comprehensive comments
- ✅ No unnecessary dependencies
- ✅ Error handling
- ✅ Responsive UI

## 🚪 Exit

To stop the server:
1. In terminal: Press **Ctrl+C**
2. Deactivate virtual environment (if used):
   ```bash
   deactivate
   ```

## 📧 Notes

- The project uses in-memory storage (data resets when server restarts)
- No database is required
- All operations are simulated for demonstration
- Processing times are artificially added for realism

## 🎯 Future Enhancements (Optional)

- Database integration (persistent storage)
- Smart contracts simulation
- Advanced consensus mechanisms (PoW, PoS)
- Real network communication between nodes
- WebSocket for real-time updates
- More nodes in decentralized system
- Transaction fee simulation
- Account balances verification

## 📄 License

This is an educational project. Feel free to modify and distribute.

---

**Happy Learning! 🚀**

For any issues or questions, check the browser console (F12) and Flask server logs.
