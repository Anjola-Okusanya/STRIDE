from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Client
from ..schemas import ClientResponse
from ..models import Client, Holding, Portfolio
from ..schemas import ClientResponse, HoldingResponse
from ..services.alpha_vantage import get_live_price

router = APIRouter()

@router.get("/clients/", response_model=List[ClientResponse])
def get_clients(db: Session = Depends(get_db)):
    clients = db.query(Client).all()
    return clients

@router.get("/clients/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    return client

@router.get("/clients/{client_id}/holdings",
            response_model=List[HoldingResponse])
def get_holdings(client_id: int, db: Session = Depends(get_db)):
    portfolio = db.query(Portfolio)\
                  .filter(Portfolio.client_id == client_id)\
                  .first()
    holdings = db.query(Holding)\
                 .filter(Holding.portfolio_id == portfolio.id)\
                 .all()
    
    result = []
    for holding in holdings:
        current_price = get_live_price(holding.ticker)
        current_value = float(holding.quantity) * current_price
        gain_loss = current_value - (float(holding.quantity) * float(holding.avg_buy_price))
        
        result.append({
            "id": holding.id,
            "ticker": holding.ticker,
            "company_name": holding.company_name,
            "asset_type": holding.asset_type,
            "quantity": holding.quantity,
            "avg_buy_price": holding.avg_buy_price,
            "current_price": current_price,
            "current_value": current_value,
            "gain_loss": gain_loss
        })
    
    return result