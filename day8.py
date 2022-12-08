import copy

def line_of_site(y, x, dir, height):
    if y >= trees_len or x >= trees_len or y < 0 or x < 0:
        return True
    if height <= trees[y][x]:
        return False
    
    if dir == "y+":
        return line_of_site(y+1, x, dir, height)
    if dir == "y-":
        return line_of_site(y-1, x, dir, height)
    if dir == "x+":
        return line_of_site(y, x+1, dir, height)
    if dir == "x-":
        return line_of_site(y, x-1, dir, height)
    


"""
hot plate
"""
day8input = open("./day8input.txt", "r" )
output = day8input.read()
day8input.close()
trees = [ [*x] for x in output.split('\n') if x != ""]
trees_len = len(trees)

vis = [[False for _ in range(trees_len)] for _ in range(trees_len)]

for x in range(0,trees_len):
    vis[0][x] = True
    vis[trees_len-1][x] = True
    vis[x][0] = True
    vis[x][trees_len-1] = True

for y in range(1,trees_len-1):
    for x in range(1,trees_len-1):
        if line_of_site(y+1,x,"y+", trees[y][x]) or line_of_site(y-1,x,"y-", trees[y][x]) or line_of_site(y,x+1,"x+", trees[y][x]) or line_of_site(y,x-1,"x-", trees[y][x]):
            vis[y][x] = True

# for x in trees:
#     print(x)

# for y in vis:    
#     print(y)


count = 0
for x in range(trees_len):
    for y in range(trees_len):
        if vis[y][x]:
            count = count + 1

print("----p1------")
print(count) # 1789

print("----p2------")
# print(f'space available for update: {free_space - update_size}')


