"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Check number of 'X's and 'O's
    x_count = 0
    o_count = 0
    for row in board:
        for space in row:
            if space == 'X':
                x_count += 1
            elif space == 'O':
                o_count +=1
    if x_count == 0 and o_count == 0:
        return X
    elif x_count == o_count:
        return X
    elif x_count > o_count:
        return O
    else:
        raise('Impossible board!')


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_list.append((i, j))
    return action_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if action is not in empty spot
    if board[action[0]][action[1]] != EMPTY:
        raise(Exception('Not valid move!'))
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            return board[i][0]
    for j in range(3):
        if (board[0][j] == board[1][j]) and (board[1][j] == board[2][j]):
            return board[0][j]
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return board[1][1]
    elif(board[2][0] == board[1][1]) and (board[1][1] == board[0][2]):
        return board[1][1]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    full = True
    for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    full = False
    if full == True:
        return True
    # If there is a winner stop game
    elif winner(board) != None:
        return True
    else:
        return False
            


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
         return None
    # Get player
    p = player(board)   
    if p == 'X':
        a = actions(board)
        best_val = float('-inf')
        for action in a:
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_action = action
        return best_action
    if p == 'O':
        a = actions(board)
        best_val = float('inf')
        for action in a:
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_action = action
        return best_action
    

def max_value(board):
    if terminal(board):
        return utility(board)
    best_val = float('-inf')
    a = actions(board)
    for action in a:
        v = max(best_val, min_value(result(board, action)))
        if v > best_val:
            best_val = v
    return best_val 


def min_value(board):
    if terminal(board):
        return utility(board)
    best_val = float('inf')
    a = actions(board)
    for action in a:
        v = min(best_val, max_value(result(board, action)))
        if v < best_val:
            best_val = v
    return best_val