import math
from functools import reduce
from math import lcm
day11input = open("./day11input.txt", "r" )
output = day11input.read()
day11input.close()

def build_monkey(x):
    name = x.split('\n')[0]
    items = [y.replace(",", "") for y in x.split('\n')[1].split(':')[1].split(" ") if y != ""]
    operation = x.split('\n')[2].split(':')[1][1:].split("=")[1][1:]
    test = int(x.split('\n')[3].split(" ")[-1]) # currently all tests are divisible
    if_true = int(x.split('\n')[4].split(" ")[-1])
    if_false = int(x.split('\n')[5].split(" ")[-1])
    
    return {
        "name": name,
        "items": items,
        "operation": operation,
        "test": test,
        "if_true_destination": if_true,
        "if_false_destination": if_false,
        "times_inspected": 0
    }

def execute_operation(monkey, old_val):
    return eval(monkey["operation"].replace("old", str(old_val)))

def run_test(worry_level, test_number):
    # 2,3,5,11,13,17,19,23
    if test_number == 2:
        return int(str(worry_level)[-1]) % 2 == 0      
    if test_number == 3:
        return sum(str(worry_level).split()) % 3 == 0      
    if test_number == 5:
        return int(str(worry_level)[-1]) in [0,5]  
    if test_number == 11:
        wl_str = str(worry_level)
        return (int(wl_str[0:-1]) - int(wl[-1])) % 11
    if test_number == 13:
        wl_str = str(worry_level)
        return (int(wl_str[0:-2])*4 - int(wl[-2])) % 13
    if test_number == 17:
        wl_str = str(worry_level)
        return (int(wl_str[0:-2])*2 - int(wl[-2])) % 17
    if test_number == 19:
        wl_str = str(worry_level)
        return (int(wl_str[0:-2]) + (4* int(wl[-2]))) % 19
    if test_number == 23:
        wl_str = str(worry_level)
        return (int(wl_str[0:-3]) - (2* int(wl[-3]))) % 19

def check_and_toss(monkey):
    item_in_hand = monkey["items"][0]
    monkey["items"] = monkey["items"][1:]
    worry_level = execute_operation(monkey, item_in_hand)
    
    # bored_worry_level = math.floor(worry_level/3) # part 1 will need this
    bored_worry_level = worry_level % modulus
    
    
    if bored_worry_level % monkey["test"] == 0:
        monkeys[monkey["if_true_destination"]]["items"].append(bored_worry_level)
    else:
        monkeys[monkey["if_false_destination"]]["items"].append(bored_worry_level)
    monkey["times_inspected"] += 1

monkeys = [ build_monkey(x) for x in output.split('\n\n') if x != ""]

modulus = reduce(lcm, [m["test"] for m in monkeys])
print("modulus", modulus)
# check_and_toss(monkeys[0])
for i in range(10000):
    print(i)
    for monkey in monkeys:
        for item in range(len(monkey["items"])):
            check_and_toss(monkey)
            
    
# for monkey in monkeys:
#     print(monkey["name"], monkey["items"])

monkey_business = []
for monkey in monkeys:
    print(monkey["name"], monkey["times_inspected"])
    monkey_business.append(monkey["times_inspected"])
monkey_business = sorted(monkey_business)

print(monkey_business)
print(monkey_business[-1] * monkey_business[-2])



