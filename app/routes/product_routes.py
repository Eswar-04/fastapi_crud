from fastapi import APIRouter, HTTPException  # Import FastAPI router and HTTP exception handling
from pydantic import BaseModel  # For defining data models with validation
from app.supabase_client import supabase  # Importing the Supabase client from the app module

router = APIRouter()  # Initializing API router for modular routing

# Pydantic model for Product input validation
class Product(BaseModel):
    name: str           # Name of the product (required)
    price: float        # Price of the product (required)
    description: str    # Short description (required)

# ▶ POST - Add a new product to the database
@router.post("/product")
def create_product(product: Product):
    try:
        response = supabase.table("products").insert(product.dict()).execute()  # Insert product into 'products' table
        return {"message": "Product added", "data": response.data}  # Return success message with inserted data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Return 500 if something goes wrong

# ▶ GET - Fetch all products from the database
@router.get("/products")
def get_products():
    try:
        response = supabase.table("products").select("*").execute()  # Select all rows from 'products' table
        print("Supabase response:", response)  # Debug print in terminal to check data
        return response.data  # Return all product data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Return 500 on error

# ▶ GET - Get a specific product by ID
@router.get("/product/{product_id}")
def get_product(product_id: int):
    try:
        response = supabase.table("products").select("*").eq("id", product_id).execute()  # Fetch product by ID
        if response.data:  # If data exists, return it
            return response.data[0]  # Return first matching product
        raise HTTPException(status_code=404, detail="Product not found")  # Return 404 if not found
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Return 500 on error

# ▶ PUT - Update product info by ID
@router.put("/product/{product_id}")
def update_product(product_id: int, product: Product):
    try:
        response = supabase.table("products").update(product.dict()).eq("id", product_id).execute()  # Update matching product
        return {"message": "Product updated", "data": response.data}  # Return updated data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Return 500 on error

# ▶ DELETE - Remove a product by ID
@router.delete("/product/{product_id}")
def delete_product(product_id: int):
    try:
        response = supabase.table("products").delete().eq("id", product_id).execute()  # Delete product with matching ID
        return {"message": "Product deleted"}  # Return confirmation message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Return 500 on error
