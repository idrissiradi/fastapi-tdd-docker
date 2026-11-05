from pydantic import BaseModel


class SummaryPayLoadSchema(BaseModel):
    url: str
