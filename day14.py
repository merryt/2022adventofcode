
file = open("./day14small.txt", "r" )
output = file.read()
file.close()

rock_features = [ [[int(z) for z in x.strip().split(",")] for x in y.split('->')] for y in output.split('\n') if y != ""]
print(rock_features)

section_height_min = 0

for rock_feature in rock_features:
    for segment in rock_feature:
        x = segment[0]
        y = segment[1]
        
        if "section_height_max" not in locals():
            section_height_max = y
        if "section_width_max" not in locals():
            section_width_max = x
        if "section_width_min" not in locals():
            section_width_min = x
        
        
        if y > section_height_max:
            section_height_max = y
        if x > section_width_max:
            section_width_max = x
        if x < section_width_min:
            section_width_min = x

        #draw lines onto map
        




cave_map = [[ "." for _ in range(section_width_min, section_width_max+1)] for _ in range(section_height_min, section_height_max+1)]

for rock_feature in rock_features:
    for i, segment in enumerate(rock_feature):
        x1 = segment[0]
        y1 = segment[1]
        
        cave_map[y1-section_height_min][x1-section_width_min] = "X"

        if i < len(rock_feature)-1:
            next_segment = rock_feature[i+1]
            x2 = next_segment[0]
            y2 = next_segment[1]
            if x1 == x2:
                #edge is going vertical
                if y1 < y2:
                    for y in range(y1, y2):
                        cave_map[y-section_height_min][x1-section_width_min] = "X"
                else:
                    for y in range(y2, y1):
                        cave_map[y-section_height_min][x1-section_width_min] = "X"
            if y1 == y2:
                #edge is going horizontal
                if x1 < x2:
                    for x in range(x1, x2):
                        cave_map[y1-section_height_min][x-section_width_min] = "X"
                else:
                    for x in range(x2, x1):
                        cave_map[y1-section_height_min][x-section_width_min] = "X"


sand_starting_location = {"y": 0,"x": 500}
cave_map[sand_starting_location["y"]][sand_starting_location["x"]-section_width_min] = "+"




def print_map():
    for row in cave_map:
        row_output = "|"
        for col in row:
            row_output += col
        row_output += "|"
        print(row_output)



