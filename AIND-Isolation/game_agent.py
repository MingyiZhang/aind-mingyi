"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')
    if game.is_winner(player):
        return float('inf')
    # number of legal moves of active player
    act_moves = len(game.get_legal_moves(player))
    # number of legal moves of inactive player
    inact_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(0.4 * act_moves - 0.6 * inact_moves)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')
    if game.is_winner(player):
        return float('inf')

    act_moves = len(game.get_legal_moves(player))
    inact_moves = 0
    for move in game.get_legal_moves(player):
        new_game = game.forecast_move(move)
        inact_moves += len(new_game.get_legal_moves()) / act_moves

    return float(0.3 * act_moves - 0.7 * inact_moves)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')
    if game.is_winner(player):
        return float('inf')

    act_moves = len(game.get_legal_moves(player))

    return float(act_moves)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=20.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        def terminal_test(game):
            '''
            Check if the current node is a terminal
            Returns
            -------
            bool
                TRUE: the node is terminal
                FALSE: the node is not terminal
            '''
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return not bool(game.get_legal_moves())

        def min_value(game, depth):
            '''
            Get the score for the min player
            '''
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            if terminal_test(game) or depth <= 0:
                # if the node is terminal or the search achieves the depth limits
                # return the score
                return self.score(game, self)
            # find the minimum score from the children nodes
            v = float('inf')
            for move in game.get_legal_moves():
                v = min(v, max_value(game.forecast_move(move), depth - 1))
            return v

        def max_value(game, depth):
            '''
            Get the score for the max player
            '''
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            if terminal_test(game) or depth <= 0:
                # if the node is terminal or the search achieves the depth limits
                # return the score
                return self.score(game, self)
            # find the maximum score from the children nodes
            v = float('-inf')
            for move in game.get_legal_moves():
                v = max(v, min_value(game.forecast_move(move), depth - 1))
            return v

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # setup the initial score and move
        best_score = float('-inf')
        best_move = (-1, -1)
        if not (terminal_test(game) or depth <= 0):
            # if the root node is not terminal and the search depth is not 0
            # find the best move that maximize the score in the children nodes
            best_move = max(game.get_legal_moves(),
                            key=lambda m: min_value(game.forecast_move(m), depth-1))
            return best_move
        # if the root node is terminal or the search depth is 0
        # return (-1, -1)
        return best_move


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        best_move = (-1, -1)

        try:
            # loop over the depth from 0 to the largest depth
            for depth in range(len(game.get_blank_spaces())):
                # store the best move for each depth-fixed alpha-beta pruning search
                best_move = self.alphabeta(game, depth)

        except SearchTimeout:
            return best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        def terminal_test(game):
            '''
            Check if the current node is a terminal
            Returns
            -------
            bool
                TRUE: the node is terminal
                FALSE: the node is not terminal
            '''
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return not bool(game.get_legal_moves())

        def min_value(game, depth, alpha, beta):
            '''
            Get the score for the min player
            '''
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            if terminal_test(game) or depth <= 0:
                return self.score(game, self)

            v = float('inf')
            for move in game.get_legal_moves():
                v = min(v, max_value(game.forecast_move(move), depth-1, alpha, beta))
                # if the score of the node is not greater than alpha
                # return the score, and pruning
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        def max_value(game, depth, alpha, beta):
            '''
            Get the score for the max player
            '''
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            if terminal_test(game) or depth <= 0:
                return self.score(game, self)

            v = float('-inf')
            for move in game.get_legal_moves():
                v = max(v, min_value(game.forecast_move(move), depth-1, alpha, beta))
                # if the score of the node is not smaller than beta
                # return the score, and pruning
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_score = float('-inf')
        best_move = (-1, -1)
        if not (terminal_test(game) or depth <= 0):
            for move in game.get_legal_moves():
                score = max(best_score, min_value(game.forecast_move(move), depth-1, alpha, beta))
                # if score is greater than the best_score
                # use score to replace best_score, use current move to replace best_move
                if score > best_score:
                    best_score, best_move = score, move
                # if best_score is not smaller than beta
                # pruning and return the current best_move
                if best_score >= beta:
                    return best_move
                alpha = max(alpha, best_score)
            # if there is no pruning, return the current best_move
            return best_move
        # if the root node is terminal or search depth is 0,
        # return (-1, -1)
        return best_move
