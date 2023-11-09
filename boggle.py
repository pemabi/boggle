
import random
import numpy as np

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
for row in board:
        print(row[0], row[1], row[2], row[3])

vectors = [np.array([0, 1]), np.array([1, 1]), np.array([1, 0]), np.array([1, -1]), np.array([0, -1]), np.array([-1, -1]), np.array([-1, 0]), np.array([-1, 1])]
words = []
vector_log = []  # tracks the word path to exclude repetitions

def find_words(current_die, current_word, min_length, max_length):  # recursive implementation running thru all of the possible letter combinations to a defined max length
    for vector in vectors:  # iterates thru the vectors, looking at next die along
        next_die = (current_die[0] + vector[0], current_die[1] + vector[1])

        if 0 <= next_die[0] <= 3 and 0 <= next_die[1] <= 3:  # if die is on board
            if len(vector_log) < 2 or not (np.array_equal(vector, vector_log[-1] * -1) and np.array_equal(vector, vector_log[-2])):  # first checks if word is too short to be repeating, if not then makes sure there is no repetition

                vector_log.append(vector)

                word = current_word + board[next_die[0]][next_die[1]]  # adds new letter to existing string, then adds this to word array
                if sum(1 for c in word if c.isupper()) >= min_length:  # checks word is above minimum length. Counting upper case letters to deal with 'Qu's
                    words.append(word)
                if sum(1 for c in word if c.isupper()) <= max_length:  # if the word is within max length limits, run the recursion setting most recent die examined as current_die.
                    find_words(next_die, word, min_length, max_length)

                del vector_log[-1]  # removes the last vector - works handily with the recursion when stepping back down in word size - cuts off each node when done with branching

find_words(current_die=(0,0), current_word=board[0][0], min_length=3, max_length=4)
print(len(words))
print(words)

