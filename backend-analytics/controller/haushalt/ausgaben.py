from fastapi import APIRouter

router = APIRouter()

@router.get("/ausgaben")
async def get_ausgaben():
    """
    Returns a list of all expenditures (mock data).
    """
    mock_ausgaben = [
        {"id": "a1", "description": "Rent", "amount": 1200.00, "category": "Housing"},
        {"id": "a2", "description": "Groceries", "amount": 350.50, "category": "Food"},
        {"id": "a3", "description": "Internet", "amount": 50.00, "category": "Utilities"},
        {"id": "a4", "description": "Electricity", "amount": 75.20, "category": "Utilities"},
        {"id": "a5", "description": "Transportation", "amount": 120.00, "category": "Transport"},
    ]
    return {"ausgaben": mock_ausgaben}
