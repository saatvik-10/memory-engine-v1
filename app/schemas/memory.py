from pydantic import BaseModel

class MemoryCreate(BaseModel):
    memory: str
    type: str
    
class MemoryResponse(BaseModel):
    id: int
    memory: str
    type: str