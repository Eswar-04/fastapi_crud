from fastapi import APIRouter, HTTPException # FastAPI classes for routing and error handling
from app.models.product import Product # Our product model for validation
from app.utils.database import collection # MongoDB collection imported from utils
from bson import ObjectId # To work with MongoDB's default ID format

router = APIRouter()# Create a router object to group all product-related API routes

# CREATE a new product
@router.post("/product")
def create_product(product: Product):
    try:
        result = collection.insert_one(product.dict()) # Convert product model to dictionary and insert into MongoDB

        return {"id": str(result.inserted_id)}# Return the ID of the newly created product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating product: {str(e)}")# If something goes wrong, return a 500 error

# READ - Get all products
@router.get("/products")
def get_all_products():
    try:
        products = []
        for product in collection.find():# Loop through all documents in the collection

            product["_id"] = str(product["_id"])# Convert MongoDB ObjectId to string so it’s JSON convertible
            products.append(product)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving products: {str(e)}")

# READ - Get a single product by its ID
@router.get("/product/{product_id}")
def get_product(product_id: str):
    try:
        product = collection.find_one({"_id": ObjectId(product_id)})# Try to find the product by its ID in MongoDB
        if product:
            product["_id"] = str(product["_id"])# Convert ObjectId to string
            return product
       
        raise HTTPException(status_code=404, detail="Product not found") # If product not found, return 404 error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving product: {str(e)}")

# UPDATE an existing product by ID
@router.put("/product/{product_id}")
def update_product(product_id: str, updated_product: Product):
    try:
        # Update the matching product with new data
        result = collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": updated_product.dict()}
        )
        if result.modified_count == 1:
            return {"message": "Product updated successfully"}
        raise HTTPException(status_code=404, detail="Product not found or not modified")# Product not found or nothing was changed
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating product: {str(e)}")

# DELETE a product by ID
@router.delete("/product/{product_id}")
def delete_product(product_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(product_id)}) # Try to delete the product with given ID
        if result.deleted_count == 1:
            return {"message": "Product deleted successfully"}
        raise HTTPException(status_code=404, detail="Product not found")# If product doesn't exist
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting product: {str(e)}")
