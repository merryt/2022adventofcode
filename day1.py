
day1input = open("./day1input.txt", "r" )
output = day1input.read()
elves_load = output.split('\n\n')
elves_load_calories = [ sum([int(i) for i in x.split('\n') if i !='']) for x in elves_load]
sorted_loaded_elves = sorted(elves_load_calories)

print("----Part 1-----")
print(sorted_loaded_elves[-1])

print("----Part 2-----")
print(sum(sorted_loaded_elves[-3:]))



day1input.close()