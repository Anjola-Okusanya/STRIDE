from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal

class ClientResponse(BaseModel):
    id: int
    full_name: str
    email: Optional[str] = None
    risk_profile: str
    target_equity_pct: int
    target_bond_pct: int
    target_cash_pct: int

    model_config = {"from_attributes": True}

class HoldingResponse(BaseModel):
    id: int
    ticker: str
    company_name: str
    asset_type: str
    quantity: Decimal
    avg_buy_price: Decimal
    current_price: float
    current_value: float
    gain_loss: float

    model_config = {"from_attributes": True}