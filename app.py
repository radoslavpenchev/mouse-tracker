from flask import Flask, render_template
from flask_socketio import SocketIO
from camera import Camera
from database import Database
from serial_reader import SerialReader

class MouseTrackerApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)
        self.db = Database('database.db')
        self.camera = Camera()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.socketio.on('mouse_move')
        def handle_mouse_move(data):
            x = data['x']
            y = data['y']
            print(f"Mouse moved to ({x}, {y})")
            self.socketio.emit('update_mouse_position', {'x': x, 'y': y})

        @self.socketio.on('mouse_click')
        def handle_mouse_click(data):
            x = data['x']
            y = data['y']
            print(f"Mouse clicked at ({x}, {y})")
            image_path = self.camera.capture_image()
            if image_path:
                self.db.insert_data(x, y, image_path)
                self.socketio.emit('image_captured', {'x': x, 'y': y, 'image_path': image_path})
            self.socketio.emit('update_click_position', {'x': x, 'y': y})

    def run(self):
        self.socketio.run(self.app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app = MouseTrackerApp()
    app.run()

