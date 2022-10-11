from typing import Optional
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    code: int = Field(gt=0)
    name: str = Field(max_length=100, min_length=2)
    size: Optional[str] = Field(max_length=4)
    description: str = Field(max_length=200, min_length=5)
    price: Optional[float] = Field(gt=0.01)
    image: Optional[str]
    type: Optional[str]
    category: Optional[str]
    trademark: Optional[str]
    color: Optional[str]
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
    