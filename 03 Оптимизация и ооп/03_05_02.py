import sqlite3
from tkinter import INSERT

DB_CREDS = {"database": "example.db"}

class DBAccessor:
    def __init__(self, db_creds: dict):
        self.__db_creds = db_creds
        self.__connection = None # если будет - лучш еобъявить сразу
        self.__cursor = None

    def __enter__(self):
        if self.__connection is None:
            self.__connection = sqlite3.connect(**self.__db_creds)
        self.__cursor = self.__connection.cursor()
        return self.__cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.commit()
        self.__connection.close()
        print("Connection was closed")

def main():
    with DBAccessor(DB_CREDS) as cursor:
        for row in cursor.execute("SELECT * FROM user"):
            print(row)
        # cursor.execute("CREATE TABLE user (personid int, username varchar(255))")
        # cursor.execute("INSERT INTO user (personid, username) VALUES (1, 'mike')")
        # cursor.execute("INSERT INTO user (personid, username) VALUES (2, 'kate')")
        # cursor.execute("INSERT INTO user (personid, username) VALUES (3, 'ann')")

    print("111")


if __name__ == "__main__":
    main()