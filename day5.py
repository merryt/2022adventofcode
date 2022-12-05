import copy

def process_row(row):
    row_arr = []
    for i in range(1, 36, 4):
        row_arr.append(row[i])
    return row_arr

def process_instruction(x):
    instruction_array = x.split(' ')
    return {
            "qty":int(instruction_array[1]),
            "origin": int(instruction_array[3]),
            "destination": int(instruction_array[5]),
            }
    
def move_create(instruction, stack_of_boxes, new_crane=False):
    if instruction["qty"] == 0:
        return
    
    #grab size is always negitive because we are pulling from top of stack
    if(new_crane):
        grab_size = -1 * instruction["qty"] 
    else:
        grab_size = -1
        
    # origin and destination have to be `-1` to offset 0 based index
    boxes_to_move = stack_of_boxes[instruction["origin"] -1][grab_size:] # grab block with crane
    stack_of_boxes[instruction["origin"] -1] = stack_of_boxes[instruction["origin"] -1][0:grab_size] # remove blocks from old tower
    stack_of_boxes[instruction["destination"] -1] = stack_of_boxes[instruction["destination"] -1] + boxes_to_move # drop block off on new location
    
    if(new_crane):
        return 
    else:
        move_create({
                "qty": instruction["qty"] -1,
                "origin": instruction["origin"],
                "destination": instruction["destination"],
                }, stack_of_boxes, new_crane)
            
day5input = open("./day5input.txt", "r" )
output = day5input.read()
sections = [ x for x in output.split('\n\n') if x != ""]

initial_chart = sections[0]
intructions = sections[1]

print(initial_chart)
rotated_towers = [ process_row(x) for x in initial_chart.split('\n') if x != ""]

tower = [[]]*9
for row in rotated_towers:
    for col_index, item in enumerate(row):
        if(item != " "):
            tower[col_index] = [item] + tower[col_index]


instructions = [ process_instruction(x) for x in intructions.split('\n') if x != "" ]

tower2 = copy.deepcopy(tower)
for instruction in instructions:
    move_create(instruction, tower)

for instruction in instructions:
    move_create(instruction, tower2, True)
    
print("----p1------")
for column in tower:
    print(column[-1])

print("----p2------")
for column in tower2:
    print(column[-1])

day5input.close()