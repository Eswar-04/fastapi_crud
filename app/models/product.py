from pydantic import BaseModel
class Product(BaseModel):# this class defines what a product should look like (validation)
    name: str # Product name
    price: float # Product price
    description: str # Product description
# description is optional