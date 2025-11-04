from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Expense Management API")

# Data model for expenses
class Expense(BaseModel):
    id: int
    description: str
    amount: float

class ExpenseCreate(BaseModel):
    description: str
    amount: float

# In-memory storage
expenses: Dict[int, Expense] = {}
current_id = 0


@app.post("/expenses", response_model=Expense, status_code=201)
def create_expense(expense: ExpenseCreate):
    """
    Create a new expense with a unique ID
    """
    global current_id
    current_id += 1
    new_expense = Expense(id=current_id, **expense.dict())
    expenses[current_id] = new_expense
    return new_expense


@app.get("/expenses", response_model=list[Expense])
def get_all_expenses():
    """
    Retrieve all expenses
    """
    return list(expenses.values())


@app.get("/expenses/{expense_id}", response_model=Expense)
def get_expense(expense_id: int):
    """
    Retrieve a specific expense by ID
    """
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expenses[expense_id]


@app.put("/expenses/{expense_id}", response_model=Expense)
def update_expense(expense_id: int, updated_expense: ExpenseCreate):
    """
    Update a specific expense by ID
    """
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")

    expenses[expense_id].description = updated_expense.description
    expenses[expense_id].amount = updated_expense.amount
    return expenses[expense_id]


@app.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: int):
    """
    Delete a specific expense by ID
    """
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")

    del expenses[expense_id]
    return