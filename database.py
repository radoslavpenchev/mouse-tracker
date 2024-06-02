import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mouse_data'")
        table_exists = self.cursor.fetchone()
        if not table_exists:
            self.cursor.execute("CREATE TABLE mouse_data (x INT, y INT, image_path TEXT)")
            self.connection.commit()

    def insert_data(self, x, y, image_path):
        self.cursor.execute("INSERT INTO mouse_data (x, y, image_path) VALUES (?, ?, ?)", (x, y, image_path))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
