from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    payment_mode = Column(String(30), nullable=False)
    expense_date = Column(Date, nullable=False)