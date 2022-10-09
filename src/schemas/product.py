from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    name: str = Field(max_length=100)
    size: str = Field(max_length=3)
    decription: str
    price: float
    type: str
    category: str
    trademark: str
    color: str