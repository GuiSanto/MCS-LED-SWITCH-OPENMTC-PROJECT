from tkinter import *
import tkinter.font as font

def select_led():
 if(button1['text'] == 'LED 1'):
  button1['text'] = 'LED 2'
 else:
  button1['text'] = 'LED 1'


def change_state():
 #check the state of the led and reverse it
 print("!state")
	
	
window=Tk()

#title
label=Label(window, text="Virtual Switch", fg='red', font=("Helvetica", 40))
label.place(x=800, y=50)

#text size of both buttons
f = font.Font(family='Times New Roman', size=50, weight="bold")

#button to select the LED
button1=Button(window, fg = 'black', text = "LED 1", font = f, command = select_led, height = 9, width= 23)
button1.place(x=100, y=200)

#button to turn ON or OFF
button2=Button(window, fg = 'black', font = f, command = change_state, height = 9, width= 23)
button2.place(x=950, y=200)

window.title('Virtual Switch')
#put the resolution of YOUR PC
window.geometry("1920x1080")


window.mainloop()

