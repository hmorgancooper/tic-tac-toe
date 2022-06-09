import pytest
from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax

EMPTY = None

def test_player_empty():
    board = initial_state()
    assert(player(board) == 'X')


def test_player_x_turn():
    board = initial_state()
    board[0][0] = 'X'
    board[0][1] = 'O'
    assert(player(board) == 'X')
    board[0][2] = 'X'
    board[1][0] = 'O'
    assert(player(board) == 'X')

def test_player_o_turn():
    board = initial_state()
    board[0][0] = 'X'
    assert(player(board) == 'O')
    board[0][1] = 'O'
    board[0][2] = 'X'
    assert(player(board) == 'O')

def test_actions():
    board = [['X', 'O', EMPTY],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    assert(actions(board) == [(0, 2)])
    board = [['X', 'O', EMPTY],
             [EMPTY, 'O', 'X'],
             ['O', 'X', EMPTY]]  
    assert(actions(board) == [(0,2), (1, 0), (2,2)])  

def test_result_invalid_action():
    board = [['X', 'O', EMPTY],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    with pytest.raises(Exception):
        assert(result(board, action))

def test_result_x_turn():
    board = [['X', 'O', EMPTY],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    action = (0, 2)
    new_board = [['X', 'O', 'X'],
                 ['X', 'O', 'X'],
                 ['O', 'X', 'O']]
    assert(result(board, action) == new_board)

def test_result_o_turn():
    board = [['X', EMPTY, EMPTY],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    action = (0, 1)
    new_board = [['X', 'O', EMPTY],
                 ['X', 'O', 'X'],
                 ['O', 'X', 'O']]
    assert(result(board, action) == new_board)
    
def test_x_winner_diagonal():
    board = [['X', EMPTY, EMPTY],
             ['X', 'X', 'O'],
             ['O', 'O', 'X']]
    assert(winner(board) == 'X')

def test_o_winner_diagonal():
    board = [['X', EMPTY, 'O'],
             ['X', 'O', 'X'],
             ['O', 'O', 'X']]
    assert(winner(board) == 'O')

def test_x_winner_horizontal():
    board = [['X', 'O', EMPTY],
             ['X', 'X', 'X'],
             ['O', 'O', EMPTY]]
    assert(winner(board) == 'X')

def test_o_winner_vertical():
    board = [['X', 'O', EMPTY],
             ['X', 'O', 'X'],
             ['O', 'O', 'X']]
    assert(winner(board) == 'O')

def test_winner_tie():
    board = [['X', 'O', 'X'],
             ['X', 'O', 'O'],
             ['O', 'X', 'X']]
    assert(winner(board) == None)

def test_terminal_no_winner():
    board = [['X', 'O', 'X'],
             ['X', 'O', 'O'],
             ['O', 'X', 'X']]
    assert(terminal(board) == True)

def test_terminal_o_winner():
    board = [['X', 'O', 'X'],
             ['X', 'O', 'O'],
             ['O', 'O', 'X']]
    assert(terminal(board) == True)

def test_terminal_x_winner():
    board = [['X', 'X', 'O'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']]
    assert(terminal(board) == True)

def test_terminal_unfinished():
    board = [['X', 'X', 'O'],
            ['O', EMPTY, 'O'],
            ['X', 'O', 'X']]
    assert(terminal(board) == False)

def test_terminal_winner_unfinished():
    board = [['X', 'X', EMPTY],
            ['X', EMPTY, 'O'],
            ['X', 'O', 'O']]
    assert(terminal(board) == True)

def test_terminal_example():
    board = [['X', 'X', EMPTY],
             ['O', 'X', 'O'],
             [EMPTY, 'O', EMPTY]]
    assert(terminal(board) == False)

def test_utility_x_winner():
    board = [['X', 'X', 'O'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']]
    assert(utility(board) == 1)

def test_utility_o_winner():
    board = [['X', 'O', 'X'],
             ['X', 'O', 'O'],
             ['O', 'O', 'X']]
    assert(utility(board) == -1)

def test_utility_no_winner():
    board = [['X', 'O', 'X'],
             ['X', 'O', 'O'],
             ['O', 'X', 'X']]
    assert(utility(board) == 0)

def test_mini_max_x():
    board = [['X', 'X', EMPTY],
             ['O', 'X', 'O'],
             [EMPTY, 'O', EMPTY]]
    assert(minimax(board) == (2,2) or minimax(board) == (0,2))

def test_mini_max_x_2():
    board = [['X', 'X', EMPTY],
             ['O', 'O', 'X'],
             [EMPTY, 'O', EMPTY]]
    assert(minimax(board) == (0,2))

def test_mini_max_x_3():
    board = [['X', 'O', EMPTY],
             ['X', 'O', 'X'],
             [EMPTY, EMPTY, 'O']]
    assert(minimax(board) == (2,0))

def test_mini_max_o():
    board = [['X', 'X', 'O'],
             [EMPTY, 'X', 'O'],
             ['X', 'O', EMPTY]]
    assert(minimax(board) == (2,2))

def test_mini_max_o_2():
    board = [['X', EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert(minimax(board) == (1,1))

# def main():
#     board = [['X', EMPTY, EMPTY],
#                 [EMPTY, EMPTY, EMPTY],
#                 [EMPTY, EMPTY, EMPTY]]
#     minimax(board)

# if __name__ == '__main__':
#     main()
