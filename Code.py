import random
import sys
import tkinter as tk
from tkinter import ttk
import time
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

score = 0
movecount = 0

#I deleted this by accident, do not do that, this was so much harder than it looks
# opening the file (reading)
#setting writer to write to file and THEN you add in the new elements

def DataSaving():


    with open("database.csv", mode="a", newline="") as file:
          writer = csv.writer(file)
          writer.writerow([score, movecount])
    

def leavefunc():
    DataSaving()
    sys.exit()
    
#I did this so long ago I forget how it works
#adds a 2 to the grid
#No problems as of yet
#edit: added in the print statements, data saving

def AddTwo():
    global score
    global grid
    global movecount
    
    n = 15
    occupiedcount = 0
    #parse through the grid to find out how many are occupied
    for i in range(16):
            
        if grid[n] != 0:
            occupiedcount += 1
        n -= 1
        if occupiedcount == 16:
            print("GAME OVER!")
            print("Score: ", score)
            print("Moves: ", movecount)
            DataSaving()
            grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            score = 0
            movecount = 0
            MainMenu()
 
            
            sys.exit()
    
        
    rnum = random.randint(1, 16)
    while grid[rnum - 1] != 0:
        
        rnum = random.randint(1, 16)
        
    grid[rnum - 1] = 2
        
        
        
#TKINTER SETUP
#setup and basic static things like text and background image

# def MainWindow():
#     global root1
#     
#     root1 = tk.Tk()
#     root1.geometry("1150x817")
#     root1.title('2048!')
#     
#     #background image
#     bg_image = tk.PhotoImage(file="background colour.png")
#     bg_label = tk.Label(root1, image=bg_image)
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# 
#     #adding some cool text saying 2048
#     #text_label = tk.Label(root1, text="2048", font=("Arial", 50))
#     #text_label.place(x=1080, y=100, anchor="ne")
# 
#     #adding a logo instead
#     logo_image = tk.PhotoImage(file="2048-logo.png")
#     logo_label = tk.Label(root1, image=logo_image)
#     logo_label.place(x=830, y=10)
#     
#     root1.mainloop()

#root1.resizable(0, 0)

# MAIN MENU (MENU 1)

# root2 = tk.Tk()
# root2.geometry("300x300")
# root2.title('2048 Menu!')
# 
# qbutton = ttk.Button(root2, text="Quit", command= sys.exit)
# qbutton.place(x=50, y=50)


def DataMenu():
    
    root3 = tk.Tk()
    root3.geometry("500x500")
    root3.title('2048 Data Analysis!')

    qbutton = ttk.Button(root2, text="Quit", command= sys.exit)
    qbutton.place(x=50, y=50)

def MainMenu():
    
    grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    
    global root2

    root2 = tk.Tk()
    root2.geometry("300x400")
    root2.title('2048 Menu!')
    root2.configure(bg="#faf8ef")
    #root2[background]="#bbada0"    

    score_label = tk.Label(root2, text="2048!", font=("Tanseek Modern Arabic Medium", 45, "bold"), background = '#faf8ef', fg= "#776e65")
    score_label.place(x=70, y=30, anchor="nw")

    SinglePlayerbutton = ttk.Button(root2, text="Singleplayer", command= Singleplayer)
    SinglePlayerbutton.place(x=110, y=150)  

    MultiPlayerbutton = ttk.Button(root2, text="Multiplayer", command= Multiplayer)
    MultiPlayerbutton.place(x=110, y=200)
    
    Computerbutton = ttk.Button(root2, text="Computer", command= Computerplayer)
    Computerbutton.place(x=110, y=250)

    Databutton = ttk.Button(root2, text="Analyse Data", command= DataMenu)
    Databutton.place(x=110, y=300)
    
    q2button = ttk.Button(root2, text="Quit", command= sys.exit)
    q2button.place(x=110, y=350)

    root2.mainloop()
    
def DataMenu():
    root2 = tk.Tk()
    root2.geometry("300x350")
    root2.title('Data Analysis!')
    root2.configure(bg="#faf8ef")
    
    score_label = tk.Label(root2, text="Analyse Data!", font=("Tanseek Modern Arabic Medium", 15, "bold"), background = '#faf8ef', fg= "#776e65")
    score_label.place(x=70, y=30, anchor="nw")
    
    graph_label = tk.Label(root2, text="Moves Taken vs. Score Graph", font=("Tanseek Modern Arabic Medium", 10, "bold"), background = '#faf8ef', fg= "#776e65")
    graph_label.place(x=35, y=75, anchor="nw")
    
    Graphbutton = ttk.Button(root2, text="Scatter", command= PlotData)
    Graphbutton.place(x=110, y=100)  

    graph_label = tk.Label(root2, text="Moves Made and Score Averages", font=("Tanseek Modern Arabic Medium", 10, "bold"), background = '#faf8ef', fg= "#776e65")
    graph_label.place(x=20, y=150, anchor="nw")

    AVGbutton = ttk.Button(root2, text="Averages", command= PrintAverages)
    AVGbutton.place(x=110, y=175)
    
    mm1button = ttk.Button(root2, text="Main Menu", command= MainMenu)
    mm1button.place(x=110, y=225)
    
    q3button = ttk.Button(root2, text="Quit", command= sys.exit)
    q3button.place(x=110, y=275)
    
def ScoringSystem():
    
#     for i in grid:
#         score = score + grid[i]
        
        
#     score = str(score)

    score_label = tk.Label(root1, text="Score: " + str(score), font=("Tanseek Modern Arabic Medium", 20, "bold"), background = '#faf8ef', fg= "#776e65")
    score_label.place(x=915, y=200, anchor="nw")



# BETTER PRINT GRID?? image functonailty and dictionary usage unironically?
def PrintGrid():
    label = None
    
    image_dict = {0: '2048-0-final.png', 2: '2048-2-final.png', 4: '2048-4-final.png', 8: '2048-8-final.png', 16: '2048-16.png',
                  32: '2048-32-final.png', 64: '2048-64-final.png', 128: '2048-128-final.png', 256: '2048-256-final.png',
                  512: '2048-512.png', 1024: '2048-1024.png', 2048: '2048-2048.png'}
    #mapping numbers to image files for easy access
    
    if label != None:
        #optimisation! => deletes previous image grid so it doesnt crash after 500 or so clicks
        for lbl in label.grid_slaves():
            lbl.grid_forget()
        
    #creates image grid, refreshes constantly, not optimal but functional
    # note: very problematic section
    #cannot get rid of padding padx=0 pady=0 doesnt work
    for row in range(4):
        for col in range(4):
            number = grid[row*4 + col]
            image = tk.PhotoImage(file=image_dict[number])
            label = tk.Label(root1, image=image)
            label.image = image
            label.grid(row=row, column=col)
            
    
            

#genius 500iq logic (works perfectly)
            
def CombiningLogic(u, i, o, p):
    global score
    if grid[o] == grid[p]:
        grid[p] = grid[o] + grid[p]
        grid[o] = 0
        score += grid[p]
        
    if grid[i] == grid[o]:
        grid[o] = grid[o] + grid[i]
        grid[i] = 0
        score += grid[o]
    
    if grid[u] == grid[i]:
        grid[i] = grid[u] + grid[i]               
        grid[u] = 0
        score += grid[i]
        
                
def MovingLogic(u, i, o, p):
    if grid[i] == 0 and grid[u] > 0:
        grid[i] = grid[u]
        grid[u] = 0
            
    if grid[o] == 0 and grid[i] > 0:
        grid[o] = grid[i]
        grid[i] = 0
            
    if grid[p] == 0 and grid[o] > 0:
        grid[p] = grid[o]
        grid[o] = 0

#kinda a lazy solution, extra functions that take the funcs that were at the end of w/a/s/dfunc so I can call them without calling AddTwo() etc
#necessary cuurently for the greedy alg stuff to work
#also did the same for combining logic
#the code was so tidy before -_-
        

def wfunc2():
    global movecount
    movecount += 1
    wfunc()
    PrintGrid()
    AddTwo()
    ScoringSystem()
    
def afunc2():
    global movecount
    movecount += 1
    afunc()
    PrintGrid()
    AddTwo()
    ScoringSystem()
    
def sfunc2():
    global movecount
    movecount += 1
    sfunc()
    PrintGrid()
    AddTwo()
    ScoringSystem()
    
def dfunc2():
    global movecount
    movecount += 1
    dfunc()
    PrintGrid()
    AddTwo()
    ScoringSystem()

#calls all the logic functions to be coherent with the web game
#umm theres def a better way to do this
#use classes???!?!
#NEW AND IMPROVED! now they have gone through so manay iterations that they are fucking incomprehensible now in terms of layered complexity
#so hopefully they dont break
#see screenshots in lccsproj folder for reverse engineer fingers crossed there will be no need to do that
    
def wfunc():
    n=16
    for i in range(4):
        for i in range(5):
            if i != 3:
                MovingLogic(n-1, n-5, n-9, n-13)
                
                
            if i == 3:
                CombiningLogic(n-1, n-5, n-9, n-13)
                
        n -= 1
        

def afunc():
    n=16
    for i in range(4):
        for i in range(5):
            if i != 3:
                MovingLogic(n-1, n-2, n-3, n-4)
                
                
            if i == 3:
                CombiningLogic(n-1, n-2, n-3, n-4)
                
        n -= 4
    

    
def sfunc():
    n=16
    for i in range(4):
        for i in range(5):
            if i != 3:
                MovingLogic(n-13, n-9, n-5, n-1)
                
                
            if i == 3:
                CombiningLogic(n-13, n-9, n-5, n-1)
                
        n -= 1
 

    
def dfunc():
    n=16
    for i in range(4):
        for i in range(5):
            if i != 3:
                MovingLogic(n-4, n-3, n-2, n-1)
                
                
            if i == 3:
                CombiningLogic(n-4, n-3, n-2, n-1)
                
        n -= 4
        
    
    
#buttons for controlling the game, note wfunc not wfunc() and sys.exit not sys.exit() for the future
    
def tkintersection():
    
    global root1
    
    root1 = tk.Tk()
    root1.geometry("1150x817")
    root1.title('2048!')
    
    #background image
    bg_image = tk.PhotoImage(file="background colour.png")
    bg_label = tk.Label(root1, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #adding some cool text saying 2048
    #text_label = tk.Label(root1, text="2048", font=("Arial", 50))
    #text_label.place(x=1080, y=100, anchor="ne")

    #adding a logo instead
    logo_image = tk.PhotoImage(file="2048-logo.png")
    logo_label = tk.Label(root1, image=logo_image)
    logo_label.place(x=830, y=10)
    
    #root1.mainloop()
    
    #print("test1")
    #PrintGrid()
    #AddTwo()
    #w_image = tk.PhotoImage(file='2048-2048.png')
    
    wbutton = ttk.Button(root1, text="UP", command= wfunc2)
    wbutton.place(x=935, y=558)
    #wbutton.bind("<Button-1>", wfunc)
    #wbutton.grid(column=8, row=1, padx=5, pady=5)
    #wbutton.config(image = w_image)
    #wbutton.pack()

    abutton = ttk.Button(root1, text="LEFT", command= afunc2)
    abutton.place(x=835, y=585)
    #abutton.grid(column=7, row=2, padx=5, pady=5)
    

    sbutton = ttk.Button(root1, text="DOWN", command= sfunc2)
    sbutton.place(x=935, y=615)
    #sbutton.grid(column=8, row=2, padx=5, pady=5)

    dbutton = ttk.Button(root1, text="RIGHT", command= dfunc2)
    dbutton.place(x=1035, y=585)
    #dbutton.grid(column=9, row=2, padx=5, pady=5)
    
    qbutton = ttk.Button(root1, text="Quit", command= leavefunc)
    qbutton.place(x=935, y=750)
    #qbutton.grid(column=8, row=3, padx=5, pady=5)
    
    #print("test2")
    
    root1.mainloop()
 
#AI!??!?
#"greedy" algorithm
#what am I doing! help!
#dict to control the options???? good idea????
#new plan => random moves
    
def MakeMove():
    global movecount
    randint = random.randint(1, 4)
    
    if randint == 1:
        wfunc()
        
    elif randint == 2:
        afunc()
        
    elif randint == 3:
        sfunc()
        
    else:
        dfunc()

    movecount += 1
        
    #root1.update()

randint4 = random.randint(1, 4)
def Hypothesis2():
    if randint == 1:
        wfunc()
        
    elif randint == 2:
        afunc()
        
    elif randint == 3:
        sfunc()
        
    else:
        dfunc()

    movecount += 1
        
    
    
    

# def Simulation1():
#     time.sleep(1)
#     
#     AddTwo()
#     rn = random.randint(1, 4)
#     if rn == 1:
#         afunc()
#         
#     if rn == 2:
#         wfunc()
#         
#     if rn == 3:
#         sfunc()
#         
#     if rn == 4:
#         dfunc()
#         
#     movecount += 1
#         
#     PrintGrid()
        
#basic grid for the simulation
def PrintGrid2():
    print(grid[0], grid[1], grid[2], grid[3])
    print(grid[4], grid[5], grid[6], grid[7])
    print(grid[8], grid[9], grid[10], grid[11])
    print(grid[12], grid[13], grid[14], grid[15])
    print(" ")

#Analyses the data, mean median and mode
def DataAnalysis():
    df = pd.read_csv('database.csv')
    sum_scores = df['Scores'].sum()
    sum_moves = df['Num_Moves'].sum()

    mean_scores = df['Scores'].mean()
    mean_moves = df['Num_Moves'].mean()
    median_scores = df['Scores'].median()
    median_moves = df['Num_Moves'].median()
    mode_scores = df['Scores'].mode()
    mode_moves = df['Num_Moves'].mode()
    
    
#     rows  = 0
#     for rows in open("Data.csv"):
#         rows+= 1
#     
#     mean_scores = sum_scores / rows
#     mean_moves = sum_moves / rows
#    print("""

#         Mean  Median  Mode
#Scores: {mean_scores}  {median_scores}  {mode_scores}
# Moves:
    
#Plots a scattergraph using numpy
def PlotData():
    df = pd.read_csv('database.csv')
    xpts = np.array(df["Scores"])
    ypts = np.array(df["Num_Moves"])

    plt.scatter(xpts, ypts)
    plt.xlabel("Scores")
    plt.ylabel("Number of Moves Made")
    plt.show()

#Shows the averages
def PrintAverages():
    
    df = pd.read_csv('database.csv')
    sum_scores = df['Scores'].sum()
    sum_moves = df['Num_Moves'].sum()
    
    mean_scores = df['Scores'].mean()
    mean_moves = df['Num_Moves'].mean()
    median_scores = df['Scores'].median()
    median_moves = df['Num_Moves'].median()
    mode_scores = df['Scores'].mode()
    mode_moves = df['Num_Moves'].mode()
    
    print("<= Average Scores = >")
    print("Mean: ", mean_scores)
    print("Median: ", median_scores)
    print("Modes: ", mode_scores)
    
    print(" ")
    
    print("<= Average Move Counts = >")
    print("Mean: ", mean_moves)
    print("Median: ", median_moves)
    print("Modes: ", mode_moves)
  
#Starts SIngleplayer
def Singleplayer():
    root2.destroy()
    #MainWindow()
    AddTwo()
    #PrintGrid()
    tkintersection()
    PrintGrid()

    while True:
        PrintGrid()
        root1.mainloop()

#Starts Multiplayer
def Multiplayer():
    counter = 1
    print("Take turns to play!")
    
    root2.destroy()
    #MainWindow()
    AddTwo()
    #PrintGrid()
    tkintersection()
    PrintGrid()

    while True:
            
        PrintGrid()
        root1.mainloop()
        
        if counter == 1:
            turn_label = tk.Label(root1, text="Player 1's Turn", font=("Tanseek Modern Arabic Medium", 20, "bold"), background = '#faf8ef', fg= "#776e65")
            turn_label.place(x=915, y=0, anchor="nw")
            counter = 2
            
        else:
            print("Player 1's turn")
            counter = 1

#Starts the simulation
def Computerplayer():
    root2.destroy()
    #ComputerWindow()
    #tkintersection()
    AddTwo()    

    while True:
        MakeMove()
        #print("exited")
        PrintGrid2()
        AddTwo()
        time.sleep(0.1)
        
    



#START
#Box Ticking
#Start of the program, asks for inputs

user_name = "1"
while user_name.isalpha() == False:
    user_name = str(input("Please enter your name, (latin alphabet only): "))

user_age = "A"
while user_age.isnumeric() == False:
    user_age = str(input("Please enter your age, (numbers only): "))

user_start = ""
while user_start != "yes" and "no":
    user_start = str(input("Would you like to start? - (yes/no) - "))

MainMenu()





#PrintGrid()
#PrintGrid2()
#tkintersection()
#AddTwo()

#while True:
    #PrintGrid()
    #PrintGrid2()
    #tkintersection()
    #AddTwo()
    #MakeMove()
    
    #root1.mainloop()
    
    
    
    #time.sleep(0.01)
    

#questions for someone smart:
#how to get rid of padx and y??? why is it there???
    
    
    
