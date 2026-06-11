from pydantic import BaseModel


class SearchReq(BaseModel):
    query: str
    top_k: int = 3
