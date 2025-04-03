from tkinter import *
from tkinter import messagebox
import ast

logged_in_user = None

root = Tk()
root.title('Banking System')
root.geometry('925x500+300+200')
root.configure(bg = "#fff")
root.resizable(False, False)

def signin():

    global logged_in_user

    username = user.get()
    password = psw.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]['password']:
        
        logged_in_user = username
        
        root.destroy()
        open_menu_window(r)
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def open_menu_window(r):
    menu_window = Tk()
    menu_window.title("Banking System")
    menu_window.geometry('925x500+300+200')
    menu_window.configure(bg = '#fff')
    menu_window.resizable(False, False)

    img = PhotoImage(file= 'pngegg.png')
    Label(menu_window, image = img, border = 0, bg = 'white').place(x = 50, y = 90)

    frame = Frame(menu_window, width = 350, height = 390, bg = '#fff')
    frame.place(x = 480, y = 50)

    heading = Label(frame, text = 'Menu', fg = "#57a1f8", bg = 'white', font = ('Microsoft Yahei UI Light', 36, 'bold'))
    heading.place(x = 120, y = 15)

    def get_account_details():
        if logged_in_user:
            account = r[logged_in_user]
            password = account['password']
            messagebox.showinfo("Account Details", f"Username: {logged_in_user}\nPassword: {password}")
        else:
            messagebox.showerror("Error")

    def show_balance():
        if logged_in_user:
            balance = r[logged_in_user]['balance']
            messagebox.showinfo("Balance", f"Balance: {balance}")
        else:
            messagebox.showerror("Error")

    def deposit(amount):
        if logged_in_user:
            r[logged_in_user]['balance'] += amount
            with open('datasheet.txt', 'w') as file:
                file.write(str(r))
            messagebox.showinfo("Deposit", f"Deposited {amount}.")
        else:
            messagebox.showerror("Error")

    def on_deposit():
        def submit_deposit():
            try:
                amount = float(deposit_amount_entry.get())
                deposit(amount)
                deposit_window.destroy()
            except:
                messagebox.showerror("Error", "Please enter a valid amount for deposit")

        deposit_window = Toplevel(menu_window)
        deposit_window.title("Deposit amount")
        deposit_window.geometry("300x200")

        Label(deposit_window, text = "Enter Deposit Amount:", font = ("Arial", 12)).pack(pady = 10)
        deposit_amount_entry = Entry(deposit_window, width = 20, font = ("Arial", 12))
        deposit_amount_entry.pack(pady = 10)

        Button(deposit_window, text = "Submit", command = submit_deposit).pack(pady = 10)

    def withdraw(amount):
        if logged_in_user:
            if r[logged_in_user]['balance'] >= amount:
                r[logged_in_user]['balance'] -= amount
                with open('datasheet.txt', 'w') as file:
                    file.write(str(r))
                messagebox.showinfo("Withdraw", f"Withdrew {amount}")
            else:
                messagebox.showerror("Error", "Insufficient balance")
        else:
            messagebox.showerror("Error")

    def on_withdraw():
        def submit_withdraw():
            try:
                amount = float(withdraw_amount_entry.get())
                withdraw(amount)
                withdraw_window.destroy()
            except:
                messagebox.showerror("Error", "Please enter a valid amount for withdrawal")

        withdraw_window = Toplevel(menu_window)
        withdraw_window.title("Withdraw amount")
        withdraw_window.geometry("300x200")
        
        Label(withdraw_window, text = "Enter Withdraw Amount:", font = ("Arial", 12)).pack(pady = 10)
        withdraw_amount_entry = Entry(withdraw_window, width = 20, font = ("Arial", 12))
        withdraw_amount_entry.pack(pady = 10)

        Button(withdraw_window, text = "Submit", command = submit_withdraw).pack(pady = 10)

    Button(frame, width = 27, pady = 7, text = 'Account detail', bg = '#57a1f8', fg = 'black', border = 0, command = get_account_details).place(x = 35, y = 80)
    Button(frame, width = 27, pady = 7, text = 'Show Balance', bg = '#57a1f8', fg = 'black', border = 0, command = show_balance).place(x = 35, y = 130)
    Button(frame, width = 27, pady = 7, text = 'Deposit', bg = '#57a1f8', fg = 'black', border = 0, command = on_deposit).place(x = 35, y = 180)
    Button(frame, width = 27, pady = 7, text = 'Withdraw', bg = '#57a1f8', fg = 'black', border = 0, command = on_withdraw).place(x = 35, y = 230)

    menu_window.mainloop()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
    window = Toplevel(root)
    window.title("Banking System")
    window.geometry('925x500+300+200')
    window.configure(bg = '#fff')
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = psw.get()
        comform_password = c_psw.get()

        if not username or username == "Username":
            messagebox.showerror('Invalid', "Please enter a valid username")
            return

        if password == comform_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                r[username] = {'password': password, 'balance': 0}  # Initial balance is 0
                ##dict2 = {username:password}
                ##r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Sucessfully sign up')
                window.destroy()

            except:
                file = open('datasheet.txt', 'w')
                file.write(str({username: {'password': password, 'balance': 0}}))  # Initialize with balance 0
                ##pp = str({'Username':'password'})
                ##file.write(pp)
                file.close

        else:
            messagebox.showerror('Invalid', "Both Password should match")

    def sign():
        window.destroy()

    img = PhotoImage(file= 'signup.png')
    Label(window, image = img, border = 0, bg = 'white').place(x = 50, y = 90)

    frame = Frame(window, width = 350, height = 390, bg = '#fff')
    frame.place(x = 480, y = 50)

    heading = Label(frame, text = 'Sign up', fg = "#57a1f8", bg = 'white', font = ('Microsoft Yahei UI Light', 36, 'bold'))
    heading.place(x = 120, y = 5)

#####-----------------------
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width = 25, fg = 'black', border=0, bg = 'white', font = ('Microsoft Yahei UI Light', 15),
                 highlightthickness = 0, insertbackground = 'black')
    user.place(x = 25, y = 89)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 107)

#####-----------------------
    def on_enter(e):
        psw.delete(0, 'end')

    def on_leave(e):
        if psw.get() == '':
            psw.insert(0, 'Password')

    psw = Entry(frame, width = 25, fg = 'black', border=0, bg = 'white', font = ('Microsoft Yahei UI Light', 15), 
                highlightthickness = 0, insertbackground = 'black')
    psw.place(x = 25, y = 159)
    psw.insert(0, 'Password')
    psw.bind("<FocusIn>", on_enter)
    psw.bind("<FocusOut>", on_leave)

    Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 177)

#####-----------------------
    def on_enter(e):
        c_psw.delete(0, 'end')

    def on_leave(e):
        if c_psw.get() == '':
            c_psw.insert(0, 'Confirm Password')

    c_psw = Entry(frame, width = 25, fg = 'black', border=0, bg = 'white', font = ('Microsoft Yahei UI Light', 15), 
                highlightthickness = 0, insertbackground = 'black')
    c_psw.place(x = 25, y = 229)
    c_psw.insert(0, 'Confirm Password')
    c_psw.bind("<FocusIn>", on_enter)
    c_psw.bind("<FocusOut>", on_leave)

    Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 247)

#---------------------------

    Button(frame, width = 27, pady = 7, text = 'Sign up', bg = '#57a1f8', fg = 'black', border = 0, command = signup).place(x = 35, y = 290)
    label = Label(frame, text = 'I have an account', fg = 'black', bg = 'white', font = ('Microsoft Yahei UI Light', 15))
    label.place(x = 70, y = 340)

    signin = Button(frame, width = 6, text = 'Sign in', border = 0, bg = 'white', cursor = 'hand2', fg = '#57a1f8',
                 highlightthickness = 0, borderwidth = 0, relief = 'flat', command = sign)
    signin.place(x = 200, y = 340)

    window.mainloop()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

img = PhotoImage(file = 'login.png')
Label(root, image = img, bg = 'white').place(x = 50, y = 50)

frame = Frame(root, width = 350, height = 350, bg = "white")
frame.place(x = 480, y = 70)

heading = Label(frame, text = 'Sign in', fg = "#57a1f8", bg = 'white', font = ('Microsoft Yahei UI Light', 36, 'bold'))
heading.place(x = 120, y = 5)

#####-----------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width = 25, fg = 'black', border=0, bg = 'white', font = ('Microsoft Yahei UI Light', 15),
             highlightthickness = 0, insertbackground = 'black')
user.place(x = 25, y = 89)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 107)

#####-----------------------
def on_enter(e):
    psw.delete(0, 'end')

def on_leave(e):
    if psw.get() == '':
        psw.insert(0, 'Password')

psw = Entry(frame, width = 25, fg = 'black', border=0, bg = 'white', font = ('Microsoft Yahei UI Light', 15), 
            highlightthickness = 0, insertbackground = 'black')
psw.place(x = 25, y = 159)
psw.insert(0, 'Password')
psw.bind("<FocusIn>", on_enter)
psw.bind("<FocusOut>", on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 177)

#####-----------------------
Button(frame, width = 27, pady = 7, text = 'Sign in', bg = '#57a1f8', fg = 'black', border = 0, command = signin).place(x = 35, y = 210)
label = Label(frame, text = "Don't have an account?", fg = 'black', bg = 'white', font = ('Microsoft Yahei UI Light', 15))
label.place(x = 30, y = 280)

signup = Button(frame, width = 6, text = 'Sign up', border = 0, bg = 'white', cursor = 'hand2', fg = '#57a1f8',
                 highlightthickness = 0, borderwidth = 0, relief = 'flat', command = signup_command)
signup.place(x = 200, y = 280)

root.mainloop()