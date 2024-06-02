import unittest
from unittest.mock import patch, MagicMock
from database import Database

class TestDatabase(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_insert_data(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        db = Database('test.db')
        db.insert_data(10, 20, 'test_image.jpg')

        mock_cursor.execute.assert_any_call("SELECT name FROM sqlite_master WHERE type='table' AND name='mouse_data'")
        mock_cursor.execute.assert_any_call("INSERT INTO mouse_data (x, y, image_path) VALUES (?, ?, ?)", (10, 20, 'test_image.jpg'))
