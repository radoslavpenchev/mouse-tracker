from flask import Flask, render_template
from flask_socketio import SocketIO
from camera import Camera
from database import Database
from serial_reader import SerialReader
from pynput import mouse

class MouseTrackerApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)
        self.db = Database('database.db')
        self.camera = Camera()
        self.setup_routes()

        self.listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click
        )
        self.listener.start()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

    def on_move(self, x, y):
        print(f"Mouse moved to ({x}, {y})")

    def on_click(self, x, y, button, pressed):
        if pressed:
            image_path = self.camera.capture_image()
            if image_path:
                self.db.insert_data(x, y, image_path)
                self.socketio.emit('image_captured', {'x': x, 'y': y, 'image_path': image_path})

    def run(self):
        self.socketio.run(self.app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app = MouseTrackerApp()
    app.run()
