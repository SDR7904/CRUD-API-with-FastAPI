# 💰 Expense Management API (FastAPI, In-Memory)

A simple **Expense Management REST API** built using **FastAPI**.
This project uses an **in-memory dictionary** instead of a database to store expenses.
It demonstrates how to perform basic **CRUD operations** in FastAPI.

---

## 🚀 Features

* 🧾 Create, Read, Update, and Delete (CRUD) operations for expenses
* 💾 Uses in-memory storage (no external database required)
* ⚡ Built with FastAPI for high performance and automatic documentation
* 📘 Includes Swagger and ReDoc API docs

---

## 📦 Project Structure

```
./
│
├── main.py          # Main FastAPI application
└── README.md        # Project documentation
```

---

## 🧠 Data Model

Each expense has the following fields:

| Field         | Type    | Description                      |
| ------------- | ------- | -------------------------------- |
| `id`          | `int`   | Unique ID assigned automatically |
| `description` | `str`   | Description of the expense       |
| `amount`      | `float` | Amount of the expense            |

---

## 🔧 Installation & Running

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SDR7904/CRUD-API-with-FastAPI.git
cd expense-api
```

### 2️⃣ (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn
```

### 4️⃣ Run the server

```bash
uvicorn main:app --reload
```

### 5️⃣ Open API documentation

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🌐 API Endpoints

| Method   | Endpoint         | Description                | Status Code                      |
| -------- | ---------------- | -------------------------- | -------------------------------- |
| `POST`   | `/expenses`      | Create a new expense       | `201 Created`                    |
| `GET`    | `/expenses`      | Retrieve all expenses      | `200 OK`                         |
| `GET`    | `/expenses/{id}` | Retrieve an expense by ID  | `200 OK / 404 Not Found`         |
| `PUT`    | `/expenses/{id}` | Update an existing expense | `200 OK / 404 Not Found`         |
| `DELETE` | `/expenses/{id}` | Delete an expense          | `204 No Content / 404 Not Found` |

---

## 🧩 Example JSON

### ➕ Create Expense (POST `/expenses`)

```json
{
  "description": "Coffee and snacks",
  "amount": 12.5
}
```

### 🔄 Update Expense (PUT `/expenses/1`)

```json
{
  "description": "Groceries",
  "amount": 45.9
}
```

### ✅ Response Example

```json
{
  "id": 1,
  "description": "Groceries",
  "amount": 45.9
}
```

---

## ⚙️ Technical Notes

* Data is **not persistent** — all expenses are lost when the server restarts.
* Each expense is stored in a **Python dictionary** in memory.
* The project is ideal for **learning FastAPI basics** or testing REST endpoints.
---
