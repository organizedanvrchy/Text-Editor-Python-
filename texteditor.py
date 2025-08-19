from tkinter import *
import tkinter.filedialog

def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

def fontHelvetica():
    global text
    text.config(font = "Helvetica")

def fontCourier():
    global text
    text.config(font = "Courier")

def fontLexend():
    global text
    text.config(font = "Lexend")

# Main
root = Tk("Text Editor")

text = Text(root)
text.grid()

button = Button(root, text = "Save", command = saveAs)
button.grid()

font = Menubutton(root, text = "Font")
font.grid()

font.menu = Menu(font, tearoff = 0)
font["menu"] = font.menu

Helvetica = IntVar()
Courier = IntVar()
Lexend = IntVar()

font.menu.add_checkbutton(
    label = "Helvetica", 
    variable = Helvetica, 
    command = fontHelvetica
)

font.menu.add_checkbutton(
    label = "Courier", 
    variable = Courier, 
    command = fontCourier
)

font.menu.add_checkbutton(
    label = "Lexend", 
    variable = Lexend, 
    command = fontLexend
)

root.mainloop()