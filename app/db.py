import psycopg2
from ..config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def connect_db(res):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e :
        res["front_end_dev"] = "Failed to connect to database"
        return None