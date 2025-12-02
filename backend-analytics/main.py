from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import pandas as pd

app = FastAPI()

# Define data model
class TelemetryData(BaseModel):
    vehicle_id: str
    temperature: float
    speed: float
    timestamp: Optional[datetime] = None

class AnalyticsResult(BaseModel):
    status: str
    total_analyzed: int
    issues: List[dict] = []
    timestamp: str

# Settings
CRITICAL_TEMPERATURE = 110  # Example threshold
SPEED_LIMIT = 180  # Example speed limit

@app.post("/analyze", response_model=AnalyticsResult)
async def analyze_telemetry(data: List[TelemetryData]):
    try:
        # Convert incoming data to DataFrame
        data_dicts = [item.model_dump() for item in data] # Pydantic to dict
        # load all in table storage
        df = pd.DataFrame(data_dicts)

        # analyse with pandas it is easier and faster 

        # filter
        critical_df = df[
            (df['temperature'] > CRITICAL_TEMPERATURE) |
            (df['speed'] > SPEED_LIMIT)
        ]

        # Prepare issues list
        issues = []

        if not critical_df.empty:
            # add error_type column
            critical_df.loc[critical_df['temperature'] > CRITICAL_TEMPERATURE, 'error_type'] = 'High Temperature'
            critical_df.loc[critical_df['speed'] > SPEED_LIMIT, 'error_type'] = 'Over Speeding'

            # Convert to list of dicts
            issues = critical_df.to_dict(orient='records')

        status = "Warning" if not critical_df.empty else "OK"

        result = AnalyticsResult(
            status=status,
            total_analyzed=len(df),
            issues=issues,
            timestamp=datetime.now().isoformat()
        )

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=6000, reload=True)
    

