# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).

Daniel Willard and I (Isabella Cortez) worked together
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # Daniel Willard's Implementation (Q1)
    """
    # Initialize the stack (now PQ) with the initial state
    stack = util.Stack()
    start_state = problem.getStartState()
    # note to self: (state, path)
    stack.push((start_state, []))

    # Initialize the explored states
    explored = set()

    while not stack.isEmpty():
        # note: python trick to define two variables
        current_state, path = stack.pop()

        if problem.isGoalState(current_state):
            # Goal state reached
            return path
        if current_state not in explored:
            explored.add(current_state)
            successors = problem.getSuccessors(current_state)

            # Python tuple unpacking statement allows you to iterate through the elements of the successors (greek for greeks info and x in y minutes resources)
            # successor: This variable is used to store the first element of each tuple, which represents the successor state.
            # action: This variable is used to store the second element of each tuple, which represents the action taken to reach the successor state
            # _: This variable is used to store the third element of each tuple, which is the cost associated with the action. not used since stack so by convention _
            for successor, action, _ in successors:
                if successor not in explored:
                    stack.push((successor, path + [action]))
    # Return an empty list if no path is found
    # Note to Partner (Isabella Cortez): DFS Completed
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    # My (Isabella Cortez) Implementation (Q2)
    """
    from util import Queue
    # initialize queue and start node
    q = Queue()
    start_node = problem.getStartState()

    # initialize empty lists
    fringe_list = []
    empty_list = []

    # push start node to empty list
    q.push((start_node, empty_list))

    fringe_list.append(start_node)

    # while the queue is not empty
    while not q.isEmpty():
        # pop current state and movements to queue
        state, actions = q.pop()

        # if the state happens to be the goal
        if problem.isGoalState(state):
            return actions

        else:
            # gets successor node/state
            successors = problem.getSuccessors(state)

            # checks items in successor state
            for successor, action, cost in successors:
                # if successor is not in fringe, add it there
                if successor not in fringe_list:
                    fringe_list.append(successor)
                    # create a new path
                    new_path = actions + [action]
                    # push successor with the new path
                    q.push((successor, new_path))
    return empty_list
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """
    Search the node of the least total cost first.
    # Daniel Willard's Implementation (Q3)
    """
    # Initialize the priority queue with the start state and a cost of 0 stolen from my dfs shamelessly
    pq = util.PriorityQueue()
    start_state = problem.getStartState()
    # Note to self (state, path, cost) , priority
    pq.push((start_state, [], 0), 0)

    # Initialize a set to keep track of explored states
    explored = set()

    while not pq.isEmpty():
        # pop doesn't return cost cuzse error remember for future the proritiy is used internal for the made class
        current_state, path, current_cost = pq.pop()

        if problem.isGoalState(current_state):
            return path

        if current_state not in explored:
            explored.add(current_state)
            successors = problem.getSuccessors(current_state)

            #the good ol' python tuple
            for successor, action, step_cost in successors:
                if successor not in explored:
                    # Calculate the new cost based on the path cost
                    new_cost =  current_cost + step_cost
                    # Push the successor state and its path onto the priority queue
                    pq.push((successor, path + [action], new_cost), new_cost)
    # Return an empty list if no path is found
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.

    # My (Isabella Cortez) Implementation with Daniel Willard's Edits (Q4)
    """

    from util import PriorityQueue

    q = PriorityQueue()
    empty_list = []

    # initialize fringe list (this is my explored set)
    fringe_list = []

    # starting node on open
    start_node = problem.getStartState()
    first_heuristic = heuristic(start_node, problem)
    q.push((start_node, empty_list, 0), first_heuristic)

    # while queue is not empty
    while not q.isEmpty():
        # pop queue off list
        state, actions, cost = q.pop()

        # if state is the goal, return actions list
        if problem.isGoalState(state):
            return actions
        # if current position not in list, add it to list
        if state not in fringe_list:
            fringe_list.append(state)
            # get successor node
            successors = problem.getSuccessors(state)

            # for these values in successor node
            for successor, action, cost_of_successor in successors:
                # if successor not in current list
                if successor not in fringe_list:
                    # set path equal to
                    path = list(actions) + [action]
                    # g value this i believed to be the error g = problem.getCostOfActions(path)
                    g = cost + cost_of_successor
                    # h value
                    h = heuristic(successor, problem)
                    # was missing f calculation
                    f = g + h
                    # push into queue
                    q.push((successor, path, g), f)

    return empty_list
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
