from tkinter import *
import tkinter.filedialog as f

window = Tk()
window.title("My-Notepad")
window.iconbitmap("")

def saveas() :
    global text  
    t = text.get("1.0", "end-1c")
    savelocation= f.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()


button=Button(window, text="Save", command=saveas,font=('consol 10 bold')) 
button.pack()


text = Text(window,font=('consol 12'))
text.pack()










window.mainloop()