
import random

# These are dice configs from pre-2008 version of game

classic_dice = True

die0 = ['R', 'I', 'F', 'O', 'B', 'X'] if classic_dice else ['A', 'A', 'E', 'E', 'G', 'N']
die1 = ['I', 'F', 'E', 'H', 'E', 'Y'] if classic_dice else ['A', 'B', 'B', 'J', 'O', 'O']
die2 = ['D', 'E', 'N', 'O', 'W', 'S'] if classic_dice else ['A', 'C', 'H', 'O', 'P', 'S']
die3 = ['U', 'T', 'O', 'K', 'N', 'D'] if classic_dice else ['A', 'F', 'F', 'K', 'P', 'S']
die4 = ['H', 'M', 'S', 'R', 'A', 'O'] if classic_dice else ['A', 'O', 'O', 'T', 'T', 'W']
die5 = ['L', 'U', 'P', 'E', 'T', 'S'] if classic_dice else ['C', 'I', 'M', 'O', 'T', 'U']
die6 = ['A', 'C', 'I', 'T', 'O', 'A'] if classic_dice else ['D', 'E', 'I', 'L', 'R', 'X']
die7 = ['Y', 'L', 'G', 'K', 'U', 'E'] if classic_dice else ['D', 'E', 'L', 'R', 'V', 'Y']
die8 = ['Qu', 'B', 'M', 'J', 'O', 'A']if classic_dice else ['D', 'I', 'S', 'T', 'T', 'Y']
die9 = ['E', 'H', 'I', 'S', 'P', 'N'] if classic_dice else ['E', 'E', 'G', 'H', 'N', 'W']
die10 = ['V', 'E', 'T', 'I', 'G', 'N'] if classic_dice else ['E', 'E', 'I', 'N', 'S', 'U']
die11 = ['B', 'A', 'L', 'I', 'Y', 'T'] if classic_dice else ['E', 'H', 'R', 'T', 'V', 'W']
die12 = ['E', 'Z', 'A', 'V', 'N', 'D'] if classic_dice else ['E', 'I', 'O', 'S', 'S', 'T']
die13 = ['R', 'A', 'L', 'E', 'S', 'C'] if classic_dice else ['E', 'L', 'R', 'T', 'T', 'Y']
die14 = ['U', 'W', 'I', 'L', 'R', 'G'] if classic_dice else ['H', 'I', 'M', 'N', 'U', 'Qu']
die15 = ['P', 'A', 'C', 'E', 'M', 'D'] if classic_dice else ['H', 'L', 'N', 'N', 'R', 'Z']

dice = [die0, die1, die2, die3, die4, die5, die6, die7, die8, die9, die10, die11, die12, die13, die14, die15]

random.shuffle(dice)  # puts the dice in random order

board = [  # picks a random letter from each die
    [random.choice(dice[0]), random.choice(dice[1]), random.choice(dice[2]), random.choice(dice[3])],
    [random.choice(dice[4]), random.choice(dice[5]), random.choice(dice[6]), random.choice(dice[7])],
    [random.choice(dice[8]), random.choice(dice[9]), random.choice(dice[10]), random.choice(dice[11])],
    [random.choice(dice[12]), random.choice(dice[13]), random.choice(dice[14]), random.choice(dice[15])]]

vectors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
words = []

def find_words(start_die, current_word, max_length):
    for vector in vectors:
            if 0 <= start_die[0] + vector[0] <= 3 and 0 <= start_die[1] + vector[1] <= 3:  # checks if sq is on board
                current_word = board[start_die[0]][start_die[1]] + board[start_die[0] + vector[0]][start_die[1] + vector[1]]
                words.append(current_word)
                if len(current_word) <= max_length:
                    find_words((start_die[0] + vector[0], start_die[1] + vector[1]), current_word, max_length)

                            
for row in board:
        print(row[0], row[1], row[2], row[3])

find_words((0, 0), False, 1)
print(words)
