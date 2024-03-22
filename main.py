import random

import os
import cairo
import math

import tkinter as tk

#generate art
def generate(runs):

    i = 0

    while i < runs:
        randintx = random.randint(0, 256)
        randinty = random.randint(0, 256)

        randh = random.randint(0, 256)
        randw = random.randint(0, 256)

        #generate 3 random floats between 0 and 1 and round them to two decimal places
        rand1 = random.random()
        rand1 = round(rand1, 2)

        rand2 = random.random()
        rand2 = round(rand2, 2)

        rand3 = random.random()
        rand3 = round(rand3, 2)

        #draw rectangles with randoms as parameters
        ctx.set_source_rgb(rand1, rand2, rand3)
        ctx.rectangle(randintx, randinty, randw, randh)
        ctx.fill()

        #print(f"runs:{i}")
        i += 1

#listen for enter key and print current entry
def listener(entry):
    print(entry.widget.get())

    entry.widget.delete(0,tk.END)

if __name__ == '__main__':

    #set height of project
    WIDTH, HEIGHT = 256, 256

    sfc = cairo.ImageSurface(cairo.Format.ARGB32, WIDTH, HEIGHT)

    #create context
    ctx = cairo.Context(sfc)

    #set base source color (rgb) to random
    randbase1 = random.random()
    round(randbase1, 2)

    randbase2 = random.random()
    round(randbase2, 2)

    randbase3 = random.random()
    round(randbase3, 2)

    ctx.set_source_rgb(randbase1, randbase2, randbase3)

    #draw background rectangle
    ctx.rectangle(0, 0, WIDTH, HEIGHT)

    #fill current path (?)
    ctx.fill()

    #basic rectangle
    # ctx.set_source_rgb(0.9, 0.1, 0.2)
    # ctx.rectangle(50, 20, 120, 80)
    # ctx.fill()

    """
    #prompt user for # of rectangles to generate, if none defaults to a random int 0 < x < 256
    print("rectangles to generate: ")
    try:
        runs = int(input())
    except:
        runs = random.randint(0,256)
        print(f"Invalid input, defaulting to {runs}")

    if runs == 0 or runs == "":
        runs = random.randint(0,256)
    else:
        print(runs)
    """

    #call random recatngle function

    #random # of runs
    runs = random.randint(0,256)

    if runs == 256:
        print("bingo!")

    generate(runs)

    #write to image
    output_filename = 'hello_world.png'
    sfc.write_to_png(output_filename)

    #tkinter
    #==========================================#
    #window


    #create window
    window = tk.Tk()

    #text label
    label = tk.Label(text="Name")

    #text entry
    entry = tk.Entry(window)

    label.pack()
    entry.pack()

    #bind enter to return, call listener()
    window.bind("<Return>", listener)


    window.mainloop()

    #open image with defualt image viewer
    #os.system(output_filename)

