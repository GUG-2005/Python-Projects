from tkinter import *

window = Tk()
window.title("Miles to Kilomtres Converter")
window.minsize(width=150, height=150)
window.config(padx=100, pady=100)

label = Label(text="Enter the miles: ", font=("Times New Roman", 15, 'normal'))
label.grid(column=0, row=0)

entry = Entry()
entry.grid(column=1, row=0)

label1 = Label(text="is equal to", font=("Times New Roman", 15, 'normal'))
label1.grid(column=0, row=1)


label2 = Label(text="0", font=("Times New Roman", 15, 'normal'))
label2.grid(column=1, row=1)

label3 = Label(text="Kilometres", font=("Times New Roman", 15, 'normal'))
label3.grid(column=2,row=1)


def calculate():
    miles = entry.get()
    km = int(miles)*1.609344
    label2.config(text=f"{round(km, 2)}")

but = Button(text="Calculate", command=calculate)
but.grid(column=1,row=2)

window.mainloop()