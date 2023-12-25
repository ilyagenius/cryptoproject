from pydantic import BaseModel
from datetime import datetime

class CurrencyRatePayload(BaseModel):
    pair: str
    price: float
    timestamp: datetime
