import copy

def move_h(direction):
    if direction == "L":
        h_position["x"] -= 1
    if direction == "R":
        h_position["x"] += 1
    if direction == "U":
        h_position["y"] += 1
    if direction == "D":
        h_position["y"] -= 1

def move_knot(following, current):
    # same horizontal position
    if following["x"] == current["x"]:
        if (abs(following["y"] - current["y"]) > 1) and (following["y"] > current["y"]):
            current["y"] += 1
        if (abs(following["y"] - current["y"]) > 1) and (following["y"] < current["y"]):
            current["y"] -= 1
                        
    # same virtical position 
    if following["y"] == current["y"]:
        if (abs(following["x"] - current["x"]) > 1) and (following["x"] > current["x"]):
            current["x"] += 1
        if (abs(following["x"] - current["x"]) > 1) and (following["x"] < current["x"]):
            current["x"] -= 1

    #diagonally okay
    if (abs(following["x"] - current["x"]) <= 1) and (abs(following["y"] - current["y"]) <= 1):
        return current
     
    #diagonally not okay
    if following["x"] < current["x"]:
        current["x"] -= 1
        
    elif following["x"] > current["x"]:
        current["x"] += 1
        
    if following["y"] < current["y"]:
        current["y"] -= 1
    elif following["y"] > current["y"]:
        current["y"] += 1
    
    return current
    
day9input = open("./day9input.txt", "r" )
output = day9input.read()
day9input.close()
instructions = [ [ x.split(" ")[0], int(x.split(" ")[1])] for x in output.split('\n') if x != ""]

h_position = {"x":0, "y":0}

t_position = {"x":0,"y":0,}
t_history = []
b_pos = [{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,}]


for x in instructions:
    for step in range(x[1]):
        move_h(x[0])
        move_knot(h_position, b_pos[0])
        for i in range(1,8):
            move_knot(b_pos[i-1],b_pos[i])
        
        t_history.append(copy.deepcopy(move_knot(b_pos[7],t_position)))


unique_locations = []
for location in t_history:
    if location not in unique_locations:   
        unique_locations.append(location)      

print("----p1 & 2------")
print(len(unique_locations))


