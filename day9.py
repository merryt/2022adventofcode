import copy


def move_knot(following, current):
    """
    TODO: work on tracking the tail 
    """
    
    # same horizontal position
    if following["x"] == current["x"]:
        if (abs(following["y"] - current["y"]) > 1) and (following["y"] > current["y"]):
            current["y"] += 1
        if (abs(following["y"] - current["y"]) > 1) and (following["y"] < current["y"]):
            current["y"] -= 1
        return current
        # t_history.append(copy.deepcopy(current))
        
            
            
    # same virtical position 
    if following["y"] == current["y"]:
        if (abs(following["x"] - current["x"]) > 1) and (following["x"] > current["x"]):
            current["x"] += 1
        if (abs(following["x"] - current["x"]) > 1) and (following["x"] < current["x"]):
            current["x"] -= 1
        return current
        # t_history.append(copy.deepcopy(current))

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
    # t_history.append(copy.deepcopy(current))
    
    
    
    
    
    
    
    

def move_h(direction):
    if direction == "L":
        h_position["x"] -= 1
    if direction == "R":
        h_position["x"] += 1
    if direction == "U":
        h_position["y"] += 1
    if direction == "D":
        h_position["y"] -= 1

"""
hotplate
"""
day9input = open("./day9small.txt", "r" )
output = day9input.read()
day9input.close()
instructions = [ [ x.split(" ")[0], int(x.split(" ")[1])] for x in output.split('\n') if x != ""]

h_position = {"x":0, "y":0}

t_position = {"x":0,"y":0,}
t_history = []
b_pos =  [{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,},{"x":0,"y":0,}]


for x in instructions:
    for step in range(x[1]):
        move_h(x[0])

        t_history.append(copy.deepcopy(move_knot(h_position,t_position)))
        
        # print("----post head & tail move----")
        # print(h_position)
        # print(t_position)
        # print("--------")


unique_locations = []
for location in t_history:
    if location not in unique_locations:   
        unique_locations.append(location)
        





print("----p1------")
print(len(unique_locations))

print("----p2------")
# print(bestview)


