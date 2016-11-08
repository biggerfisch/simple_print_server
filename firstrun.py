#!/usr/bin/env python
import os

from config import DATABASE_PATH
from simple_print_server.database import init_db

def create_db_if_not_created():
    if not os.path.exists(DATABASE_PATH):
        print("Creating database")
        init_db()
    else:
        print("Database already exists, nothing to do")

if __name__ == "__main__":
    create_db_if_not_created()
