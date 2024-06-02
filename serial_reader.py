import threading
import serial

class SerialReader:
    def __init__(self, port, baud_rate):
        try:
            self.ser = serial.Serial(port, baud_rate, timeout=1)
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return
        
        self.running = True
        self.thread = threading.Thread(target=self.read_serial)
        self.thread.daemon = True
        self.thread.start()

    def read_serial(self):
        while self.running:
            if self.ser.in_waiting > 0:
                try:
                    line = self.ser.readline().decode('utf-8').rstrip()
                    print(line)
                except serial.SerialException as e:
                    print(f"Error reading from serial port: {e}")
                    self.running = False

    def stop(self):
        self.running = False
        if self.thread.is_alive():
            self.thread.join()
        self.ser.close()