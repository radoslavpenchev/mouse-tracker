import unittest
from unittest.mock import MagicMock, patch
from serial_reader import SerialReader

class TestSerialReader(unittest.TestCase):
    @patch('serial.Serial')
    def test_read_serial(self, mock_serial_class):
        mock_serial = MagicMock()
        mock_serial.in_waiting = 1
        mock_serial.readline.return_value = b'Test data\r\n'
        mock_serial_class.return_value = mock_serial
        
        reader = SerialReader('/dev/ttyS1', 9600)

        reader.read_serial()

        mock_serial.readline.assert_called_once()
        self.assertEqual(reader.ser.readline(), b'Test data\r\n')
        
        reader.stop_reading()
        reader.thread.join()
