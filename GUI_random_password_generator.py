from tkinter import *
import random
import string
import re
character = list(string.ascii_letters + string.digits + "~!@#$%^&*")
root = Tk()
root.title("Strong Password Generator and Cheaker")
root.geometry("450x250")


def generate():
    new = Toplevel()
    new.title("Pop-Up")
    a = Label(new,text="Enter length of password",font=("consols",16)).pack(padx=10,pady=10)
    k = IntVar()
    e = Entry(new,font=("consols",18),textvariable=k)
    e.pack(padx=5,pady=5)
    # Generation password
    def gen1(x):
        password = ""
        for i in range (0,x) :
            f = random.choice(character)
            password += f
        return password
    def gen():
        if k.get() > 100:
            f.delete(0,END)
            f.insert(0,"Out Of Scope")
        else:
            a = gen1(k.get())
            f.delete(0,END)
            f.insert(0,a)
    
    b = Button(new,text="Submit",font=("consols",18),command=gen).pack(padx=5,pady=5)


def cheacker (a):
        ans = 0
        if (len(a)<6):
            ans+=1
        elif not (re.search("[a-z]",a)):
            ans+=1
        elif not (re.search("[A-Z]",a)):
            ans+=1
        elif not (re.search("[0-9]",a)):
            ans+=1
        elif not (re.search("[~!@#$%^&*]", a)):
            ans+=1
        return final(ans)

def final(ans):
        if (ans > 0):
            return "Password is in valid"
        else:
            return "Password is valid"

def clicked():
    a = t1.get()
    ans = cheacker(a)
    f.delete(0,END)
    f.insert(0,ans)


a = Label(text="Enter your password \n click on generate to check the password",font=("consols",18)).pack()
t1 = StringVar()
f = Entry(root,font=("consols",18),textvariable = t1)
f.pack()
b = Button(text="Check",font=("consols",16),padx=5,pady=5,command=clicked).pack(padx=5,pady=5)
c = Button(text="Generate",font=("consols",16),padx=5,pady=5,command=generate).pack(padx=5,pady=5)

root.mainloop()