import psycopg2
from config.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def connect_db(res):
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        res["dbt1"] = "Test successful"
        print("Database connection successful")
        return conn
    except psycopg2.OperationalError as e:
        res["front_end_dev"] = "Failed to connect to database: " + str(e)
        return None

def close_db(conn):
    if conn:
        conn.close()
        print("Database connection closed")
