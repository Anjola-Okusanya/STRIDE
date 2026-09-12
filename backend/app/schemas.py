from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClientResponse(BaseModel):
    id: int
    full_name: str
    email: Optional[str] = None
    risk_profile: str
    target_equity_pct: int
    target_bond_pct: int
    target_cash_pct: int

    model_config = {"from_attributes": True}