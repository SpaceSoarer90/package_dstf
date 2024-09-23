import serial
from tkinter import *

arduino = serial.Serial('/dev/ttyUSB0', 19200)

def clockwise():
    arduino.write(b'CLOCKWISE')

root = Tk()
btn_clockwise = Button(root, text="CW", command=clockwise)
btn_clockwise.pack(pady=20)

root.mainloop()
arduino.close()
