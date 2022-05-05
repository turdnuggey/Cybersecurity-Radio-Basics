# text_terminal_to_radio.py

from microbit import *
import radio

radio.on()
radio.config(channel = 7)

sleep(1000)

print("micro:bit radio sender")

while True:
    message = input("Send: ")
    radio.send(message) 