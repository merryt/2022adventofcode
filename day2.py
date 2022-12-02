# a rock
# b paper
# c scisors 
shape_points = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def round_scorer_part1(round):
    shape_converter = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    shapes = round.split(" ")
    shapes[1] = shape_converter[shapes[1]]
    win_modifier = 0
    if (shapes[0] == shapes[1]):
        #tie
        win_modifier = 3
    elif((shapes[0] == "A" and shapes[1] == "B") or (shapes[0] == "B" and shapes[1] == "C") or (shapes[0] == "C" and shapes[1] == "A")):
        #win
        win_modifier = 6
    
    return shape_points[shapes[1]] + win_modifier



def round_scorer_part2(round):
    shapes = round.split(" ")
    their_shape = shapes[0]
    their_shape_positon = ["A","B","C"].index(their_shape)
 
    round_decorder = {
        "X": 0,
        "Y": 3,
        "Z": 6, 
    }
    
    win_modifier = round_decorder[shapes[1]]
    our_shape = ["A", "B", "C"][int(their_shape_positon + win_modifier/3-1 )%3]
    return shape_points[our_shape] + win_modifier
    



day2input = open("./day2input.txt", "r" )
output = day2input.read()
rounds = output.split('\n')


scored_rounds_part1 = [ round_scorer_part1(x) for x in rounds if x != ""]


print("----Part 1-----")
print(sum(scored_rounds_part1))


print("----Part 2-----")
print(sum([ round_scorer_part2(x) for x in rounds if x != ""]))


day2input.close()