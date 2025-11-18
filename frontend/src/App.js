import React, { useState, useEffect } from "react";

function App() {
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");
  const [date, setDate] = useState("");
  const [category, setCategory] = useState("");

  const API_URL = "http://127.0.0.1:5000/api/expenses";

  const fetchExpenses = () => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        setExpenses(data);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  const handleAddExpense = (e) => {
    e.preventDefault();
    const newExpense = { title, amount, date, category };

    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newExpense),
    })
      .then((res) => res.json())
      .then((data) => {
        fetchExpenses(); // refresh table
        setTitle(""); setAmount(""); setDate(""); setCategory("");
      });
  };

  return (
    <div className="App">
      <h1>Expense Management</h1>

      <form onSubmit={handleAddExpense} style={{ marginBottom: "20px" }}>
        <input placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <input placeholder="Amount" value={amount} onChange={(e) => setAmount(e.target.value)} required />
        <input placeholder="Date" type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
        <input placeholder="Category" value={category} onChange={(e) => setCategory(e.target.value)} required />
        <button type="submit">Add Expense</button>
      </form>

      {loading ? <p>Loading...</p> :
        <table border="1" style={{ margin: "auto" }}>
          <thead>
            <tr>
              <th>ID</th><th>Title</th><th>Amount</th><th>Date</th><th>Category</th>
            </tr>
          </thead>
          <tbody>
            {expenses.map((exp) => (
              <tr key={exp.id}>
                <td>{exp.id}</td>
                <td>{exp.title}</td>
                <td>{exp.amount}</td>
                <td>{exp.date}</td>
                <td>{exp.category}</td>
              </tr>
            ))}
          </tbody>
        </table>
      }
    </div>
  );
}

export default App;

