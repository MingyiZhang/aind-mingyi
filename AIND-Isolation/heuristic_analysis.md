# Isolation Heuristic Analysis
#### Mingyi Zhang

### Definition
I defined three heuristics `custom_score()`, `custom_score_2()` and `custom_score_3()`. All heuristics are given by the difference between the number of legal moves of active player and inactive player. The general formula of the heuristics $H$
$$
H = a \times N_{\text{active}} - b\times N_{\text{inactive}}
$$
where $a$ and $b$ are two parameters that $a + b = 1$; $N_{\text{active}}$ is the number of legal moves of the active player, while $N_{\text{inactive}}$ is of the inactive player. For the three heuristics, I set $a$ and $b$ as
*  `custom_score()`: $a = 0.05$, $b = 0.95$. The number of legal moves of the inactive player dominants the heuristic. The player tends to consider the move that the opponent has fewer moves.
* `custom_score2()`: $a = 0.5$, $b = 0.5$. The numbers of legal moves of both the active player and the inactive player have the same contribution to the heuristic. Player will maximize the number of its own moves while minimize the number of the opponent's moves.
* `custom_score3()`: $a = 0.95$, $b = 0.05$. The number of legal moves of the active player dominants the heuristic. The player tends to play the move that maximize the possibility of its own moves.

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

    return float(0.05 * act_moves - 0.95 * inact_moves)
```

### Result
I set the parameter `NUM_MATCHES`, number of matches against each opponent, to be 20 in the `tournament.py`, so in total, each heuristic has 40 matches with each predefined heuristics. The result is
![alt text][result40]
__Figure 1__: `tournament.py` results with 40 matches each and 150ms time limit.

We can find that
* the win rates of all players are around 65%.
* the player `AB_Custom_2` with heuristic `custom_score2()` outperforms the baseline player `AB_Improved`. `AB_Custom_2` plays the best against all opponents.

### Recommendation
I would recommend `custom_score2()` because it has the best win rate. It consider the active and inactive player equally. And it is simple enough to explain and it is fast to compute.
![alt text][result100]
__Figure 2__: `tournament.py` results with 100 matches each and 150ms time limit.

[result40]: result.png
[result100]:result_100.png
