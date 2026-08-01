from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API"
)


@app.get("/")
def home():
    return {"message": "Expense Tracker API"}


@app.post("/expenses", response_model=schemas.ExpenseResponse)
def create(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)


@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def all_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db)


@app.get("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def expense(expense_id: int, db: Session = Depends(get_db)):
    data = crud.get_expense_by_id(db, expense_id)

    if not data:
        raise HTTPException(status_code=404, detail="Expense Not Found")

    return data


@app.put("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def update(expense_id: int, expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    data = crud.update_expense(db, expense_id, expense)

    if not data:
        raise HTTPException(status_code=404, detail="Expense Not Found")

    return data


@app.patch("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def patch(expense_id: int, expense: schemas.ExpenseUpdate, db: Session = Depends(get_db)):
    data = crud.patch_expense(db, expense_id, expense)

    if not data:
        raise HTTPException(status_code=404, detail="Expense Not Found")

    return data


@app.delete("/expenses/{expense_id}")
def delete(expense_id: int, db: Session = Depends(get_db)):
    data = crud.delete_expense(db, expense_id)

    if not data:
        raise HTTPException(status_code=404, detail="Expense Not Found")

    return {"message": "Expense Deleted Successfully"}


@app.get("/category/{category}", response_model=list[schemas.ExpenseResponse])
def category(category: str, db: Session = Depends(get_db)):
    return crud.get_category(db, category)


@app.get("/total")
def total(db: Session = Depends(get_db)):
    return {
        "Total Expense": crud.total_expense(db)
    }


@app.get("/highest", response_model=schemas.ExpenseResponse)
def highest(db: Session = Depends(get_db)):
    data = crud.highest_expense(db)

    if not data:
        raise HTTPException(status_code=404, detail="No Expenses Found")

    return data