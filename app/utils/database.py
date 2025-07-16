from pymongo import MongoClient # MongoDB connector
from dotenv import load_dotenv # To load values from .env file
import os # Load environment variables from .env file

load_dotenv()
try:
    MONGO_URL = os.getenv("MONGO_URL") # Get MongoDB connection string from .env
    client = MongoClient(MONGO_URL) # Connect to MongoDB using the URL
    db = client["productdb"]# Use database named 'productdb'
    collection = db["products"] # Use collection (like table) named 'products'

except Exception as e:
    print("MongoDB connection failed:", str(e))# If anything fails during connection, print error and stop
    raise e

