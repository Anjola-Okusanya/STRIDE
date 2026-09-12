from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class Manager(Base):
    __tablename__ = "managers"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String)
    risk_profile = Column(String, nullable=False)
    target_equity_pct = Column(Integer, nullable=False)
    target_bond_pct = Column(Integer, nullable=False)
    target_cash_pct = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class Holding(Base):
    __tablename__ = "holdings"

    id = Column(Integer, primary_key=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"), nullable=False)
    ticker = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)
    quantity = Column(Numeric, nullable=False)
    avg_buy_price = Column(Numeric, nullable=False)
    created_at = Column(DateTime, server_default=func.now())