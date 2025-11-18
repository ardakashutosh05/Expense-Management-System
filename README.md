# Expense-Management-System

📘 Expense Management System

A Full-Stack Project (Flask Backend + HTML/CSS/JS Frontend)

A simple, clean, and beginner-friendly Expense Management Project built using:

Python Flask (Backend API)

SQLite Database

HTML + CSS + JavaScript (Frontend UI)

REST API Architecture

🏗️ Project Overview

This project allows users to:

✔ Add expenses
✔ View all expenses
✔ Update expenses
✔ Delete expenses
✔ Store data in SQLite
✔ Connect with a clean frontend UI

📂 Folder Structure
expense-management/
│── backend/
│   ├── app.py
│   ├── expenses.db
│   └── requirements.txt
│
│── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md

🛠️ Tech Stack
Backend

Python 3

Flask

Flask-CORS

SQLite

Frontend

HTML

CSS

JavaScript

🚀 How To Run the Project
🔧 1. Backend Setup
Install dependencies
pip install -r requirements.txt

Run backend
python app.py

Backend will run at:
http://127.0.0.1:5000

🖥️ 2. Frontend Setup
Simply open:
frontend/index.html


OR use VS Code Live Server.

📡 API Documentation
📌 Base URL
http://127.0.0.1:5000

1️⃣ Get All Expenses

GET

/api/expenses


✔ Returns list of all expenses

2️⃣ Add Expense

POST

/api/expenses

Request Body (JSON)
{
  "title": "Groceries",
  "amount": "120.50",
  "category": "Food",
  "date": "2025-11-17"
}

3️⃣ Get Single Expense

GET

/api/expenses/<id>

4️⃣ Update Expense

PUT

/api/expenses/<id>

Request Body Example
{
  "title": "Updated Name",
  "amount": "250",
  "category": "Travel",
  "date": "2025-11-18"
}

5️⃣ Delete Expense

DELETE

/api/expenses/<id>

🧪 Example JSON Response
[
  {
    "id": 1,
    "title": "Groceries",
    "amount": "120.50",
    "category": "Food",
    "date": "Mon, 17 Nov 2025 00:00:00 GMT"
  }
]

🖥️ Frontend Files
index.html

Frontend UI for adding & viewing expenses.

style.css

Simple and clean styling.

script.js

Fetch API used to connect to backend.

🏁 Features Summary
Feature	Status
Add Expense	✔
View Expense	✔
Update Expense	✔
Delete Expense	✔
SQLite Database	✔
REST API	✔
Frontend UI	✔
🧩 How To Connect Frontend to Backend

Inside script.js:

const API_URL = "http://127.0.0.1:5000/api/expenses";


Make sure backend is running before opening the frontend.

📜 License

Free to Use • Open Source

👨‍💻 Author

Ashutosh Ardak
Python • Backend • DevOps Enthusiast
