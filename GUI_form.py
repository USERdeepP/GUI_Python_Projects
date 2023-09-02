from tkinter import *
window = Tk()

def f1() :
    with open("D:\\Python Programs\\Projects\\1.txt","a") as file :
        file.write(f"Name = {v1.get()} \n")
        file.write(f"Phone Number = {v2.get()} \n")
        file.write(f"Date Of Birth = {v3.get()} \n")
        file.write(f"Address = {v4.get()} \n \n ")
    l5=Label(text="Successfull").grid(row=6,column=1)    
    

window.geometry("400x300")
window.title("GUI Form")
l1 = Label(text="Name ", font=("concloes",12)).grid(row=0)
l2 = Label(text="Phone Number ", font=("concloes",12)).grid(row=1)
l3 = Label(text="Date Of Birth ", font=("concloes",12)).grid(row=2)
l4 = Label(text="Address ", font=("concloes",12)).grid(row=3)

v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

e1=Entry(window,textvariable=v1,font=("consols",12)).grid(row=0,column=2)
e2=Entry(window,textvariable=v2,font=("consols",12)).grid(row=1,column=2)
e3=Entry(window,textvariable=v3,font=("consols",12)).grid(row=2,column=2)
e4=Entry(window,textvariable=v4,font=("consols",12)).grid(row=3,column=2)
x = Label(text="").grid(row=4,column=1)
b=Button(text="Submit",font=("consoles 12"),pady=3,padx=3,command=f1).grid(row=5,column=1)


window.mainloop()