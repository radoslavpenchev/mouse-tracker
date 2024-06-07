import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS mouse_data (
                               x INTEGER,
                               y INTEGER,
                               image_path TEXT)''')
        self.connection.commit()

    def insert_data(self, x, y, image_path):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mouse_data (x, y, image_path) VALUES (?, ?, ?)", (x, y, image_path))
        conn.commit()
        cursor.close()
        conn.close()
