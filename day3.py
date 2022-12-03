# a rock
# b paper
# c scisors 
points = ["-"]
points = points + list(map(chr, range(ord('a'), ord('z')+1)))
points = points + list(map(chr, range(ord('A'), ord('Z')+1)))
    
    
day3input = open("./day3input.txt", "r" )
output = day3input.read()
rucksacks = output.split('\n')

split_rucksacks = [[x[:len(x)//2],x[len(x)//2:]] for x in rucksacks if x != ""]

duplicates_for_part1 = []
duplicates_for_part2 = []

def check_for_duplicates_from_two(list1, list2):
    for item in list1:
        if list2.count(item) > 0:
            duplicates_for_part1.append(item)
            return

def check_for_duplicates_from_three(list1, list2, list3):
    for item in list1:
        if (list2.count(item) > 0) and (list3.count(item) > 0):
            duplicates_for_part2.append(item)
            return

for rucksack in split_rucksacks:
    check_for_duplicates_from_two(rucksack[0], rucksack[1])
    
print(len(rucksacks))
for i in range(0,len(rucksacks)-3, 3):
    print(f'total:{len(rucksacks)}, current: {i}, {i+1}, {i+2}')
    check_for_duplicates_from_three(rucksacks[i], rucksacks[i+1], rucksacks[i+2])
            

scored_duplicates_part1 = [ points.index(x) for x in duplicates_for_part1]
scored_duplicates_part2 = [ points.index(x) for x in duplicates_for_part2]




print("----Part 1-----")
print(sum(scored_duplicates_part1))


print("----Part 2-----")
print(sum(scored_duplicates_part2))


day3input.close()