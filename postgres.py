import logging
import psycopg2
import psycopg2.extras
import psycopg2.errors
from config import DB_URL

conn = psycopg2.connect(DB_URL, sslmode='require')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def create_tables():
    pass


def close():
    cur.close()
    conn.close()
