from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
    title: str
    category: str
    amount: float
    payment_mode: str
    expense_date: date


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    amount: Optional[float] = None
    payment_mode: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseResponse(ExpenseCreate):
    expense_id: int

    class Config:
        from_attributes = True