from typing import Optional
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    code: int 
    name: str = Field(max_length=100)
    size: str = Field(max_length=4)
    description: str = Field(max_length=200)
    price: float
    image: str
    type: str
    category: str
    trademark: str
    color: str 
class ProductUpdatedSchema(BaseModel):
    name: Optional[str]
    size: Optional[str]
    description: Optional[str]
    price: Optional[float]
    image: Optional[str]
    type: Optional[str]
    category: Optional[str]
    trademark: Optional[str]
    color: Optional[str]
    