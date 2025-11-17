const API_BASE = "http://localhost:5000/api";

async function addExpense() {
    const title = document.getElementById("title").value;
    const amount = document.getElementById("amount").value;
    const category = document.getElementById("category").value;

    const res = await fetch(`${API_BASE}/add`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, amount, category })
    });

    if (res.ok) {
        alert("Expense Added!");
        loadExpenses();
    }
}

async function loadExpenses() {
    const res = await fetch(`${API_BASE}/list`);
    const data = await res.json();

    const table = document.getElementById("expenseTable");
    table.innerHTML = "";

    data.forEach((exp) => {
        table.innerHTML += `
            <tr>
                <td>${exp.id}</td>
                <td>${exp.title}</td>
                <td>${exp.amount}</td>
                <td>${exp.category}</td>
            </tr>
        `;
    });
}

loadExpenses();
