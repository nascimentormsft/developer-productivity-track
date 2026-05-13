const API_BASE = "http://localhost:8000";

/**
 * Load and display transactions from the backend API.
 */
async function loadTransactions() {
    const customerFilter = document.getElementById("filter-customer").value.trim();
    let url = `${API_BASE}/transactions/`;
    if (customerFilter) {
        url += `?customer_id=${encodeURIComponent(customerFilter)}`;
    }

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        const transactions = await response.json();
        renderTransactions(transactions);
    } catch (error) {
        console.error("Failed to load transactions:", error);
        document.getElementById("transactions-body").innerHTML =
            `<tr><td colspan="7" class="error">Failed to load transactions: ${error.message}</td></tr>`;
    }
}

/**
 * Render transactions into the HTML table.
 */
function renderTransactions(transactions) {
    const tbody = document.getElementById("transactions-body");

    if (transactions.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" class="empty">No transactions found</td></tr>';
        return;
    }

    tbody.innerHTML = transactions
        .map(
            (t) => `
        <tr class="${t.is_flagged ? "flagged" : ""}">
            <td>${t.transaction_id}</td>
            <td>${t.customer_id}</td>
            <td>${t.amount.toFixed(2)}</td>
            <td>${t.currency}</td>
            <td>${t.transaction_type}</td>
            <td>${t.merchant_category}</td>
            <td>${new Date(t.timestamp).toLocaleDateString()}</td>
        </tr>
    `
        )
        .join("");
}

/*
═══════════════════════════════════════════════════════════════════
LAB EXERCISE: In Part 3, you'll add a fetchCustomerSummary function
here using Agent mode. It should:
- Call GET /transactions/summary/{customerId}
- Display the result in the #customer-summary div
- Handle 404 errors gracefully
═══════════════════════════════════════════════════════════════════
*/

// Load transactions on page load
document.addEventListener("DOMContentLoaded", loadTransactions);
