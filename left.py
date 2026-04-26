import time
import board
import pwmio
import adafruit_requests
from adafruit_motor import servo
    
pwm = pwmio.PWMOut(board.GP14, frequency=50)
pwm2 = pwmio.PWMOut(board.GP12, frequency=50)
pwm3 = pwmio.PWMOut(board.GP13, frequency=50)
pwm4 = pwmio.PWMOut(board.GP11, frequency=50)
pwm5 = pwmio.PWMOut(board.GP10, frequency=50)
pinky = servo.Servo(pwm3, min_pulse=500, max_pulse=2600)
ring = servo.Servo(pwm2, min_pulse=500, max_pulse=2600)
middle = servo.Servo(pwm, min_pulse=500, max_pulse=2500)
index = servo.Servo(pwm4, min_pulse=650, max_pulse=2600)
thumb = servo.Servo(pwm5, min_pulse=550, max_pulse=2600)
pinky_stop_angle = 100 # full down is pinky_stop_angle
ring_stop_angle = 100 # full down is 0
middle_stop_angle = 90 # full down is middle_stop_angle
index_stop_angle = 115 # full down is 0
thumb_stop_angle = 115 # full down is 0
slow_finger_speed = 0.05
normal_finger_speed = 0.01
fast_finger_speed = 0.001
finger_speed = normal_finger_speed

# def set_to_last_position(finger_positions):
#     pinky.angle = finger_positions['pinky']
#     ring.angle = finger_positions['ring']
#     middle.angle = finger_positions['middle']
#     index.angle = finger_positions['index']
#     thumb.angle = finger_positions['thumb']

# Countdown before finger movement
for x in range(3,0,-1):
    print(x)
    time.sleep(1)
    if x == 1:
        print('GO!!!')
        break
    
def get_finger_stop_angle(finger_stop_angle):
    if finger_stop_angle == 'pinky':
        return pinky_stop_angle
    elif finger_stop_angle == 'ring':
        return ring_stop_angle
    elif finger_stop_angle == 'middle':
        return middle_stop_angle
    elif finger_stop_angle == 'index':
        return index_stop_angle
    elif finger_stop_angle == 'thumb':
        return thumb_stop_angle
    
def get_finger_speed(finger_speed):
    if finger_speed == 'slow':
        return slow_finger_speed
    elif finger_speed == 'normal':
        return normal_finger_speed
    elif finger_speed == 'fast':
        return fast_finger_speed
    
def get_servo(finger):
    if finger == 'pinky':
        return pinky
    elif finger == 'ring':
        return ring
    elif finger == 'middle':
        return middle
    elif finger == 'index':
        return index
    elif finger == 'thumb':
        return thumb
    
def test_one_finger(finger, finger_speed_param):
    stop_angle = get_finger_stop_angle(finger)
    finger_speed = get_finger_speed(finger_speed_param)
    servo = get_servo(finger)
    try:
        if finger == 'pinky' or finger == 'middle':
            for angle in range(0, stop_angle, 1):
                servo.angle = angle
                print(str(finger) + " set to: " + str(angle))
                time.sleep(finger_speed)
            for angle in range(stop_angle, 0, -1):
                servo.angle = angle
                print(str(finger) + " set to: " + str(angle))
                time.sleep(finger_speed)
        else:
            for angle in range(stop_angle, 0, -1):
                servo.angle = angle
                print(str(finger) + " set to: " + str(angle))
                time.sleep(finger_speed)
            for angle in range(0, stop_angle, 1):
                servo.angle = angle
                print(str(finger) + " set to: " + str(angle))
                time.sleep(finger_speed)

    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(ring.angle))
        
def all_fingers_up(finger_speed_param):
    finger_speed = get_finger_speed(finger_speed_param)
    try:
        for angle in range(pinky_stop_angle, 0, -1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, ring_stop_angle, 1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(middle_stop_angle, 0, -1):
            middle.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, index_stop_angle, 1):
            index.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, thumb_stop_angle, 1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(pinky.angle))
    
def finger_wave(finger_speed_param):
    finger_speed = get_finger_speed(finger_speed_param)
    try:
        # All fingers down
        for angle in range(0, pinky_stop_angle, 1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(ring_stop_angle, 0, -1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, middle_stop_angle, 1):
            middle.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(index_stop_angle, 0, -1):
            index.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(thumb_stop_angle, 0, -1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
            
        # All fingers back up
        for angle in range(0, thumb_stop_angle, 1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, index_stop_angle, 1):
            index.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(middle_stop_angle, 0, -1):
            middle.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, ring_stop_angle, 1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(pinky_stop_angle, 0, -1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
            
    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(pinky.angle))
        
def fingers_peace_sign(finger_speed_param):
    finger_speed = get_finger_speed(finger_speed_param)
    try:
        # fingers down
        for angle in range(0, pinky_stop_angle, 1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(ring_stop_angle, 0, -1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(thumb_stop_angle, 0, -1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
            
        time.sleep(3)
        
        # fingers back up
        for angle in range(0, thumb_stop_angle, 1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, ring_stop_angle, 1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(pinky_stop_angle, 0, -1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)

    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(ring.angle))
        
def finger_fist(finger_speed_param):
    finger_speed = get_finger_speed(finger_speed_param)
    try:
        # All fingers down
        for angle in range(0, pinky_stop_angle, 1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(ring_stop_angle, 0, -1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, middle_stop_angle, 1):
            middle.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(index_stop_angle, 0, -1):
            index.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(thumb_stop_angle, 0, -1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
            
        time.sleep(3)
        
        # All fingers back up
        for angle in range(0, thumb_stop_angle, 1):
            thumb.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, index_stop_angle, 1):
            index.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(middle_stop_angle, 0, -1):
            middle.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(0, ring_stop_angle, 1):
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
        for angle in range(pinky_stop_angle, 0, -1):
            pinky.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)
            
    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(pinky.angle))
        
def fingers_down_a(finger_speed_param):
    finger_speed = get_finger_speed(finger_speed_param)
    try:
        # fingers down
        for angle in range(index_stop_angle, 0, -1):
            index.angle = angle
            thumb.angle = angle
            ring.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)

    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(ring.angle))
        
def fingers_down_b(finger_speed_param):
    finger_speed = get_finger_speed(finger_speed_param)
    try:
        # fingers down
        for angle in range(0, pinky_stop_angle, 1):
            pinky.angle = angle
            middle.angle = angle
            print("set to: " + str(angle))
            time.sleep(finger_speed)

    except KeyboardInterrupt:
        print('Gotcha!!!' + ' Stop Angle: ' + str(ring.angle))
    
# Fingers: pinky, ring, middle, index, thumb
# Finger speeds: slow, normal, fast
all_fingers_up('fast')
#finger_fist('normal')
finger_wave('fast')
print("Off")