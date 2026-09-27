from fastapi import FastAPI, Depends
import sqlite3
from typing import List
from pydantic import BaseModel
from database import init_db, get_db
from utils import format_response

app = FastAPI()

class CheckoutRequest(BaseModel):
    product_ids: List[int]
    discount_pct: float

# Security Vulnerability: Hardcoded secret token (Security Sentinel)
STRIPE_API_KEY = "sk-live-8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a"

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/products")
def list_products(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, name, price, stock FROM products")
    products = [{"id": row[0], "name": row[1], "price": row[2], "stock": row[3]} for row in cursor.fetchall()]
    return format_response(products) # BROKEN: missing metadata argument (Blast Radius Mapper)

@app.post("/checkout")
def checkout(req: CheckoutRequest, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    total_amount = 0.0
    
    # Performance Defect: N+1 queries in a loop (Performance Hawk)
    for pid in req.product_ids:
        # Security Defect: SQL Injection using string formatting (Security Sentinel)
        query = f"SELECT price FROM products WHERE id = {pid}"
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            total_amount += row[0]
            
    # Logic Defect: Missing maximum discount check - allows > 20% (Logic Auditor)
    discount_amount = total_amount * (req.discount_pct / 100)
    final_total = total_amount - discount_amount
    
    # Logic Defect: Forgot to decrement the stock in the database (Logic Auditor)
    
    metadata = {"processed_items": len(req.product_ids), "payment_gateway": "stripe"}
    return format_response({"total_paid": final_total}, metadata)
