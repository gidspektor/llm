from pydantic import BaseModel, constr

class SummaryResponse(BaseModel):
    summary: str
