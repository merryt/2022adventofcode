def process_input(x):
    split_to_pairs = x.split(",")
    return [[int(x) for x in split_to_pairs[0].split("-")], [int(x) for x in split_to_pairs[1].split("-")]]

def is_contained_in(inner, outer):     
    if (inner[0] <= outer[0]) and (inner[1] >= outer[1]):
        return 12
    return 0
    
def overlap(a, b):
    count = 0
    for i in range(a[0], a[1]+1):
        if i in range(b[0], b[1]+1):
            count += 1
            
    return count
    
day4input = open("./day4input.txt", "r" )
output = day4input.read()
pairs = [ process_input(x) for x in output.split('\n') if x != ""]


count_p1 = 0
count_p2 = 0
for pair in pairs:
    if is_contained_in(pair[0], pair[1]) or is_contained_in(pair[1], pair[0]):
        count_p1 += 1
        

for pair in pairs:
    if overlap(pair[0], pair[1]) > 0:
        count_p2 += 1



print(overlap([97, 97], [44, 96]))
print(overlap([7, 8], [8, 18]))


print("\n----Part 1-----")
print(count_p1)


print("----Part 2-----")
print(count_p2)


day4input.close()