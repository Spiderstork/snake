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
    accept = False
    while accept == False:
        spot = [random.randint(0,12), random.randint(0,29)]

        # makes sure the apple doesnt spawn on snake
        if spot in snake_spots:
            accept = False

        else:
            apples.append(spot)
            screen[spot[0]][spot[1]] = "\33[41m \33[0m"
            accept = True

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
    if (snake_spots[-1][0] < 13 and snake_spots[-1][0] > 0) and (snake_spots[-1][1] < 30 and snake_spots[-1][1] > 0):

        # moves the snake to the last key presses direction
        if direction == "left":
            snake_spots.append([snake_spots[-1][0],snake_spots[-1][1]-1])

        if direction == "right": 
            snake_spots.append([snake_spots[-1][0],snake_spots[-1][1]+1])
        
        if direction == "up":
            snake_spots.append([snake_spots[-1][0]-1,snake_spots[-1][1]])
        
        if direction == "down":
            snake_spots.append([snake_spots[-1][0]+1,snake_spots[-1][1]])
        
        try:
            # changes the last snake spot back to green
            screen[snake_spots[0][0]][snake_spots[0][1]] = "\33[42m \33[0m"
            snake_spots.pop(0)
        except:
            pass
        
        try:
            # put the snakes new spot on the screenw
            for pixel in snake_spots:
                screen[pixel[0]][pixel[1]] = "\33[43m \33[0m"
        except:
            pass
        
        
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
    for pixel in screen:
        for cords in pixel:
            print(cords, end="")
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