import math

day10input = open("./day10input.txt", "r" )
output = day10input.read()
day10input.close()
width = 40
height = 6

instructions = [ x for x in output.split('\n') if x != ""]

buffer = [1]
rolling_interpretation = [1]
for i in range(len(instructions)):
    op = instructions[i]
    rolling_interpretation.append(rolling_interpretation[i-1])

    if op == "noop":
        buffer.append(False)
    else:
        op_val = int(op.split(" ")[1])
        buffer.append(0)
        buffer.append(op_val)
        rolling_interpretation.append(rolling_interpretation[i-1] + op_val)

print(buffer)    

def signal_strength_checker(buffer, time):
    return sum(buffer[0:time] * time)

t1 = signal_strength_checker(buffer, 20)
t2 = signal_strength_checker(buffer, 60)
t3 = signal_strength_checker(buffer, 100)
t4 = signal_strength_checker(buffer, 140)
t5 = signal_strength_checker(buffer, 180)
t6 = signal_strength_checker(buffer, 220)


print(t5)
print(rolling_interpretation[179]*180)

print("----p1------")
print(t1 + t2 + t3 + t4 + t5 + t6)

print("----p2------")
screen = [[" " for _ in range(width)] for _ in range(height)]

for i in range(1, 240):
    row = math.floor((i - 1) / 40)
    col = (i) % 40
    print(col, rolling_interpretation[i])
    if (abs(col - rolling_interpretation[i]) <= 1):
      screen[row][col] = "█"


for row in screen:
    print("".join(str(x) for x in row))
    

# print(buffer)
print(rolling_interpretation)