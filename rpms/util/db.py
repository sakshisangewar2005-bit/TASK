import mysql.connector
from config import DB_CONFIG

def get_connection():
    """Create a new MySQL connection. Update config.py before running."""
    return mysql.connector.connect(**DB_CONFIG)
