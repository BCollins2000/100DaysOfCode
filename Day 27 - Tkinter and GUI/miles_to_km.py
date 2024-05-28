from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)

label_1 = Label(text="Km")
label_1.grid(row = 1, column = 2)

label_2 = Label(text="is equal to")
label_2.grid(row = 1, column = 0)

label_3 = Label(text="Miles")
label_3.grid(row = 0, column = 2)

label_3.grid(row = 0, column = 2)

conv_label = Label(text="0")
conv_label.grid(row = 1, column = 1)

#Entries
input = Entry(width=10)
input.grid(row = 0, column = 1)

label_3 = Label(text="Miles")

def button_clicked():
    old_num = input.get()
    new_num = int(old_num) * 1.609
    conv_label["text"] = new_num

button = Button(text="Calculate", command=button_clicked)
button.grid(row = 2, column = 1)

window.mainloop()