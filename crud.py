from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Expense
from schemas import ExpenseCreate, ExpenseUpdate


def create_expense(db: Session, expense: ExpenseCreate):
    new_expense = Expense(**expense.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def get_all_expenses(db: Session):
    return db.query(Expense).all()


def get_expense_by_id(db: Session, expense_id: int):
    return db.query(Expense).filter(
        Expense.expense_id == expense_id
    ).first()


def update_expense(db: Session, expense_id: int, expense: ExpenseCreate):
    db_expense = get_expense_by_id(db, expense_id)

    if db_expense:
        db_expense.title = expense.title
        db_expense.category = expense.category
        db_expense.amount = expense.amount
        db_expense.payment_mode = expense.payment_mode
        db_expense.expense_date = expense.expense_date

        db.commit()
        db.refresh(db_expense)

    return db_expense


def patch_expense(db: Session, expense_id: int, expense: ExpenseUpdate):
    db_expense = get_expense_by_id(db, expense_id)

    if db_expense:
        update_data = expense.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_expense, key, value)

        db.commit()
        db.refresh(db_expense)

    return db_expense


def delete_expense(db: Session, expense_id: int):
    db_expense = get_expense_by_id(db, expense_id)

    if db_expense:
        db.delete(db_expense)
        db.commit()

    return db_expense


def get_category(db: Session, category: str):
    return db.query(Expense).filter(
        Expense.category == category
    ).all()


def total_expense(db: Session):
    return db.query(func.sum(Expense.amount)).scalar()


def highest_expense(db: Session):
    return db.query(Expense).order_by(
        Expense.amount.desc()
    ).first()