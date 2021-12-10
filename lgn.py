from sqlite3.dbapi2 import SQLITE_OK
from sqlite_engine import *
from tkinter import *

sqlite3.connect("database.db")

## Functions
"""Sign Up Function"""
def sign_up(user, passw):
    """
    Args: Username, Password
    Return: If validated, A new user created,
            window will be destroyed
            and main window will appear.
    """
    c.execute("SELECT * FROM user_logins")
    d = c.fetchall()
    p = (user, passw)
    if user == "" or passw == "":
        print("Please Enter a username and password")
        w.config(text="Please Enter a username and password", fg="#B21F00")
        w.place(relx=0.5, 
                rely=0.75, 
                anchor=CENTER, )
        return
    # if user == "" and passw == "":
    #     print("Please enter username ")
    if not d:
        c.execute("INSERT INTO user_logins VALUES (?,?)", p)
        w.config(text="Account has been created!",  fg="#0DAC00")
        w.place(relx=0.5, 
                        rely=0.75, 
                        anchor=CENTER, )
        print("Test")
        c.execute("SELECT * FROM user_logins")
        print(c.fetchall())
        conn.commit()
    else:
        for i in range(len(d)):
                if user == d[i][0]:
                        print("Username taken")
                        w.config(text="Username Taken", fg="#B21F00")
                        w.place(relx=0.5, 
                            rely=0.75, 
                            anchor=CENTER, )
                        return
                else:
                    c.execute("INSERT INTO user_logins VALUES (?,?)", p)
                    w.config(text="Account has been created!",  fg="#0DAC00")
                    w.place(relx=0.5, 
                            rely=0.75, 
                            anchor=CENTER, )
                    print("Test")
                    c.execute("SELECT * FROM user_logins")
                    print(c.fetchall())
                    conn.commit()
                    return
    return 

"""Log In Function"""
def log_in(user, passw):
    """
    Args: Username, Password
    Return: If validated, window will be destroyed
            and main window will appear.
    """
    global x_pos, y_pos
    c.execute("SELECT * FROM user_logins")
    d = c.fetchall()
    p = (user, passw)
    if user == "" or passw == "":
        print("Please Enter a username and password")
        w.config(text="Please Enter a username and password", fg="#B21F00")
        w.place(relx=0.5, 
                rely=0.75, 
                anchor=CENTER, )
        return
    if not d:
        print("No accounts have been created yet...\nPlease sign in to make one :)")
        w.config(text="Account hasn't been created yet...", fg="#B21F00")
        w.place(relx=0.5, 
                rely=0.75, 
                anchor=CENTER, )
    else:
        for i in range(len(d)):
            print(d)
            if user not in d[i]:
                # print("FALSE")
                print("No accounts have been created yet...\nPlease sign in to make one :)")
                w.config(text="Account hasn't been created yet...", fg="#B21F00")
                w.place(relx=0.5, 
                rely=0.75, 
                anchor=CENTER, )
            else:
                if user == d[i][0]:
                    print("Username available")
                    if passw == d[i][1]:
                        print("Password available")
                        print("{} logged in!!".format(user))
                        x_pos = root.winfo_x()
                        y_pos = root.winfo_y()
                        print(x_pos)
                        print(y_pos)        
                        root.destroy()
                        return
                    else:
                        print("Password incorrect")
                        w.config(text="Incorrect Password", fg="#B21F00")
                        w.place(relx=0.5, 
                                rely=0.75, 
                                anchor=CENTER, )
                        return
    return

## Window Properties
root = Tk()
root.title("Sign Up")
root.geometry("450x280")
root.config(bg="#131512")
root.resizable(False, False)



## Variables
l_user = StringVar()
l_pass= StringVar()
s_user = StringVar()
s_pass = StringVar()
string = StringVar()


## Frames
fl = Frame(root, 
            width=225, 
            height=280,
            background="#131512")

fs = Frame(root, 
            width=225, 
            height=280, 
            background="#131512")

line = Frame(root, 
            width=1, 
            height=250, 
            background="#00a7e5").place(x=225,y=10)

fl.place(x=0,y=0)
fl.grid_propagate(0)
fs.place(x=225,y=0)
fs.grid_propagate(0)

## Labels
l1 = Label(fl, 
            text="Log In", 
            background="#131512", 
            fg="#00a7e5")
l1.place(x=56,y=70)

s1 = Label(fs, 
            text="Sign Up", 
            background="#131512", 
            fg="#00a7e5")
s1.place(x=56,y=70)

w = Label(root,
        background="#131512",
        fg="#B21F00")

## Login Entries
l_user_entry = Entry(fl, textvariable=l_user)
l_user_entry.place(x=56,y=100)

l_pass_entry = Entry(fl, textvariable=l_pass, show="*")
l_pass_entry.place(x=56,y=120)

## SignUp Entries
s_user_entry = Entry(fs, textvariable=s_user)
s_user_entry.place(x=56,y=100)

s_pass_entry = Entry(fs, textvariable=s_pass, show="*")
s_pass_entry.place(x=56,y=120)

## Buttons
b_log = Button(fl, 
                width= 5, height=1, 
                text="Login", 
                fg="#00a7e5", 
                bg="#131512", 
                border= False, 
                command=lambda: log_in(l_user.get(), l_pass.get()))

b_sign = Button(fs, 
                width= 5, height=1, 
                text="SignIn", 
                fg="#00a7e5", 
                bg="#131512", 
                border= False, 
                command=lambda: sign_up(s_user.get(), s_pass.get()))

b_log.place(x=84,y=150)
b_sign.place(x=84,y=150)


conn.commit()
root.mainloop()

