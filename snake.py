import numpy
from pynput.keyboard import Key, Listener
import threading
import time
import os
import random

def genMatrix(size):
    matrix = numpy.zeros((size,size), dtype=str)    
    for y in range(size):
        for x in  range(size):
            matrix[y][x] = "."    
    return matrix

def printTable(Matrix):
    for y in Matrix:
        for x in y:
            print(x, end=" ")
        print(end="\n")

def keyBoardInput(list):
    def on_press(key):
        KeyAvaible = [Key.up, Key.down, Key.left, Key.right,Key.esc]
        if key in KeyAvaible:
            list.append(key)
    
    def on_release(key):
        if key == Key.esc:
            return False
    
    listener = Listener( on_press=on_press,on_release=on_release)
    listener.start()
     
def cleanTable(Matrix, size):
    for y in range(size):
        for x in  range(size):
            Matrix[y][x] = "."

def addTable(Matrix, cords, body):
    try:
        for cord in cords:
            if cord[1] < 0 or cord[0] < 0:
                return False
            Matrix[cord[1]][cord[0]] = body
        return True
    except IndexError:
        return False

def endGame(points):
    print("\n")
    print("Puntaje  ", points)
    print("\n")
    print("\n")
    print("  /$$$$$$                                           /$$$$$$                                \n"
          " /$$__  $$                                         /$$__  $$                               \n"
          "| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$  /$$$$$$   /$$$$$$ \n"
          "| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$/ /$$__  $$ /$$__  $$\n"
          "| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/ | $$$$$$$$| $$  \__/\n"
          "| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/  | $$_____/| $$      \n"
          "|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/   |  $$$$$$$| $$      \n"
          " \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/     \_______/|__/      ")
    print("\n")
    print("\n")

def game(size):
    
    table = genMatrix(size)
    snakeCords = [[0,int(size/2)]]
    direction = Key.right
    point = 0
    foodCord = [[random.randint(0,size-1), random.randint(0,size-1)]]
    aux = None

    while foodCord[0] in snakeCords:
        foodCord = [[random.randint(0,size-1), random.randint(0,size-1)]]

    while addTable(table, snakeCords, "■"):

        addTable(table, foodCord, "☀")

        os.system('cls')
        printTable(table)        

        if len(keyInput) != 0:
            yDirections = [Key.up, Key.down]
            xDirections = [Key.right, Key.left]
            key = keyInput.pop(0)
            
            if key == Key.esc:
                break
            
            if not (key in yDirections and direction in yDirections) and not(key in xDirections and direction in xDirections):
                direction = key
            
        if direction == Key.right:
            aux = snakeCords[0]
            snakeCords[0] = [snakeCords[0][0]+1, snakeCords[0][1]] 
        elif direction == Key.down:
            aux = snakeCords[0]
            snakeCords[0] = [snakeCords[0][0], snakeCords[0][1]+1]  
        elif direction == Key.left:
            aux = snakeCords[0]
            snakeCords[0] = [snakeCords[0][0]-1, snakeCords[0][1]] 
        elif direction == Key.up:
            aux = snakeCords[0]
            snakeCords[0] = [snakeCords[0][0], snakeCords[0][1]-1]  


        for i in range(len(snakeCords)-1):
            aux2 = aux
            aux = snakeCords[i+1]
            snakeCords[i+1]  = aux2


        if snakeCords[0] == foodCord[0]:
            snakeCords.append(aux)
            point+=1
            foodCord = [[random.randint(0,size-1), random.randint(0,size-1)]]
            while foodCord[0] in snakeCords:
                foodCord = [[random.randint(0,size-1), random.randint(0,size-1)]]
        
        if snakeCords.count(snakeCords[0]) >= 2:
            break
        
        cleanTable(table,size)
        
        time.sleep(0.1)
    
    endGame(point)
        
keyInput = []

thread = threading.Thread(target=keyBoardInput, kwargs={'list':keyInput}) 
thread.start()

game(20)