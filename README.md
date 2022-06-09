# Tic-Tac-Toe
Implemented AI to play tic-tac-toe optimally using a minimax algorithm. Completed as part of Harvard's CS50-AI course. 
The runner.py script was provided by CS50, I completed the functions in tictactoe.py and wrote test_tictactoe.py.

## Set up
Clone repo and set up venv.
Install requirements using
```bash
  pip install -r requirements.txt
```

The tests are run using pytest as follows:
```bash
  pytest test_tictactoe.py
```

To play:
```bash
python3 runner.py
```

## Method
The script uses a minimax algorithm to find the optimum move for the AI to take in tic-tac-toe.
In a minimax algorithm one 'player' is trying to maximise the score, and one player is trying to minimise the score. Each player considers what move its opponent will make when making its decision, which in turn triggers the opponent to consider what move the player will make. This cycle continues until there there is a final board state with a winner, a loser or a tie. This final board state is given a score - +1 for a win, -1 for a lose and 0 for a tie. Player X will chose the final board state with the maximum score and Player O will chose the final board state with the minimum score.

The minimax function in tictactoe.py follows this logic:

1. Work out whose turn it is
2. Work out what actions they can take
3. Loop through each of the possible actions and check board state
4. Repeat steps 1 - 3 alternating playing as X or O until there is a winner, loser or a tie
5. Return the board score (+1 for winner, -1 for loser, 0 for tie)
6. Player X will chose the highest possible score from all the possible actions
7. Player O will chose the lowest possible score from all the possible actions

