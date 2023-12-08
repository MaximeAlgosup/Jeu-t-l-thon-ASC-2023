from tkinter import *
from random import randrange

def move():
    global x, y, pX, pY
    global Serpent
    can.delete('all')  # Clear the canvas
    i = len(Serpent) - 1
    j = 0
    while i > 0:
        # Update the position of each segment in the snake
        Serpent[i][0] = Serpent[i - 1][0]
        Serpent[i][1] = Serpent[i - 1][1]
        # Draw each segment of the snake
        can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] + 10, Serpent[i][1] + 10, outline='red', fill='black')
        i = i - 1

    can.create_rectangle(pX, pY, pX + 5, pY + 5, outline='green', fill='black')  # Draw the food
    # Move the head of the snake based on the current direction
    if direction == 'gauche':
        Serpent[0][0] = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 493
    elif direction == 'droite':
        Serpent[0][0] = Serpent[0][0] + dx
        if Serpent[0][0] > 493:
            Serpent[0][0] = 0
    elif direction == 'haut':
        Serpent[0][1] = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = 493
    elif direction == 'bas':
        Serpent[0][1] = Serpent[0][1] + dy
        if Serpent[0][1] > 493:
            Serpent[0][1] = 0
    # Draw the head of the snake
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0] + 10, Serpent[0][1] + 10, outline='red', fill='yellow')
    test()
    test()

    if flag != 0:
        # Call the move function after a delay (animation)
        fen.after(120, move)

def newGame():
    global pX, pY
    global flag
    if flag == 0:
        flag = 1
    move()

def left(event):
    global direction
    direction = 'gauche'

def right(event):
    global direction
    direction = 'droite'

def up(event):
    global direction
    direction = 'haut'

def down(event):
    global direction
    direction = 'bas'

def test():
    global pomme
    global x, y, pX, pY
    global Serpent
    # Check if the head of the snake has collided with the food
    if Serpent[1][0] > pX - 7 and Serpent[1][0] < pX + 7:
        if Serpent[1][1] > pY - 7 and Serpent[1][1] < pY + 7:
            # Place a new food at a random position
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(pomme, pX, pY, pX + 5, pY + 5)
            # Add a new segment to the snake
            Serpent.append([0, 0])

x = 245
y = 24
dx, dy = 10, 10
flag = 0
direction = 'haut'
Serpent = [[x, y], [x + 2.5, y + 2.5], [x + 5, y + 5], [0, 0]]

pX = randrange(5, 495)
pY = randrange(5, 495)

fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=TOP, padx=5, pady=5)

oval1 = can.create_oval(Serpent[1][0], Serpent[1][1], Serpent[1][0] + 10, Serpent[1][1] + 10, outline='green', fill='red')

oval = can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0] + 10, Serpent[0][1] + 10, outline='green', fill='green')

pomme = can.create_rectangle(pX, pY, pX + 5, pY + 5, outline='green', fill='black')

b1 = Button(fen, text='Lancer', command=newGame, bg='black', fg='green')
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black', fg='green')
b2.pack(side=RIGHT, padx=5, pady=5)

tex1 = Label(fen, text="Cliquez sur 'New Game' pour commencer le jeu.", bg='black', fg='green')
tex1.pack(padx=0, pady=11)

fen.bind('<Right>', right)
fen.bind('<Left>', left)
fen.bind('<Up>', up)
fen.bind('<Down>', down)

fen.mainloop()
