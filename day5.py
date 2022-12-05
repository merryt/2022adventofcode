
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
    
def move_create(instruction):
    if instruction["qty"] == 0:
        return
    
    # origin and destination have to be `-1` to offset 0 based index
    number_to_move = tower[instruction["origin"] -1][-1] # grab block with crane
    tower[instruction["origin"] -1] = tower[instruction["origin"] -1][0:-1] # remove block from old tower
    tower[instruction["destination"] -1].append(number_to_move) # drop block off on new location
    move_create({
            "qty": instruction["qty"] -1,
            "origin": instruction["origin"],
            "destination": instruction["destination"],
            })
            
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

print("---")

# move 5 from 3 to 6
instructions = [ process_instruction(x) for x in intructions.split('\n') if x != "" ]

for instruction in instructions:
    move_create(instruction)

print(tower)

print("\n----Part 1-----")
print("-")


print("----Part 2-----")
print("-")


day5input.close()