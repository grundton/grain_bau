# Tim-Tarek Grund for Etudes for live-electronics, 2023
# Combines use of VL53L0X ToF distance sensor and fader
# Sends values via OSC

import time
import board
import analogio
import touchio
import adafruit_CircuitPython_VL53L0X
import board
import busio

import usb_midi

import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

#set MIDI ports
print(usb_midi.ports)
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0],
                          in_channel=0,
                          midi_out=usb_midi.ports[1],
                          out_channel=0)

touch_pad = board.IO12 
touch = touchio.TouchIn(touch_pad)

i2c = busio.I2C(board.IO13, board.IO14) # SCL, then SDA
sensor = adafruit_CircuitPython_VL53L0X.VL53L0X(i2c)
sensor_value = sensor.range #in mms if im not mistaken

# Slide pot setup
fader = analogio.AnalogIn(board.IO2)
fader_position = fader.value  # ranges from 0-65535

# pitchwheel pot setup
pitchwheel = analogio.AnalogIn(board.IO5)
pitchwheel_position = pitchwheel.value  # ranges from 0-65535

# Set Osc client

host_ip = '10.0.0.7'
host_port = 9001
#client = udp_client.SimpleUDPClient(socketpool, host_ip, host_port)

current_side = "left"
last_side = "left"

NOTE_ON_DURATION = 3.5
LAST_NOTE_TIME = -1

pitch_array = [1]

while True:
    sensor_value = sensor.range
    fader_position = fader.value
    pitchwheel_position = pitchwheel.value
    #client.send_message('/distance', sensor_value)
    #client.send_message('/fader', fader.value)
    print(sensor_value, fader_position, pitchwheel_position, touch.raw_value)
    if fader_position > 62754/2:
        
        current_side = "right"
    else:
        current_side = "left"
        
    #if last_side == "left" and current_side == "right":
        #midi.send(NoteOff(pitch_array[0], 120))
        #pitch = int(-(sensor_value/1024) * 20 + 80)
        #pitch_array[0]= pitch
        #midi.send(NoteOn(pitch, 120))  # G sharp 2nd octave
        #time.sleep(0.5)
        # note how a list of messages can be used
        
        
    #time.sleep(0.001)
    
    last_side = current_side

 

