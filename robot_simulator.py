# Robot Command Simulator

x = 0
y = 0
direction = "NORTH"

def move_forward():
    global x, y, direction
    if direction == "NORTH":
        y += 1
    elif direction == "SOUTH":
        y -= 1
    elif direction == "EAST":
        x += 1
    elif direction == "WEST":
        x -= 1

def move_backward():
    global x, y, direction
    if direction == "NORTH":
        y -= 1
    elif direction == "SOUTH":
        y += 1
    elif direction == "EAST":
        x -= 1
    elif direction == "WEST":
        x += 1

def turn_left():
    global direction
    if direction == "NORTH":
        direction = "WEST"
    elif direction == "WEST":
        direction = "SOUTH"
    elif direction == "SOUTH":
        direction = "EAST"
    elif direction == "EAST":
        direction = "NORTH"

def turn_right():
    global direction
    if direction == "NORTH":
        direction = "EAST"
    elif direction == "EAST":
        direction = "SOUTH"
    elif direction == "SOUTH":
        direction = "WEST"
    elif direction == "WEST":
        direction = "NORTH"

while True:
    command = input("Enter command (FORWARD, BACKWARD, LEFT, RIGHT, STOP): ").upper()

    if command == "FORWARD":
        move_forward()
    elif command == "BACKWARD":
        move_backward()
    elif command == "LEFT":
        turn_left()
    elif command == "RIGHT":
        turn_right()
    elif command == "STOP":
        print("Simulation stopped.")
        break
    else:
        print("Invalid command!")

    print(f"Position: ({x}, {y}), Direction: {direction}")
