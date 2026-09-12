def calculate_drift(holdings, client):
    equity_total = 0
    bond_total = 0
    cash_total = 0

    for holding in holdings:
        if holding.asset_type == "equity":
            equity_total += holding.current_value
        elif holding.asset_type == "bond":
            bond_total += holding.current_value
        elif holding.asset_type == "cash":
            cash_total += holding.current_value

    portfolio_total = equity_total + bond_total + cash_total

    if portfolio_total == 0:
        return {}

    equity_pct = equity_total / portfolio_total * 100
    bond_pct = bond_total / portfolio_total * 100
    cash_pct = cash_total / portfolio_total * 100

    equity_drift = equity_pct - client.target_equity_pct
    bond_drift = bond_pct - client.target_bond_pct
    cash_drift = cash_pct - client.target_cash_pct

    return {
        "equity": {"actual": round(equity_pct, 1), "target": client.target_equity_pct, "drift": round(equity_drift, 1), "alert": abs(equity_drift) > 5},
        "bond":   {"actual": round(bond_pct, 1),   "target": client.target_bond_pct,   "drift": round(bond_drift, 1),   "alert": abs(bond_drift) > 5},
        "cash":   {"actual": round(cash_pct, 1),   "target": client.target_cash_pct,   "drift": round(cash_drift, 1),   "alert": abs(cash_drift) > 5},
    }