from pydantic import BaseModel, Field, conint, condecimal
from typing import Optional
from uuid import UUID

Preco = condecimal(max_digits=10, decimal_places=2)

class ProductBase(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    preco: Preco
    estoque: conint(ge=0)
    descricao: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=1, max_length=100)
    preco: Optional[Preco] = None
    estoque: Optional[conint(ge=0)] = None
    descricao: Optional[str] = None

class ProductResponse(ProductBase):
    id: int
    user_id: UUID

    class Config:
        from_atributes = True
