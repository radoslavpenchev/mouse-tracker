Mouse Tracker Application

The Mouse Tracker Application is a Python application that tracks the movement of the mouse cursor and captures images from a connected webcam when the left mouse button is pressed. The application uses parallel processes to handle multiple tasks concurrently. It utilizes a web server and websockets for real-time visualization of mouse cursor movement and image capture events in a browser environment. The data collected, including mouse cursor coordinates and image data, is stored in a SQLite database.
Features

    Real-time tracking of mouse cursor movement
    Capture images from a connected webcam when the left mouse button is pressed
    Web-based visualization of mouse cursor movement
    Storage of mouse cursor coordinates and image data in a SQLite database

Installation

    Clone the repository:

    terminal

git clone https://github.com/radoslavpenchev/mouse-tracker.git
cd mouse-tracker

Install the required dependencies:

terminal

pip install -r requirements.txt

Run the application:

terminal

    python app.py

Usage

Once the application is running, you can access the web interface by opening a browser and navigating to http://localhost:5000. Mouse cursor movements will be displayed in real-time on the web interface. Pressing the left mouse button will trigger image capture events from the webcam.
Configuration
