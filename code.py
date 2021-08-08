import board
import digitalio
import time
import usb_hid
import rotaryio
import busio

from adafruit_hid.keyboard import Keyboard

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from keys_dict.keys import key_lookup

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

BlueLed = digitalio.DigitalInOut(board.GP21)
BlueLed.direction = digitalio.Direction.OUTPUT
GreenLed = digitalio.DigitalInOut(board.GP20)
GreenLed.direction = digitalio.Direction.OUTPUT
YellowLed = digitalio.DigitalInOut(board.GP19)
YellowLed.direction = digitalio.Direction.OUTPUT
RedLed = digitalio.DigitalInOut(board.GP18)
RedLed.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

pins = [board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP12]

KEY = 1

keymap = {

    (0): (KEY, [Keycode.ONE]),
    (1): (KEY, [Keycode.TWO]),

    (7): (KEY, [Keycode.THREE]),
    (8): (KEY, [Keycode.FOUR]),
    (5): (KEY, [Keycode.FIVE]),

    (4): (KEY, [Keycode.SIX]),
    (9): (KEY, [Keycode.SEVEN]),
    (3): (KEY, [Keycode.EIGHT]),

    (2): (KEY, [Keycode.NINE]),
    (6): (KEY, [Keycode.COMMAND, Keycode.Z]),
    (10): (KEY, [Keycode.B]),


}

keymap2 = {

    (0): (KEY, [Keycode.A]),
    (1): (KEY, [Keycode.B]),

    (7): (KEY, [Keycode.C]),
    (8): (KEY, [Keycode.D]),
    (5): (KEY, [Keycode.E]),

    (4): (KEY, [Keycode.F]),
    (9): (KEY, [Keycode.G]),
    (3): (KEY, [Keycode.H]),

    (2): (KEY, [Keycode.NINE]),
    (6): (KEY, [Keycode.COMMAND, Keycode.Z]),
    (10): (KEY, [Keycode.J]),
}

keymap3 = {

    (0): (KEY, [Keycode.ONE]),
    (1): (KEY, [Keycode.TWO]),

    (7): (KEY, [Keycode.THREE]),
    (8): (KEY, [Keycode.FOUR]),
    (5): (KEY, [Keycode.FIVE]),

    (4): (KEY, [Keycode.SIX]),
    (9): (KEY, [Keycode.SEVEN]),
    (3): (KEY, [Keycode.EIGHT]),

    (2): (KEY, [Keycode.NINE]),
    (6): (KEY, [Keycode.COMMAND, Keycode.Z]),
    (10): (KEY, [Keycode.B]),


}

keymap4 = {

    (0): (KEY, [Keycode.A]),
    (1): (KEY, [Keycode.B]),

    (7): (KEY, [Keycode.C]),
    (8): (KEY, [Keycode.D]),
    (5): (KEY, [Keycode.E]),

    (4): (KEY, [Keycode.F]),
    (9): (KEY, [Keycode.G]),
    (3): (KEY, [Keycode.H]),

    (2): (KEY, [Keycode.NINE]),
    (6): (KEY, [Keycode.COMMAND, Keycode.Z]),
    (10): (KEY, [Keycode.J]),


}

switches = []
for i in range(len(pins)):
    switch = digitalio.DigitalInOut(pins[i])
    switch.direction = digitalio.Direction.INPUT
    switch.pull = digitalio.Pull.UP
    switches.append(switch)

switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

switch_state2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

switch_state3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

switch_state4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

""" Not using this int for now...

numStates = 4"""

button_state = None


while True:
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        BlueLed.value = True
        button_state = "Blue"
    if not button.value and button_state == "Blue":
        BlueLed.value = False
        button_state = "pressed2"
    if button.value and button_state == "pressed2":
        GreenLed.value = True
        button_state = "Green"
    if not button.value and button_state == "Green":
        GreenLed.value = False
        button_state = "pressed3"
    if button.value and button_state == "pressed3":
        YellowLed.value = True
        button_state = "Yellow"
    if not button.value and button_state == "Yellow":
        YellowLed.value = False
        button_state = "pressed4"
    if button.value and button_state == "pressed4":
        RedLed.value = True
        button_state = "Red"
    if not button.value and button_state == "Red":
        RedLed.value = False
        button_state = "pressed"


    for i in range(11):
        if switch_state[i] == 0 and button_state == "Blue":
            if not switches[i].value:
                try:
                    if keymap[i][0] == KEY:
                        kbd.press(*keymap[i][1])
                    else:
                        cc.send(keymap[i][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state[i] = 1

        if switch_state[i] == 1:
            if switches[i].value:
                try:
                    if keymap[i][0] == KEY:
                        kbd.release(*keymap[i][1])

                except ValueError:
                    pass
                switch_state[i] = 0


        if switch_state2[i] == 0 and button_state == "Green":
            if not switches[i].value:
                try:
                    if keymap2[i][0] == KEY:
                        kbd.press(*keymap2[i][1])
                    else:
                        cc.send(keymap2[i][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state2[i] = 1

        if switch_state2[i] == 1:
            if switches[i].value:
                try:
                    if keymap2[i][0] == KEY:
                        kbd.release(*keymap2[i][1])

                except ValueError:
                    pass
                switch_state2[i] = 0

        if switch_state3[i] == 0 and button_state == "Yellow":
            if not switches[i].value:
                try:
                    if keymap3[i][0] == KEY:
                        kbd.press(*keymap3[i][1])
                    else:
                        cc.send(keymap3[i][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state3[i] = 1

        if switch_state3[i] == 1:
            if switches[i].value:
                try:
                    if keymap3[i][0] == KEY:
                        kbd.release(*keymap3[i][1])

                except ValueError:
                    pass
                switch_state3[i] = 0

        if switch_state4[i] == 0 and button_state == "Red":
            if not switches[i].value:
                try:
                    if keymap4[i][0] == KEY:
                        kbd.press(*keymap4[i][1])
                    else:
                        cc.send(keymap4[i][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state4[i] = 1

        if switch_state4[i] == 1:
            if switches[i].value:
                try:
                    if keymap4[i][0] == KEY:
                        kbd.release(*keymap4[i][1])

                except ValueError:
                    pass
                switch_state4[i] = 0

    time.sleep(0.01)  # debounce





