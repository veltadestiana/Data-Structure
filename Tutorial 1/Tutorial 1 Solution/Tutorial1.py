"""Tutorial 1"""
# Name: [fill in your name here]
# NPM: [fill in you NPM here]

from tkinter import *

def loadMap(filename):
    # Loads .map file, filters numbers only and returns a 2D array
    # [TO DO]
    rawfile = open(filename)
    file = (rawfile.read())
    file = list(filter(lambda x: x.isdigit(), file))
    array = [] # array is now 1D list of numbers
    for i in range(30):
        # converts 1D array to 30x30 2D array
        array.append(file[:30])
        file = file[30:]
    rawfile.close()
    return array

def renderMap(mapfile):
    # Accepts 2D array, creates a tkinter GUI and canvas, reads the array
    # then renders a 600x600 graphic gamespace according to the array's
    # values.
    # [TO DO]
    r = Tk()
    r.title("Tutorial 1")
    c = Canvas(r, width=600, height=600)
    c.pack()
    # Image dictionary for holding PhotoImage instances of .gif
    # Available directories: ./sprite, ./sprite/emoji
    imgdict = {'0':PhotoImage(file = './sprite/emoji/0.gif'),
               '1':PhotoImage(file = './sprite/emoji/1.gif'),
               '2':PhotoImage(file = './sprite/emoji/2.gif'),
               '3':PhotoImage(file = './sprite/emoji/3.gif'),
               '4':PhotoImage(file = './sprite/emoji/4.gif')}
    y = 0
    for line in mapfile:# iterates by row
        x = 0
        for i in line:  # iterates by column
            # array value provides index for image dict
            c.create_image(15+x*20,15+y*20,image=imgdict[i])
            x += 1
        y+=1
    r.mainloop()

# Main program
if __name__ == "__main__":
    renderMap(loadMap('test.map'))
    
    
