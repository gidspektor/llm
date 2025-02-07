from pydantic import BaseModel, constr

from typing import Optional


class SummaryRequest(BaseModel):
	text: constr(max_length=1000)
	max_length: Optional[Optional[int]]


class SummaryResponse(BaseModel):
    summary: str
