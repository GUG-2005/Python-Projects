# # def add(*args):
# #     sum = 0
# #     for i in args:
# #         sum += i
# #     print(sum)
# #
# # add(3,5)
#
# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#
# my_car = Car(make="Mahindra", model="Xylo")
# print(my_car.color)

from tkinter import *

window = Tk()
window.title("Examole")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

label = Label(text="This is Label", font=("Times New Roman", 13, "bold"))
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

b1 = Button(text="Click here")
b1.grid(column=1, row=1)
b1.config(pady=50, padx=50)

b2 = Button(text="Click here")
b2.grid(column=2, row=0)
b2.config(padx=50, pady=50)

en = Entry()
print(en.get())
en.grid(column=3, row=2)

window.mainloop()