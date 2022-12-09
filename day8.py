import copy

def line_of_site(y, x, dir, height, count = False):
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
    

def scenic_scorer(y, x, dir,orig_height, height=0, count = 0):
        
    if y >= trees_len or x >= trees_len or y < 0 or x < 0:
        return count
    
    if orig_height <= trees[y][x]:
        return count + 1
        
    if dir == "y+":
        return scenic_scorer(y+1, x, dir, orig_height, height, count+1)
    if dir == "y-":
        return scenic_scorer(y-1, x, dir, orig_height, height, count+1)
    if dir == "x+":
        return scenic_scorer(y, x+1, dir, orig_height, height, count+1)
    if dir == "x-":
        return scenic_scorer(y, x-1, dir, orig_height, height, count+1)
    

"""
hotplate
"""
day8input = open("./day8input.txt", "r" )
output = day8input.read()
day8input.close()
trees = [ [ int(y) for y in [*x]] for x in output.split('\n') if x != ""]
trees_len = len(trees)

vis = [[False for _ in range(trees_len)] for _ in range(trees_len)]
scenic_score = [[0 for _ in range(trees_len)] for _ in range(trees_len)]

for x in range(0,trees_len):
    vis[0][x] = True
    vis[trees_len-1][x] = True
    vis[x][0] = True
    vis[x][trees_len-1] = True

for y in range(1,trees_len-1):
    for x in range(1,trees_len-1):
        if line_of_site(y+1,x,"y+", trees[y][x]) or line_of_site(y-1,x,"y-", trees[y][x]) or line_of_site(y,x+1,"x+", trees[y][x]) or line_of_site(y,x-1,"x-", trees[y][x]):
            vis[y][x] = True

count = 0
for x in range(trees_len):
    for y in range(trees_len):
        if vis[y][x]:
            count = count + 1
           
           
bestview = 0
for y in range(trees_len):
    for x in range(trees_len):
        # if not vis[y][x]:
        scenic_score[y][x] = scenic_scorer(y+1,x,"y+", trees[y][x]) * scenic_scorer(y-1,x,"y-", trees[y][x]) * scenic_scorer(y,x+1,"x+", trees[y][x]) * scenic_scorer(y,x-1,"x-", trees[y][x])
        if scenic_score[y][x] > bestview:
            bestview = scenic_score[y][x] 
  
  
           
# print(scenic_scorer(2,4-1,"x-", trees[2][4]))
# print("----")           
# for x in trees:
#     print(x)
    
# print("---")

# for y in vis:    
#     print(y)

# print("---")

# for y in scenic_score:    
#     print(y)





print("----p1------")
print(count) # 1789

print("----p2------")
print(bestview)


