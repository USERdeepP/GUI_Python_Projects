from tkinter import *
import random

window = Tk()
window.geometry("335x100")
window.title("Game")
    
a = ['stone','paper','scissor']
def game(player):
    computer = random.choice(a)
    l=f"computer choes {computer}"
    if(player == computer):
        l1="its a tie"
    elif(player == 'scissor' and computer == 'paper'):
        l1="congratulation you won"
    elif(player == 'stone' and computer == 'paper'):
        l1="bad you lost"
    elif(player == 'paper' and computer == 'stone'):
        l1="congratulation you won"
    elif(player == 'scissor' and computer == 'stone'):
        l1="bad you lost"
    elif(player == 'stone' and computer == 'scissor'):
        l1="congratulation you won"
    elif(player == 'paper' and computer == 'scissor'):
        l1="bad you lost"
    return f"\n\t You chose {player} \n\n\t {l} \n\n\t {l1}"
def st():
    player = "stone"
    ans = game(player)  #stored the return of game in ans and passed it to open_popup to display in popup
    open_popup(ans)
def sc():
    player = "scissor"
    ans = game(player)
    open_popup(ans)
def pa():
    player = "paper"
    ans = game(player)
    open_popup(ans)

def open_popup(ans):
   top= Toplevel(window)
   top.geometry("500x250")
   top.title("result")
   Label(top, text = ans, font=('consol 18 bold')).place(x=0,y=0)

title_of_game = Label(text="Choose Your Move",font=("consols",16),pady=5).grid(row=0,column=1,columnspan=6)
stone = Button(text="STONE",command=st,font=("consols",12),padx=3,pady=3).grid(row=1,column=2)
paper = Button(text="PAPER",command=pa,font=("consols",12),padx=3,pady=3).grid(row=1,column=4)
scissor = Button(text="SCISSOR",command=sc,font=("consols",12),padx=3,pady=3).grid(row=1,column=6)

us1=Label(text=" ",padx=5,pady=5).grid(row=0)
us2=Label(text=" ",padx=5,pady=5).grid(row=1,column=1)
us3=Label(text=" ",padx=5,pady=5).grid(row=1,column=3)
us4=Label(text=" ",padx=5,pady=5).grid(row=1,column=5)
us5=Label(text=" ",padx=5,pady=5).grid(row=2,column=4)



window.mainloop()