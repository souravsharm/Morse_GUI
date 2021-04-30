from tkinter import * 
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
 
root = Tk()
 
def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
 
    result = userEntry.get()
    list_of_letters = list(result.upper())
    for  a in list_of_letters:
     letters_morse(a)
    resultLabel.config(text=result)
    userEntry.delete(0,END)
 
# Create the Entry widget
userEntry = Entry(root, width=20)
userEntry.focus()
userEntry.bind("<Return>",returnEntry)
userEntry.pack()
 
 
 
 
 
 
# This command Creates the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry)
enterEntry.pack(fill=X)
 
 
# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)


def point():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1.2)
    GPIO.output(8,GPIO.LOW)


def dash():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(8,GPIO.LOW)

def letters_morse(letter):

    if letter == "A":
        point()
        time.sleep(1.2)
        dash()

    elif letter == "B":
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()

    elif letter == "C":
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()

    elif letter == "D":
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()

    elif letter == "E":
        point()

    elif letter == "F":
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()

    elif letter == "G":
        dash()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()

    elif letter == "H":
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()

    elif letter == "I":
        point()
        time.sleep(1.2)
        point()

    elif letter == "J":
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        dash()

    elif letter == "K":
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)

    elif letter == "L":
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()

    elif letter == "M":
        dash()
        time.sleep(1.2)
        dash()

    elif letter == "N":
        dash()
        time.sleep(1.2)
        point()

    elif letter == "O":
        dash()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        dash()

    elif letter == "P":
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()

    elif letter == "Q":
        dash()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()

    elif letter == "R":
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()

    elif letter == "S":
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()

    elif letter == "T":
        dash()

    elif letter == "U":
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()

    elif letter == "V":
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()

    elif letter == "W":
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        dash()

    elif letter == "X":
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()

    elif letter == "Y":
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        dash()

    elif letter == "Z":
        dash()
        time.sleep(1.2)
        dash()
        time.sleep(1.2)
        point()
        time.sleep(1.2)
        point()