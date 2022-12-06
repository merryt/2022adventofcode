import sys
sys.setrecursionlimit(5000)
          
day6input = open("./day6input.txt", "r" )
output = day6input.read()
day6input.close()
letters = [*output]

def find_first_unique_group(list, count=0, size=4):
    first_group = list[0:size]
    if len(first_group) == len({*first_group}):
        return count

    return find_first_unique_group(list[1:], count+1, size)
    

print("----p1------")
print(find_first_unique_group(letters, 4, 4))

print("----p2------")
print(find_first_unique_group(letters, 14, 14))