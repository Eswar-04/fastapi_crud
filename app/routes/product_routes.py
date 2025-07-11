from fastapi import APIRouter
from app.models.product import Product
from app.utils.database import collection
router = APIRouter()

@router.post("/product")
def create_product(product: Product):
    result = collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products")
def get_all_products():
    products = []
    for product in collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
        return products
    
from bson import ObjectId
from fastapi import HTTPException

@router.get("/product/{product_id}")
def get_product(product_id: str):
    product = collection.find_one({"_id": ObjectId(product_id)})
    if product:
        product["_id"] = str(product["_id"])
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/product/{product_id}")
def update_product(product_id: str, updated_product: Product):
    result = collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": updated_product.dict()}
    )
    
    if result.modified_count == 1:
        return {"message": "Product updated successfully"}
    
    raise HTTPException(status_code=404, detail="Product not found or not modified")

@router.delete("/product/{product_id}")
def delete_product(product_id: str):
    result = collection.delete_one({"_id": ObjectId(product_id)})
    
    if result.deleted_count == 1:
        return {"message": "Product deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Product not found")
