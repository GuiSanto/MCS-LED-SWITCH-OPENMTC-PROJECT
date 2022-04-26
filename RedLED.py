#!/usr/bin/python

from tkinter import *
import requests
 
#Set display sizes
WINDOW_W = 1920
WINDOW_H = 1080

#Set display sizes
BUTTON_SIZE = 1920
MARGIN = 2

#Set colours
BLACK = '#000000'
RED = '#ff0000'
GREY = '#808080'


LIGHTOFFON=[GREY,RED]
OFF = 0
ON = 1
colourBackground = BLACK
colourButton = GREY
#Light Status
lightStatus=[OFF]

def createDisplay():
  global tk, canvas, light
  # create the tk window - within which
  # everything else will be built.
  tk = Tk()
  #Add a canvas area ready for drawing on
  canvas = Canvas(tk, width=WINDOW_W, height=WINDOW_H, background=BLACK)
  canvas.pack()
  #Add some "lights" to the canvas
  light = []
  x = MARGIN+((MARGIN+BUTTON_SIZE)*0)
  light.append(canvas.create_rectangle(x,MARGIN,
  x+BUTTON_SIZE,BUTTON_SIZE+MARGIN,fill=GREY))
  
  # Start the tk main-loop (this updates the tk display)
  
  # Create keyboard bindings
  tk.bind_all('<KeyPress-1>', handleInput)
  
  tk.mainloop()
 
def terminate():
 global tk
 tk.destroy()
 
 
def handleInput(event):
  inputkey = 0
  if event.keysym == '1':
    inputkey = 1
  #Handle the keyboard input
  if inputkey != 0:
    lightStatus[inputkey-1] = toggle(lightStatus[inputkey-1])
    canvas.itemconfig(light[inputkey-1], fill=LIGHTOFFON[lightStatus[inputkey-1]])
    
def toggle(value):
  if value == ON:
    value = OFF
  else:
    value = ON
  return value
 
def main():
 createDisplay()
 
if __name__ == '__main__':
 main()
