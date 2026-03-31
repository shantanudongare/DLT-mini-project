/**
 * 💰 MONEY TRANSFER GAME - Frontend JavaScript
 * Fun and interactive learning experience!
 */

// ============================================================================
// GLOBAL STATE
// ============================================================================

let selectedSystem = null;

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎮 Money Transfer Game Started!');
    
    // Setup mode card clicks
    document.querySelectorAll('.mode-card').forEach(card => {
        card.addEventListener('click', function() {
            const system = this.dataset.system;
            selectSystem(system);
        });
    });

    // Only refresh when needed (after transactions or manual actions)
    // No continuous polling - better for performance!
});

// ============================================================================
// SYSTEM SELECTION
// ============================================================================

function selectSystem(system) {
    selectedSystem = system;
    
    // Update UI
    document.querySelectorAll('.mode-card').forEach(card => {
        card.classList.remove('active');
    });
    document.querySelector(`[data-system="${system}"]`).classList.add('active');
    
    // Show/hide sections
    document.getElementById('centralized-section').style.display = system === 'centralized' ? 'block' : 'none';
    document.getElementById('decentralized-section').style.display = system === 'decentralized' ? 'block' : 'none';
    
    // Fun message
    if (system === 'centralized') {
        showMessage('🏦 Bank Mode Selected! One server rules them all!', 'success');
    } else {
        showMessage('⛓️ Crypto Mode Selected! Distributed power!', 'success');
    }
    
    refreshDashboard();
    console.log(`✅ System changed to: ${system}`);
}

// ============================================================================
// QUICK TRANSACTION (PRESETS)
// ============================================================================

function quickTransaction(sender, receiver, amount) {
    if (!selectedSystem) {
        showMessage('Pick a system first! 🎮', 'error');
        return;
    }
    
    document.getElementById('sender').value = sender;
    document.getElementById('receiver').value = receiver;
    document.getElementById('amount').value = amount;
    
    addTransaction();
}

// ============================================================================
// TRANSACTION HANDLING
// ============================================================================

async function addTransaction() {
    if (!selectedSystem) {
        showMessage('🎮 Pick Bank Mode or Crypto Mode first!', 'error');
        return;
    }
    
    const sender = document.getElementById('sender').value.trim();
    const receiver = document.getElementById('receiver').value.trim();
    const amount = parseInt(document.getElementById('amount').value);
    
    // Validation
    if (!sender || !receiver) {
        showMessage('⚠️ Enter both names! (e.g., Alice and Bob)', 'error');
        return;
    }
    
    if (!amount || amount <= 0) {
        showMessage('⚠️ Amount must be a positive number!', 'error');
        return;
    }
    
    if (amount > 999) {
        showMessage('💰 Max amount is 999! (Too rich!)', 'error');
        return;
    }
    
    // Clear inputs
    document.getElementById('sender').value = '';
    document.getElementById('receiver').value = '';
    document.getElementById('amount').value = '';
    
    const endpoint = selectedSystem === 'centralized'
        ? '/api/centralized/add_transaction'
        : '/api/decentralized/add_transaction';
    
    try {
        const payload = { sender, receiver, amount };
        console.log('💳 Sending transaction:', payload);
        console.log('📍 Endpoint:', endpoint);
        
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
        console.log('📨 Server response:', data);
        
        if (data.success) {
            playSuccessAnimation();
            showMessage(`✅ Success! ${sender} sent 💰$${amount} to ${receiver}!`, 'success');
            setTimeout(() => refreshDashboard(), 500);
        } else {
            playFailAnimation();
            showMessage(`❌ Failed: ${data.message}`, 'error');
        }
    } catch (error) {
        showMessage(`💥 Error: ${error.message}`, 'error');
    }
}

// ============================================================================
// SYSTEM CONTROL
// ============================================================================

async function simulateFailure() {
    if (!selectedSystem) {
        showMessage('Pick a system first!', 'error');
        return;
    }
    
    let endpoint, data, msg;
    
    if (selectedSystem === 'centralized') {
        endpoint = '/api/centralized/simulate_failure';
        data = {};
        msg = '💥 CRASH! Bank Server is DOWN! All transactions will fail!';
    } else {
        endpoint = '/api/decentralized/simulate_failure';
        data = { node_id: 0 };
        msg = '⚠️ Node 1 Failed! Network still working with 2 computers! 💻';
    }
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        playShakeAnimation();
        showMessage(msg, 'error');
        refreshDashboard();
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    }
}

async function restoreSystem() {
    if (!selectedSystem) {
        showMessage('Pick a system first!', 'error');
        return;
    }
    
    let endpoint, data, msg;
    
    if (selectedSystem === 'centralized') {
        endpoint = '/api/centralized/restore';
        data = {};
        msg = '✅ Bank Server is BACK UP! All systems go!';
    } else {
        endpoint = '/api/decentralized/restore';
        data = { node_id: 0 };
        msg = '✅ Node 1 Restored! All 3 computers working again!';
    }
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        playSuccessAnimation();
        showMessage(msg, 'success');
        refreshDashboard();
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    }
}

async function failNode(nodeId) {
    const nodeNames = ['Node 1', 'Node 2', 'Node 3'];
    
    try {
        const response = await fetch('/api/decentralized/simulate_failure', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ node_id: nodeId })
        });
        
        const result = await response.json();
        
        if (result.success) {
            playShakeAnimation();
            showMessage(`💥 ${nodeNames[nodeId]} DOWN! Still have ${result.active_nodes} computers working!`, 'error');
            
            // Update node button
            const btn = document.getElementById(`node-btn-${nodeId}`);
            if (btn) {
                btn.classList.add('failed');
                btn.classList.remove('active');
            }
            
            refreshDashboard();
        }
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    }
}

async function clearAllData() {
    if (!confirm('🗑️ Delete ALL transactions? This is forever!')) {
        return;
    }

    const endpoint = selectedSystem === 'centralized'
        ? '/api/centralized/clear'
        : '/api/decentralized/clear';

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        const result = await response.json();
        document.getElementById('sender').value = '';
        document.getElementById('receiver').value = '';
        document.getElementById('amount').value = '';
        playSuccessAnimation();
        showMessage('✅ All data cleared! Fresh start!', 'success');
        refreshDashboard();
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    }
}

// Animation helper functions
function playSuccessAnimation() {
    const gameArea = document.getElementById('game-area');
    if (gameArea) {
        gameArea.style.animation = 'none';
        setTimeout(() => {
            gameArea.style.animation = 'slideDown 0.6s ease-out';
        }, 10);
    }
}

function playFailAnimation() {
    const gameArea = document.getElementById('game-area');
    if (gameArea) {
        gameArea.style.animation = 'shake 0.5s ease-in-out';
    }
}

function playShakeAnimation() {
    const gameArea = document.getElementById('game-area');
    if (gameArea) {
        gameArea.style.animation = 'none';
        setTimeout(() => {
            gameArea.style.animation = 'shake 0.5s ease-in-out';
        }, 10);
    }
}

// ============================================================================
// TAMPERING & VALIDATION
// ============================================================================

async function tamperBlock() {
    const nodeId = parseInt(document.getElementById('tamper-node').value);
    const blockIndex = parseInt(document.getElementById('tamper-block').value);

    try {
        const response = await fetch('/api/decentralized/tamper_block', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                node_id: nodeId,
                block_index: blockIndex
            })
        });

        const data = await response.json();

        // Display tampering results
        displayTamperingResults(data);
        showMessage('⚠️ Block tampered! Blockchain validity checked.', 'error');
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    }
}

function displayTamperingResults(data) {
    const validityDiv = document.getElementById('validity-status');
    const validity = data.blockchain_validity;

    let html = '';
    for (const [nodeName, status] of Object.entries(validity)) {
        const validClass = status.valid ? 'valid' : 'invalid';
        const validText = status.valid ? '✓ VALID' : '✗ INVALID';
        const blockCount = status.blocks;

        html += `
            <div class="validity-item">
                <span class="node-name">${nodeName} (${blockCount} blocks)</span>
                <span class="status ${validClass}">${validText}</span>
            </div>
        `;
    }

    validityDiv.innerHTML = html;
}

// ============================================================================
// DASHBOARD REFRESH
// ============================================================================

async function refreshDashboard() {
    if (!selectedSystem) return;
    
    if (selectedSystem === 'centralized') {
        refreshCentralizedSystem();
    } else {
        refreshDecentralizedSystem();
    }
}

// === Centralized System Refresh ===

async function refreshCentralizedSystem() {
    try {
        const [statusRes, logsRes] = await Promise.all([
            fetch('/api/centralized/status'),
            fetch('/api/centralized/get_logs')
        ]);

        const status = await statusRes.json();
        const logs = await logsRes.json();
        
        console.log('🏦 Bank Status:', status);
        console.log('📝 Bank Logs:', logs);

        // Update status with emoji and text
        const serverStatus = status.server_running ? '✅' : '💥';
        const statusText = status.server_running ? 'ONLINE' : 'OFFLINE';
        
        const statusIcon = document.getElementById('cent-status-icon');
        const statusTextEl = document.getElementById('cent-status-text');
        const transactionCount = document.getElementById('cent-transaction-count');
        
        if (statusIcon) statusIcon.textContent = serverStatus;
        if (statusTextEl) statusTextEl.textContent = statusText;
        if (transactionCount) transactionCount.textContent = status.total_transactions;

        // Update logs - pass the transactions array
        if (logs && logs.transactions) {
            updateLogsDisplay('centralized', logs.transactions);
        } else {
            console.error('❌ No transactions data in response:', logs);
            updateLogsDisplay('centralized', []);
        }

    } catch (error) {
        console.error('❌ Error refreshing centralized system:', error);
    }
}

// === Decentralized System Refresh ===

async function refreshDecentralizedSystem() {
    try {
        const [statusRes, logsRes] = await Promise.all([
            fetch('/api/decentralized/status'),
            fetch('/api/decentralized/get_logs')
        ]);

        const status = await statusRes.json();
        const logs = await logsRes.json();
        
        console.log('⛓️ Crypto Status:', status);
        console.log('📝 Crypto Logs:', logs);

        // Update network status with emoji
        const healthStatus = status.network_healthy ? '✅ Healthy' : '⚠️ Degraded';
        document.getElementById('dec-active-nodes').textContent = status.active_nodes;
        document.getElementById('dec-health').textContent = healthStatus;

        // Update node button colors
        status.node_status.forEach((node, index) => {
            const btn = document.getElementById(`node-btn-${index}`);
            if (btn) {
                if (node.status === 'UP') {
                    btn.classList.remove('failed');
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                    btn.classList.add('failed');
                }
            }
        });

        // Update logs - pass the transactions array
        if (logs && logs.transactions) {
            updateLogsDisplay('decentralized', logs.transactions);
        } else {
            console.error('❌ No transactions data in response:', logs);
            updateLogsDisplay('decentralized', []);
        }

    } catch (error) {
        console.error('❌ Error refreshing decentralized system:', error);
    }
}

// ============================================================================
// DISPLAY HELPERS
// ============================================================================

function updatePerformanceDisplay(system, perf) {
    const prefix = system === 'centralized' ? 'cent' : 'dec';

    const totalTime = perf.total_time_ms.toFixed(2);
    const avgTime = perf.average_time_ms.toFixed(2);
    const minTime = perf.min_time_ms.toFixed(2);
    const maxTime = perf.max_time_ms.toFixed(2);

    document.getElementById(`${prefix}-total-time`).textContent = totalTime;
    document.getElementById(`${prefix}-avg-time`).textContent = avgTime;

    if (perf.total_transactions > 0) {
        document.getElementById(`${prefix}-min-max`).textContent = `${minTime} / ${maxTime}`;
    } else {
        document.getElementById(`${prefix}-min-max`).textContent = '-';
    }
}

function updateLogsDisplay(system, transactions) {
    const container = document.getElementById(`${system}-logs`);
    
    if (!container) {
        console.error(`Container not found: ${system}-logs`);
        return;
    }
    
    // Handle undefined or null transactions
    if (!transactions || transactions.length === 0) {
        container.innerHTML = '<p class="empty-state">No transactions yet. Send one! 👆</p>';
        return;
    }

    let html = '';
    transactions.slice(-10).reverse().forEach((tx, index) => {
        const time = tx.timestamp ? new Date(tx.timestamp).toLocaleTimeString() : 'N/A';
        html += `
            <div class="log-entry success">
                <strong>💳 ${tx.sender} → ${tx.receiver}</strong>
                <br />💰 <strong>$${tx.amount}</strong> | ⏱️ <span class="timestamp">${time}</span>
            </div>
        `;
    });

    container.innerHTML = html;
}

function displayBlockchainValidity(validity) {
    const validityDiv = document.getElementById('validity-status');

    if (Object.keys(validity).length === 0) {
        validityDiv.innerHTML = '<p class="empty-message">No data yet</p>';
        return;
    }

    let html = '';
    for (const [nodeName, status] of Object.entries(validity)) {
        const validClass = status.valid ? 'valid' : 'invalid';
        const validText = status.valid ? '✓ VALID' : '✗ INVALID';
        const blockCount = status.blocks;

        html += `
            <div class="validity-item">
                <span class="node-name">${nodeName} (${blockCount} blocks)</span>
                <span class="status ${validClass}">${validText}</span>
            </div>
        `;
    }

    validityDiv.innerHTML = html;
}

// ============================================================================
// MESSAGE DISPLAY
// ============================================================================

function showMessage(text, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
    messageDiv.style.display = 'block';

    // Auto-hide after 4 seconds
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 4000);
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

function formatTimestamp(timestamp) {
    if (!timestamp) return 'N/A';
    const date = new Date(timestamp);
    return date.toLocaleTimeString();
}

function formatNumber(num) {
    return num.toFixed(2);
}
