import random

import os
import cairo
import math

import tkinter as tk

from tkinter import messagebox as mb


def generate(runs):
    print(f"Generating...{runs}")

    # random colors
    rand_color1 = random.random()
    rand_color1 = round(rand_color1, 2)

    rand_color2 = random.random()
    rand_color2 = round(rand_color2, 2)

    rand_color3 = random.random()
    rand_color3 = round(rand_color1, 2)

    i = 0

    while i < runs:
        randintx = random.randint(0, 256)
        randinty = random.randint(0, 256)

        randh = random.randint(0, 256)
        randw = random.randint(0, 256)

        # random colors
        rand_color1 = random.random()
        rand_color1 = round(rand_color1, 2)

        rand_color2 = random.random()
        rand_color2 = round(rand_color2, 2)

        rand_color3 = random.random()
        rand_color3 = round(rand_color3, 2)

        # increment colors
        rand_color_inc1 = rand_color1 + 0.1

        rand_color_inc2 = rand_color2 + 0.1

        rand_color_inc3 = rand_color3 + 0.1

        # check if color can be incremented
        if (rand_color_inc1 <= 1):

            #print(f"Base:{rand_color1}")
            #print(f"Inc:{rand_color_inc1}")

            rand_color1 = rand_color_inc1

        if (rand_color_inc2 <= 1):
            rand_color2 = rand_color_inc2

        if (rand_color_inc3 <= 1):
            rand_color3 = rand_color_inc3


        # generate 3 random floats between 0 and 1 and round them to two decimal places
        rand1 = random.random()
        rand1 = round(rand1, 2)

        rand2 = random.random()
        rand2 = round(rand2, 2)

        rand3 = random.random()
        rand3 = round(rand3, 2)

        # arc test
        ctx.arc(randintx,randinty,21,100,1*22/7)
        #ctx.fill()

        ctx.set_source_rgb(rand_color1, rand_color2, rand_color3)

        #print(f"{rand_color1},{rand_color2},{rand_color3}")

        ctx.rectangle(randintx, randinty, randw, randh)

        print(f"x:{randintx}, y:{randinty}, W:{randw}, H:{randh}")
        print(randintx * 0.33)

        # draw cow legs
        ctx.rectangle(randintx * 0.33, randinty * 0.33, randw / 2, randh / 2)

        ctx.fill()

        ctx.stroke()

        # print(f"runs:{i}")
        i += 1

    # write to file
    output_filename = 'hello_world.png'
    sfc.write_to_png(output_filename)


# tkinter gui

# listen for enter key and print current entry
def listener(text_entry):
    try:
        user_in = text_entry.widget.get()
        print(user_in)
    except:
        print("null")

    text_entry.widget.delete(0, tk.END)

# update image
def regen_img():

    # random for regeneration
    random_int = random.randint(0, 256)

    # regenerate
    generate(random_int)
    #generate(1)

    # update image
    new_output = tk.PhotoImage(file="hello_world.png")
    w1.configure(image=new_output)
    w1.image = new_output

# regen single image
def regen_img_single():

    # regenerate
    generate(1)

    # update image
    new_output = tk.PhotoImage(file="hello_world.png")
    w1.configure(image=new_output)
    w1.image = new_output


# set image to default blank
def blank_img():
    ctx.rectangle(0,0,256,256)
    ctx.set_source_rgb(255,255,255)
    ctx.fill()

    new_output = tk.PhotoImage(file="blank.png")
    w1.configure(image=new_output)
    w1.image = new_output

# works, not used
def delete_img():
    # prompt user - works
    msg = mb.askquestion("Delete Image", "Delete?")

    if (msg == 'yes'):
        # save path for dialog
        temp_path = os.path.abspath("hello_world.png")
        temp_path = os.path.abspath("blank.png")

        print(temp_path)
        # remove file

        blank_img()

        os.remove("hello_world.png")

    else:
        mb.showinfo("Return", "Returning...")

        print("Returning...")


def power_play():
    print("ass")
    return


if __name__ == '__main__':

    print("File: ", os.path.abspath('hello_world.png'))

    # set height of project
    WIDTH, HEIGHT = 256, 256

    sfc = cairo.ImageSurface(cairo.Format.ARGB32, WIDTH, HEIGHT)

    # create context
    ctx = cairo.Context(sfc)

    # set base source color (rgb) to random
    randbase1 = random.random()
    round(randbase1, 2)

    randbase2 = random.random()
    round(randbase2, 2)

    randbase3 = random.random()
    round(randbase3, 2)

    ctx.set_source_rgb(randbase1, randbase2, randbase3)

    # draw background rectangle
    ctx.rectangle(0, 0, WIDTH, HEIGHT)

    # fill current path (?)
    ctx.fill()

    # basic rectangle
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

    # call random recatngle function

    # random # of runs
    #runs = random.randint(0, 256)

    runs = 1

    if runs == 256:
        print("bingo!")

    generate(runs)

    # write to image
    output_filename = 'hello_world.png'
    sfc.write_to_png(output_filename)

    # tkinter below

    # create root window
    root = tk.Tk()

    # set dimensions
    root.geometry("500x250")

    # picture test
    output = tk.PhotoImage(file="hello_world.png")

    w1 = tk.Label(root, image=output)

    # text label
    label = tk.Label(text="Computer Art")

    # text entry
    entry = tk.Entry()

    # pack to window size
    w1.pack(side="right")
    label.pack()
    entry.pack()

    # regenerate button
    gen_button = tk.Button(root, text="Generate", command=regen_img_single)

    gen_button.pack(pady=10)

    random_button = tk.Button(root, text = "Generate random", command = regen_img)

    random_button.pack(pady=10)

    # blank button
    blank_button = tk.Button(root, text="Blank", command=blank_img)

    blank_button.pack(pady=10)

    # delete button, not used
    """
    del_button = tk.Button(root, text="Delete", command=delete_img)

    del_button.pack(pady=10)

    # bind enter to return, call listener()
    root.bind("<Return>", listener)
    """

    root.mainloop()

    # open image with default image viewer
    # os.system(output_filename)

    # scrubs
