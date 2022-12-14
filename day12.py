import copy

day12input = open("./day12small.txt", "r" )
output = day12input.read()
day12input.close()

def setup_squares(square_char):
    return ord(square_char)

topo = [ [setup_squares(x) for x in list(y)] for y in output.split('\n') if y != ""]
map_history = [[ False for _ in range(len(topo[0]))] for _ in range(len(topo))]


map_height = len(topo)
map_width = len(topo[0])
print(map_height)
for y, row in enumerate(topo):
    for x, col in enumerate(row):
        if col == 83:
            topo[y][x] = 97
            # print("Start")
            start ={"y":y,"x":x}
            
        elif col == 69:
            # print("End")
            topo[y][x] = 122
            end ={"y":y,"x":x }


def print_map(map):
    for row in map:
        row_output = "|"
        for col in row:
            if col:
                row_output += "#"
            else:
                row_output += " "
        row_output += "|"
        print(row_output)
            
    
def take_a_step(topo_map, position, map_history, count = 0, direction=" "):
    y = position["y"]
    x = position["x"]
    
    # if topo_map[y][x] == 101:    
    if x == end["x"] and y == end["y"]:
        print("found end")
        paths.append(count)
        return count

    if map_history[y][x]:
        return 0

    map_history[y][x] = True
    
    
    if count > 200 and topo_map[y][x] < 100:
        return 0
    
    if len(sorted(paths)) > 0 and sorted(paths)[0] < count:
        return 0
    
    print(sorted(paths))
    print(f'====== {count}, {direction} ======')
    print_map(map_history)

    count += 1
    
    if (x+1 < map_width) and abs(topo_map[y][x+1] - topo_map[y][x]) <= 1:
        take_a_step(topo_map, {"y": y, "x": x+1}, copy.deepcopy(map_history), count, direction=">" )

    if (y+1 < map_height) and abs(topo_map[y+1][x] - topo_map[y][x]) <= 1 :
        take_a_step(topo_map, {"y": y + 1, "x": x}, copy.deepcopy(map_history), count, direction="V" )
    
    if (y-1 >= 0) and abs(topo_map[y-1][x] - topo_map[y][x]) <= 1:
        take_a_step(topo_map, {"y": y-1, "x": x}, copy.deepcopy(map_history), count, direction="^" )
    
    if (x-1 >= 0) and abs(topo_map[y][x-1] - topo_map[y][x]) <= 1:
        take_a_step(topo_map, {"y": y, "x":x-1}, copy.deepcopy(map_history), count, direction="<" )

paths = []

take_a_step(topo, position=start, map_history=copy.deepcopy(map_history))

print(sorted(paths))
    

# >>> ord("S")
# 83
# >>> ord("a")
# 97
# >>> ord("z")
# 122
# >>> ord("E")
# 69