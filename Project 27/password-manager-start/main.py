from tkinter import *
from tkinter import messagebox
from random import *
from pyperclip import copy
import json
pas = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gene():
    global pas
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_let = [choice(letters) for i in range(randint(8, 10))]
    password_sym = [choice(numbers) for i in range(randint(4, 5))]
    password_num = [choice(symbols) for i in range(randint(4, 5))]

    password_list = password_let + password_sym + password_num
    shuffle(password_list)
    password = ''.join(password_list)
    pas = password
    pass_entry.insert(0, pas)
    copy(pas)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_f():
    web_name = web_entry.get()
    email_name = email_entry.get()
    pass_name = pass_entry.get()
    c = 0
    if len(web_name) == 0:
        messagebox.showwarning(title="Warning", message="Please fill the Website field")
        c += 1
    if len(pass_name) == 0:
        messagebox.showwarning(title="Warning", message="Please fill the Passwword field")
        c += 1

    new_dict = {
        web_name:{
            "email": email_name,
            "password": pass_name,
        }
    }
    if c == 0:
        yon = messagebox.askokcancel(title=web_name, message=f"Do you want to include the details: \nEmail : {email_name}\nPassword : {pass_name}")
        if yon:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_dict, file, indent=4)
            else:
                data.update(new_dict)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                messagebox.showinfo(title="Status: Inserted", message="Successfully inserted the data")
# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            c = 0
            for i in data:
                if i == web_entry.get():
                    c += 1
                    messagebox.showinfo(title="Details", message=f"Email: {data[i]['email']}\nPassword: {data[i]['password']}")
            if c == 0:
                messagebox.showinfo(title="Error", message=f"Given name {web_entry.get()} is not found")
    except:
        messagebox.showinfo(title="Error", message="File not Found")


window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website: ", font=("Century", 12, 'normal'))
website.grid(row=1, column=0)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email = Label(text="Email: ", font=("Century", 12, 'normal'))
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "gugaanshanmugam2005@gmail.com")

password = Label(text="Password: ", font=("Century", 12, 'normal'))
password.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search = Button(text="Search", width=8, command=find_password)
search.grid(row=1, column=2)

generate = Button(text="Generate", command=gene)
generate.grid(row=3, column=2)

add = Button(width=36, text="Add", command=save_f)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()