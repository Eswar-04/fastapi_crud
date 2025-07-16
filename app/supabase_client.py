import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()  # ← adhoda load pannuthu

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("URL:", SUPABASE_URL)
print("KEY:", SUPABASE_KEY)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", SUPABASE_KEY)
