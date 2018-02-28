# Isolation Heuristic Analysis
#### Mingyi Zhang

### Definition
I defined three heuristics `custom_score()`, `custom_score_2()` and `custom_score_3()`.
*  `custom_score()`: return the difference between the numbers of legal moves of the active player and inactive player.  
* `custom_score2()`: calculate the number of possible moves of the active player and the average number of possible moves of the opponent in the next step. The score returns the difference between the two numbers.
* `custom_score3()`: return the numbers of legal moves of the active player.

The following is an example of the implementation of `custom_score()`
```python
def custom_score(game, player):
    if game.is_loser(player):
        return float('-inf')
    if game.is_winner(player):
        return float('inf')
    # number of possible moves for active player and inactive player
    act_moves = len(game.get_legal_moves(player))
    inact_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(act_moves - inact_moves)
```

### Result
I set the parameter `NUM_MATCHES`, number of matches against each opponent, to be 20 in the `tournament.py`, so in total, each heuristic has 40 matches with each predefined heuristics. The result is
![alt text][result40]
__Figure 1__: `tournament.py` results with 40 matches each and 150ms time limit.

We can find that the player `AB_Custom` with heuristic `custom_score()` outperforms the baseline player `AB_Improved`. `AB_Custom` plays the best against all opponents.

### Recommendation
I would recommend `custom_score()` because it has the best win rate. It consider the active and inactive player equally. And it is simple enough to explain and it is fast to compute.
![alt text][result100]
__Figure 2__: `tournament.py` results with 100 matches each and 150ms time limit.

[result40]: result.png
[result100]:result_100.png
