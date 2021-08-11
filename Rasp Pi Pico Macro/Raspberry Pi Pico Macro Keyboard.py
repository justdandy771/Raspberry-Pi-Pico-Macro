import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


"""Each of these can be renamed to what you would like to use
   Based on research I've done GPIO pin 15 acts up sometimes, feel free to use that pin if you find no issues
"""
button1 = board.GP1       
button2 = board.GP2
button3 = board.GP3
button4 = board.GP4
button5 = board.GP5
button6 = board.GP6
button7 = board.GP7
button8 = board.GP8
button9 = board.GP9
button10 = board.GP10
button11 = board.GP11
button12 = board.GP12
button13 = board.GP13
button14 = board.GP14
button16 = board.GP16
button17 = board.GP17
button18 = board.GP18
button19 = board.GP19
button20 = board.GP20
button21 = board.GP21
button22 = board.GP22

"""
Initializing Buttons

Since this is a keyboard emulating script the buttons are all inputs
Call in the button with digitalio.DigitalInOut() with each of the above buttons
Next determine the direction of the button, in this case its an input
Finally setting the intial state to UP or Down
"""
button_16 = digitalio.DigitalInOut(button16)
button_16.direction = digitalio.Direction.INPUT
button_16.pull = digitalio.Pull.DOWN


button_17 = digitalio.DigitalInOut(button17)
button_17.direction = digitalio.Direction.INPUT
button_17.pull = digitalio.Pull.DOWN


button_18 = digitalio.DigitalInOut(button18)
button_18.direction = digitalio.Direction.INPUT
button_18.pull = digitalio.Pull.DOWN


button_19 = digitalio.DigitalInOut(button19)
button_19.direction = digitalio.Direction.INPUT
button_19.pull = digitalio.Pull.DOWN


button_20 = digitalio.DigitalInOut(button20)
button_20.direction = digitalio.Direction.INPUT
button_20.pull = digitalio.Pull.DOWN

button_16_bool = False
button_17_bool = False
button_18_bool = False
button_19_bool = False
button_20_bool = False


"""
For the main program you can choose between the following:
Printing out text with layout.write()
Sending Macro shortcuts using keyboard.press()

All keyboard mappings can be found at
"https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html"
"""


while True:
	# Check if button is pressed and if it is, to press the Macros and toggle LED
    if button_16.value:  
        layout.write('Example Text')
        time.sleep(0.15)
        button_16_bool = not button_16_bool

    if button_17.value:
        layout.write('Example Text')
        time.sleep(0.15)
        button_17_bool = not button_17_bool
        
    if button_18.value:  
        layout.write('Example Text')
        time.sleep(0.15)
        button_18_bool = not button_18_bool

    if button_19.value:
        layout.write('Example Text')
        time.sleep(0.15)
        button_19_bool = not button_19_bool

    if button_20.value:
	keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        time.sleep(0.15)
        keyboard.release(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
        button_20_bool = not button_20_bool

