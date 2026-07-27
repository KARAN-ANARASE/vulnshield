import sqlite3
import hashlib
import os

class UserModel:
    def __init__(self, db_path='vuln.db'):
        self.db_path = db_path
        # SAST: Hardcoded credentials
        self.admin_pass = "Admin@12345"
        
    def get_user(self, username):
        # SAST: SQL Injection
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        return cursor.fetchone()

    def hash_password(self, password):
        # SAST: Weak Cryptography (MD5)
        return hashlib.md5(password.encode()).hexdigest()

    def insecure_token(self):
        # SAST: Insecure Random Number Generation
        import random
        return str(random.random())
