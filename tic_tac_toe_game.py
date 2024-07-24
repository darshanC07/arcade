import tkinter as tk
from tkinter import messagebox


def making_buttons_grid():
    global buttons
    count = 0
    for i in range(3):
        for j in range(3):
            buttons[count].grid(row=i,column=j)
            count+=1

def disable_buttons():
    global buttons
    for i in range(9):
        buttons[i].config(state="disabled")

def reset_game():
    global buttons
    global current_player
    for button in buttons:
        button.config(text=" ",bg="white")
    current_player = "X"

def check_winner():
    global winning_combo
    global buttons
    for combo in winning_combo:
        if buttons[combo[0]]["text"]==buttons[combo[1]]["text"]==buttons[combo[2]]["text"] !=" ":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic Tac Tor",f"Player {buttons[combo[0]]['text']} wins!!")
            disable_buttons()

def toggle_player():
    global current_player
    current_player = "X" if current_player=="O" else "O"
    label.config(text=f"Player {current_player}'s Turn")


def button_click(index):
    global buttons
    if buttons[index]["text"]==" ":
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()


root = tk.Tk()
root.title("Tic Tac Toe")
winning_combo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

#creating list of buttons
buttons = [tk.Button(root,text = " ",background="white",height=4,width=10,font=("Helvetica",16,"bold"), command=lambda i=i: button_click(i)) for i in range(9)]
making_buttons_grid()

current_player = "X"

#adding menu with reset button 
menubar = tk.Menu(root)
menubar.add_cascade(label="Reset",command=lambda: reset_game())
root.config(menu=menubar)

#adding label at bottom to display player's turn
label = tk.Label(root,text = f"Player {current_player}'s Turn")
label.grid(row=3,column=0,columnspan=3)
root.mainloop()
