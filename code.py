import time
import wifi
import wifi_connect
import left 

# Initialize modular network pool
pool = wifi_connect.connect()

# Setup UDP Server Parameters
HOST = str(wifi.radio.ipv4_address)
PORT = 5005

sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
sock.bind((HOST, PORT))
sock.settimeout(0) # CRITICAL: Non-blocking mode for mechanical loops

print(f"Robotic hand (PicoW) listening for UDP payloads on {HOST}:{PORT}")

while True:
    try:
        buf = bytearray(256)
        size, addr = sock.recvfrom_into(buf)
        
        payload = buf[:size].decode('utf-8').strip()
        print(f"Telemetry received from {addr}: {payload}")
        
        # --- Kinematics Mapping ---
        if payload == "fist":
            left.finger_fist('fast') 
            print("Actuating: Fist")
        elif payload == "peace":
            fingers_peace_sign('normal') 
            print("Actuating: Peace Sign")
        elif payload == "finger_wave":
            left.finger_wave('slow')
            print("Actuating: Finger Wave")
            
    except OSError as e:
        if e.errno == 11: # Buffer empty
            pass
        else:
            print(f"Socket Error: {e}")
            
    time.sleep(0.01) # Yield core time to prevent lockup