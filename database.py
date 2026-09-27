import sqlite3

def init_db():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    
    # Insert some dummy data if empty
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO products (name, price, stock) VALUES ('Laptop', 1000.0, 10)")
        cursor.execute("INSERT INTO products (name, price, stock) VALUES ('Mouse', 25.0, 50)")
        cursor.execute("INSERT INTO products (name, price, stock) VALUES ('Keyboard', 50.0, 30)")
    
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect("ecommerce.db")
    try:
        yield conn
    finally:
        conn.close()
