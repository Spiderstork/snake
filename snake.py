import random
import msvcrt
import time
import os

screen = [["\33[42m \33[0m" for _ in range(30)] for _ in range(13)]
snake_spots = [[2,15]]
apples = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_item():
    spot = [random.randint(0,12), random.randint(0,29)]
    apples.append(spot)
    screen[spot[0]][spot[1]] = "\33[41m \33[0m"
    return screen

def eat():
    for apple in apples:
        # compares snakes head to all the apples to find overlaps
        if snake_spots[-1][0] == apple[0] and snake_spots[-1][1] == apple[1]:
            # increas snakes length
            snake_spots.insert(0,[snake_spots[0][0],snake_spots[0][1]])
            apples.remove(apple)
            # spawns in the new apple
            new_item()

def snake(direction):
    # checks snake is within the box
    if (snake_spots[-1][0] <= 13 and snake_spots[-1][0] >= 0) and (snake_spots[-1][1] <= 30 and snake_spots[-1][1] >= 0):

        # moves the snake to the last key presses direction
        if direction == "left":
            snake_spots.append([snake_spots[-1][0],snake_spots[-1][1]-1])

        if direction == "right": 
            snake_spots.append([snake_spots[-1][0],snake_spots[-1][1]+1])
        
        if direction == "up":
            snake_spots.append([snake_spots[-1][0]-1,snake_spots[-1][1]])
        
        if direction == "down":
            snake_spots.append([snake_spots[-1][0]+1,snake_spots[-1][1]])
        
        # changes the last snake spot back to green
        screen[snake_spots[0][0]][snake_spots[0][1]] = "\33[42m \33[0m"
        snake_spots.pop(0)
        # put the snakes new spot on the screenw
        for n in snake_spots:
            screen[n[0]][n[1]] = "\33[43m \33[0m"
        
        clear_console()
        new_screen()
    
    else:
        clear_console()
        print("you died!!")
        print("press enter to restart")
        input()

def controls(direction):
    # check if any key is pressed
    if msvcrt.kbhit():
        # saves the key what is pressed to compare with character
        key = msvcrt.getch()

        # compares key with direction to tell the snake what direction to go
        if key == b'w':
            direction = 'up'
        if key == b's':
            direction = 'down'
        if key == b'a':
            direction = 'left'
        if key == b'd':
            direction = 'right'
    
    return direction

    

def new_screen():
    for n in screen:
        for c in n:
            print(c,end="")
        print()

# sets up first apple
new_item()
direction = "left"

# new frame
while True:
    eat()
    direction = controls(direction)
    snake(direction)
    time.sleep(0.5)