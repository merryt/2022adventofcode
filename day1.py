
day1input = open("./day1input.txt", "r" )
# output = day1input.read()
# elves_load = output.split('\n\n')
# elves_load_calories = [ sum([int(i) for i in x.split('\n') if i !='']) for x in elves_load]
# print(sorted(elves_load_calories)[-1])


output = print(sorted([ sum([int(i) for i in x.split('\n') if i !='']) for x in day1input.read().split('\n\n')])[-1])
day1input.close()