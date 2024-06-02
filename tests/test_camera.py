import unittest
from unittest.mock import MagicMock, patch
from camera import Camera

class TestCamera(unittest.TestCase):
    @patch('camera.cv2.VideoCapture')
    @patch('camera.cv2.imwrite')
    def test_capture_image(self, mock_imwrite, mock_video_capture):
        mock_capture = MagicMock()
        mock_capture.read.return_value = (True, None)
        
        mock_video_capture.return_value = mock_capture
        
        camera = Camera()
        image_path = camera.capture_image()
        
        self.assertIsNotNone(image_path) 
        mock_imwrite.assert_called_once()
