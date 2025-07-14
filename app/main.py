from fastapi import FastAPI
from app.routes.product_routes import router
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI instance
app = FastAPI()
# Include all product-related routes into the main app
app.include_router(router)

