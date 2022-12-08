fs = {
    # 999999999 : {
    # "id": 123123,
    # "name": "sample_name",
    # "children": [], 
    # "parent": 100
    # }
}
current_id = 1


def parse_line(line, pos = "?"):
    if line[0] == "$":
        pos = process_command(line, pos)
    elif line[0].isdigit():
        pos = process_file(line, pos)
    elif line[0:3] == "dir":
        pos = process_dir(line, pos)
    else:
        print("Error!!!")
        print(line)
    
    return pos

def process_command(line, old_pos):
    command = line[2:4]
    line_with_out_dollar = line[2:]
    new_pos = ""
    
    # changing directory
    if command == "cd":
        dir = line_with_out_dollar[3:]
        
        
        if dir != "..":
            # TODO: figure out a better way to do id generation
            current_id = len(fs) 
            if dir == "/":
                old_pos = "fs"
            else:
                for sib in fs[old_pos]["children"]:
                    if sib["name"] == dir:
                        sib["id"] = current_id
            fs[current_id] = {
                "id": current_id,
                "name": dir,
                "parent": old_pos,
                "children": [],
                "type": "dir",
                "size": None
            }
            new_pos = current_id
            
        elif dir == "..":
            # TODO: work out how ... will work... oooph 
            """ good luck """
            new_pos = fs[old_pos]["parent"]
        else:
            print("changing directories to something weird")
    
    if command == "ls":
        """
            in this puzzle ls is worthless I guess.....
        """
    
    if type(new_pos) == int:
        return new_pos
    
    return old_pos

def process_file(line, pos):
    split_line = line.split(" ") 
    fs[pos]["children"].append({
        "name": split_line[1],
        "size": int(split_line[0]), 
        "type": "file"
    })
    return pos

def process_dir(line, pos):
    split_line = line.split(" ") 
    fs[pos]["children"].append({
        "name": split_line[1],
        "type": "dir",
        "id": None
    })
    return pos


def populate_sizes(id, current_size=0):
    for child in fs[id]["children"]:
        if child["type"] == "file":
            current_size = current_size + child["size"]
        else:
            current_size = current_size + populate_sizes(child["id"])
        
    fs[id]["size"] = current_size
    
    return current_size
    





"""
hot plate
"""
day7input = open("./day7input.txt", "r" )
output = day7input.read()
day7input.close()
lines = [ x for x in output.split('\n') if x != ""]


current_pos = "1"
for line in lines:
    current_pos = parse_line(line, current_pos)

populate_sizes(0)

p1Answer = 0
more_flatter_file_structure = []

for k, v in fs.items():
    more_flatter_file_structure.append(v)
    if v["size"] > 100000:
        """print('to large')"""
    else: 
        p1Answer = p1Answer + v["size"]

more_flatter_file_structure.sort(key=lambda x: x["size"]) 

for dir in more_flatter_file_structure:
    print(dir["size"])

print("----p1------")
print(p1Answer)

free_space = 70000000- fs[0]["size"]
update_size = 30000000

print("----p2------")
print(f'space available for update: {free_space - update_size}')

# 30,000,000
# 8,381,165


