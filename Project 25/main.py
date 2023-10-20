from tkinter import *

window = Tk()
window.title("First Project")
window.minsize(width=500, height=500)

#Label
label = Label(text="Change the label with your text", font=("Times New Roman", 24, "bold"))
label.pack()

#Entry
entry = Entry(width=20)
entry.pack()

def click():
    label.config(text=entry.get())

#Button
button = Button(text="Click Here", command=click)
button.pack()

#Text
text = Text(width=35, height=7)
text.focus()
text.insert(END,"Example of a multiline text entry")
print(text.get("1.0", END))
text.pack()

#spinbox
def use():
    print(spin.get())
spin = Spinbox(from_=0, to=10, width=5, command=use)
spin.pack()


#Scale
def use_sc(val):
    print(val)
scale = Scale(from_=0, to=100, command=use_sc)
scale.pack()

#checkButton
checked_state = IntVar()
def use_ch():
    print(checked_state.get())
check = Checkbutton(text="Is it On? ", variable=checked_state, command=use_ch)
checked_state.get()
check.pack()

#Radio Button
def use_r():
    print(radio_state.get())
radio_state = IntVar()
radio1 = Radiobutton(text="Option1", value = 1, variable=radio_state, command=use_r)
radio2 = Radiobutton(text="Option2", value = 2, variable=radio_state, command=use_r)
radio1.pack()
radio2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=3)
fruits =["Apple", "Orange", "Mango"]
for i in fruits:
    listbox.insert(fruits.index(i), i)
listbox.bind("<<ListBoxSelect>>", listbox_used)
listbox.pack()

window.mainloop()