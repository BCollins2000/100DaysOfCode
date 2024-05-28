from tkinter import *


window = Tk()
window.title("My first GUI program.")
window.minsize(width=500, height =300)


#label
my_label = Label(text="I am a label", font = ("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "Nicely Done."

my_label.config(text="Exceptional")

#click_num = 0
def button_clicked():
    #global click_num
    new_text = input.get()
    #click_num += 1
    my_label["text"] = new_text


input = Entry(width=10)
input.pack()



button = Button(text="click me", command = button_clicked)
button.pack()








window.mainloop()