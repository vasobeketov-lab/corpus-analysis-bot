import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite version: {sqlite3.version}")
        except Error as e:
            print(e)

    def close_connection(self):
        """ close database connection """
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def create_table(self, table_creation_sql):
        """ create a table from the create_table_sql statement """
        try:
            c = self.conn.cursor()
            c.execute(table_creation_sql)
        except Error as e:
            print(e)

    def insert_analysis(self, analysis_data):
        """ insert a new analysis into the analyses table """
        sql = ''' INSERT INTO analyses(user_id, analysis_result)
                  VALUES(?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, analysis_data)
        self.conn.commit()
        return cur.lastrowid

    def insert_user(self, user_data):
        """ insert a new user into the users table """
        sql = ''' INSERT INTO users(username, email)
                  VALUES(?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, user_data)
        self.conn.commit()
        return cur.lastrowid

    # ... Additional methods for managing records, updates, deletes, and queries
