import socket
import time

# Replace with the actual IP address of the Pico W
UDP_IP = "192.168.0.50" 
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_command(command):
    sock.sendto(command.encode('utf-8'), (UDP_IP, UDP_PORT))
    print(f"Sent telemetry payload: '{command}'")

if __name__ == "__main__":
    send_command("peace")
    time.sleep(3)
    send_command("finger_wave")