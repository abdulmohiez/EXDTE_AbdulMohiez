# import the needed elements
import board
import analogio
import digitalio
import time
import pwmio
from ada_fruit import Debouncer
# creating a knob variable
knob = analogio.AnalogIn(board.A0)
# creating a variable to connect the led with the code
led = pwmio.PWMOut(board.GP16, frequency=1000)
# adding a button as well
button1 = digitalio.DigitalInOut(board.GP16)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
# intialiazing the button with debouncer
button_debounced = Debouncer(button1)
# intializing the the variables
button_pressed_time = 0
led_pressed_time = 0
# starting a while loop
while True:
    # updating the button
    button_debounced.update()
    # calculating the delay_time
    delay_time = knob.value / 5000
    # if loop started to check if the button is pressed or not
    if button_debounced.fell:
        # intializing the led.duty cycle
        led.duty_cycle = 0
        # adding a print statement to enhance the usability
        print("The button was pressed, LED is turned off!!!")
    # checking if the button rose
    if button_deboucned.rose:
        time.sleep(delay_time)
        led.duty_cycle = 32500
        print("The LED is turned on, Quickly press the button....")

    button_pressed_time = time.montonic()






