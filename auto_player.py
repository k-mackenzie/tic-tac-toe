import random

# position = int(input("1-9: "))

def first_move():
    global position
    # if opponent takes centre, take a corner
    # if opponent takes a corner, take the centre or a corner
    best_pos = [1,3,5,7,9]
    if position in best_pos:
        best_pos.remove(position)
        print(best_pos)
        move = random.choice(best_pos)
        print(move)
    else:
        move = random.choice(best_pos)
        print(move)
    
    
    # if position == 5:
    #     corners = random.randint(1,4)
    #     if corners == 1:
    #         move = 1
    #     elif corners == 2:
    #         move = 3
    #     elif corners == 3:
    #         move = 7
    #     else:
    #         move = 9

    # elif position == 1 or 3 or 7 or 9:
    #     move = 5
# first_move()