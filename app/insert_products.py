from app.supabase_client import supabase

# List of products to insert
products = [
    {
        "name": "T-Shirt",
        "price": 500,
        "description": "Cotton printed round neck shirt"
    },
    {
        "name": "Sneakers",
        "price": 1000,
        "description": "White running shoes"
    },
    {
        "name": "Sunglasses",
        "price": 300,
        "description": "UV-protected eyewear"
    }
]

# Insert all products
response = supabase.table("products").insert(products).execute()
print(response)
