from tkinter import *
#joeditor
#By Erik "Joe" Pastori

from tkinter import Tk, font

root = Tk()
options = root.call('font', 'names')
root.destroy()


root = Tk()
root.geometry("250x400")
joefont = ["Comic Sans MS", 20, "normal"]
#Found the above in a github, seems useful!

clicked = StringVar()

clicked.set(joefont[0])

icon = PhotoImage(file="Joeditor.png") 
root.iconphoto(False, icon)
root.title("Joeditor")

scroll=Scrollbar(root, orient='vertical')
scroll.pack(side=RIGHT, fill='y')

root.resizable(True,True)

joetuple = (joefont[0], joefont[1], joefont[2])

text = Text(root, yscrollcommand=scroll.set, font=joetuple)

scroll.config(command=text.yview)

def apply_size(selected_size):
    global joefont
    text.config(font=(joefont[0], selected_size))
    joefont[1] = selected_size

def apply_font(selected_font):
    global joefont
    text.config(font=(selected_font, joefont[1]))
    joefont[0] = selected_font

def font():
    #ChatGPT Assistance, I made the font adjustments to the menu, changing font based on name
    root = Tk()
    root.title("Font List")

    font_list = root.call("font", "families")

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(frame)
    canvas.pack(side=LEFT, fill=Y)

    scrollbar = Scrollbar(frame, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor=NW)

    for font_name in font_list:
        button = Button(inner_frame, font=(font_name, 17), text=font_name, command=lambda name=font_name: apply_font(name))
        button.pack(fill=X, padx=5, pady=2)

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

def size():
    global size_input
    sizerama = size_input.get()
    apply_size(sizerama)

changefontbutton = Button(root, text="Font", command=font)
changefontbutton.pack()

size_input = Entry(root, width=4)
size_input.pack()

size_button = Button(root, text="Size", command=size)
size_button.pack()

text.pack()

root.mainloop()
