# QUICK START GUIDE

## ⚡ The Fastest Way to Run the Project

### 1️⃣ Install Python (if not already installed)
Download from: https://www.python.org/downloads/

### 2️⃣ Open Terminal/Command Prompt

Navigate to the project folder:
```
cd "C:\Users\Shantanu Dongre\OneDrive\Desktop\DLT mini project"
```

### 3️⃣ Install Flask

```
pip install flask
```

### 4️⃣ Run the Server

```
cd backend
python app.py
```

### 5️⃣ Open Browser

Go to: **http://localhost:5000**

---

## ✨ That's It! Start Using

### Try These:

1. **Add a Transaction**
   - Select system (Centralized or Decentralized)
   - Enter sender, receiver, amount
   - Click "Add Transaction"

2. **Simulate Failure**
   - Click "Simulate Failure" button
   - Try adding another transaction (should fail)
   - Click "Restore System" to recover

3. **Tamper Detection**
   - Add 2-3 transactions in Decentralized mode
   - Go to "Blockchain Integrity & Tampering Detection"
   - Select Node and Block
   - Click "Tamper Block"
   - See how blockchain detects tampering

---

## 🆘 If Something Goes Wrong

### Error: "ModuleNotFoundError: No module named 'flask'"
```
pip install flask
```

### Error: "Port 5000 already in use"
1. Edit `backend/app.py` last line:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Change 5000 to 5001
```
2. Then access: http://localhost:5001

### Error: "Frontend not loading"
- Make sure Flask is running
- Check browser console (F12) for errors
- Try clearing browser cache

---

## 📚 What Each Component Does

**Centralized System:**
- Single server processes all transactions
- If server fails → all transactions fail
- Demonstrates: Single point of failure, speed, centralized control

**Decentralized System:**
- 3 independent nodes working together
- Majority consensus (2 out of 3) needed
- Survives 1 node failure
- Demonstrates: Fault tolerance, distributed decision making, slower but safer

**Blockchain Features:**
- SHA-256 hashing for security
- Block tampering detection
- Chain validation

---

## 📊 Performance Tips

**Understanding Results:**

- **Centralized**: ~10-15ms per transaction (fast but fragile)
- **Decentralized**: ~20-30ms per transaction (slower but robust)

**Why Decentralized is Slower:**
- Needs consensus from multiple nodes
- Mining simulation adds time
- Worth the trade-off for reliability

---

## 🎓 Educational Value

Learn hands-on:
- How blockchain works
- Trade-offs between centralization and decentralization
- Consensus mechanisms
- Failure handling
- Tampering detection
- Distributed systems

---

**Questions? Check README.md for detailed documentation.**

**Ready? http://localhost:5000** 🚀
