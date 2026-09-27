from fastapi import FastAPI, Depends
import sqlite3
from database import init_db, get_db
from utils import format_response

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/products")
def list_products(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT id, name, price, stock FROM products")
    products = [{"id": row[0], "name": row[1], "price": row[2], "stock": row[3]} for row in cursor.fetchall()]
    return format_response(products)
