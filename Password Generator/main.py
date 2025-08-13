import json
from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data not found!!")
    else:
        website = website_entry.get().capitalize()
        if website in data:
            messagebox.showinfo(title=f"{website}",
                                message=f"Email:{data[website]['Email']}\nPassword:{data[website]['Password']}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists!!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list+=[random.choice(letters) for _ in range(nr_letters)]
    password_list +=[random.choice(symbols) for _ in range(nr_symbols)]
    password_list +=[random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(website_entry.get())==0 or len(password_entry.get())==0:
        messagebox.showerror(title="Oops",message="Please do not leave any fields empty!!")
    else:
        ok=messagebox.askokcancel(title=website_entry.get().capitalize(),message=f"Are you sure you want to save the following information:\nEmail: {username_entry.get()}\nPassword: {password_entry.get()}")
        if ok:
            data = {website_entry.get().capitalize(): {"Email": username_entry.get(), "Password": password_entry.get()}}
            try:
                with open("data.json", "r") as file:
                    info=json.load(file)
                    info.update(data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(data, file,indent=4)
            else:
                with open("data.json","w") as file:
                    json.dump(info,file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
logo_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_image)
logo_canvas.grid(column=1, row=0)

# Website Label & Entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

# Email/Username Label & Entry
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=50)
username_entry.insert(0, "abc@gmail.com")
username_entry.grid(column=1, columnspan=2, row=2)

# Password Label & Entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
search_button=Button(text="Search",command=find_password,width=13)
search_button.grid(column=2,row=1)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42,command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()