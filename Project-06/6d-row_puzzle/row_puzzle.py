# Author: Timur Guner
# Date: 2021-05-12
# Description: Project 6d has the user create a list of random numbers that ends in 0. It is passed to the row_puzzle
#              function, which determines each move the user can make starting at slot 0. The number in each slot tells
#              the user how many slots they can move left or right without going out of bounds. To win the final move
#              must end on the 0 in the last slot.


def row_puzzle(squares, pos=0, pos_track=None):
    """
    The row_puzzle function takes  list of random numbers that ends in 0. It is passed to the row_puzzle function, which
    determines each move the user can make starting at slot 0. The number in each slot tells the user how many slots
    they can move left or right without going out of bounds. To win the final move must end on the 0 in the last slot.
    When a win occurs, True is return. If it is not possible to win the function returns false.
    """

    # If the move is on the last spot, the user wins
    if pos == len(squares)-1:
        return True

    if squares[0] == 0:
        return False

    # pos_track is a dictionary will keep track of each move
    if pos_track is None:
        pos_track = {}

    # This if statement is used to make the first move. If the first number in the list is bigger than the list length
    # return false. If not the dictionary begins tracking by assigning the current index as the first key equal to two.
    # The next key is created by using the next index that is being used as the key and assign one to the key.
    if pos == 0:
        if squares[pos] > len(squares)-1:
            return False
        pos_track[pos] = 2
        pos_track[(pos + squares[pos])] = 1
        return row_puzzle(squares, pos + squares[pos], pos_track)

    # use the current number in the current index to determine the jumps it can go each direction
    key_1 = (pos + squares[pos])
    key_2 = (pos - squares[pos])

    # if both keys are out of bounds, game is lost and returns false
    if key_1 > len(squares)-1 and key_2 < 0:
        return False

    # The long elif statement says what move is next based on the value in the current index and index number. It first
    # checks if the moves can go right and based on if the slot was already used or not. It will create a new key in the
    # dictionary for the new slot if that slot was not used. If it is already it the dictionary listed, it can be
    # incremented again but will not be able to be used again in this statement. This statement does the same checks
    # when the move needs to go left. If everything does not pass, return False, others continue the recursion.
    if squares[pos] <= len(squares)-pos-1 and pos_track[pos] <= 1 and key_1 not in pos_track:
        pos_track[(pos + squares[pos])] = 1
        pos_track[pos] = 2
        return row_puzzle(squares, pos + squares[pos], pos_track)
    elif squares[pos] <= len(squares)-pos-1 and pos_track[pos] <= 1 and key_1 in pos_track and pos_track[key_1] <= 1:
        pos_track[(pos + squares[pos])] = 2
        pos_track[pos] = 2
        return row_puzzle(squares, pos + squares[pos], pos_track)
    elif pos_track[pos] <= 1 and pos - squares[pos] > 0 and key_2 not in pos_track:
        pos_track[(pos - squares[pos])] = 1
        pos_track[pos] = 2
        return row_puzzle(squares, pos - squares[pos], pos_track)
    elif pos_track[pos] <= 1 and pos - squares[pos] > 0 and key_2 in pos_track and pos_track[key_2] <= 1:
        pos_track[(pos - squares[pos])] = 2
        pos_track[pos] = 2
        return row_puzzle(squares, pos - squares[pos], pos_track)
    else:
        return False


squares = [2,1,1,0,1,0]

print(row_puzzle(squares))