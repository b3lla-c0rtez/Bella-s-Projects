# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """PAC man has two states (drugged up and normal), position
        Ghosts have Two Stats (killer or scared), a timer, and position 
        Game states is the score, 
        States we need to track: 
        1) PACs position 
        2) PACs drug level 1 or none 
        3) Ghost position 
        4) Ghost State Scared or not 
        5) Ghosts timer
        6) Games Scores 
        7) Game Food Postions"""

        #Address each state by priority

        #Ghost position
        # Calculate the distance to the closest ghost
        ghostDistances = [util.manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        closestGhostDistance = min(ghostDistances)
        # two is used not one since one causes interaction with killer ghost
        if closestGhostDistance < 2:
            return -float('inf')

        # food Count and Positions
        # NO killer ghost so eat up Pman
        closestFoodDistance = float('inf')
        foodCount = currentGameState.getNumFood()
        nextFoodCount = successorGameState.getNumFood()
        if nextFoodCount < foodCount:
            return float('inf')

        # This pioritise food as the 2nd highest after ghosts
        # Food in list form from method notes
        # Calculate the distance to the closest food pellet
        foodDistances = [util.manhattanDistance(newPos, food) for food in newFood.asList()]
        closestFoodDistance = min(foodDistances)

        # we must return the inverse to force node attempt
        return 1.0 / closestFoodDistance

        # given form project
        # return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def minimax(self, depth, agentIndex, gameState):
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)

        if agentIndex == 0:
            i = float('-inf')
            for move in gameState.getLegalActions(agentIndex):
                successor = gameState.generateSuccessor(agentIndex, move)
                value = self.minimax(depth, agentIndex+1, successor)
                i = max(i, value)
            return i
        else:
            i = float('inf')
            #action = None
            for move in gameState.getLegalActions(agentIndex):
                successor = gameState.generateSuccessor(agentIndex, move)
                if agentIndex == gameState.getNumAgents() - 1:
                    value = self.minimax(depth - 1, 0, successor)
                else:
                    value = self.minimax(depth, agentIndex+1, successor)
                i = min(i, value)
            return i

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        legalActions = gameState.getLegalActions(0)
        bestValue = float('-inf')
        bestAction = None
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            # Start with min layer (ghosts)
            value = self.minimax(self.depth, 1, successor)
            if value > bestValue:
                bestValue = value
                bestAction = action
        return bestAction


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def alphabeta(self, depth, agentIndex, gameState, alpha, beta):
        if gameState.isWin() or gameState.isLose() or depth == 0:
            # evaluation function for leaf nodes
            return self.evaluationFunction(gameState)

        legalActions = gameState.getLegalActions(agentIndex)

        # Check if it's Pacman's turn (max layer)
        if agentIndex == 0:
            bestValue = float('-inf')
            for action in legalActions:
                successor = gameState.generateSuccessor(agentIndex, action)
                # Next agent is a min agent
                value = self.alphabeta(depth, agentIndex + 1, successor, alpha, beta)
                bestValue = max(bestValue, value)

                # Alpha-beta pruning
                if bestValue > beta:
                    return bestValue

                alpha = max(alpha, bestValue)
            return bestValue
        # Min layer (Ghosts)
        else:
            bestValue = float('inf')
            for action in legalActions:
                successor = gameState.generateSuccessor(agentIndex, action)
                if agentIndex == gameState.getNumAgents() - 1:
                    # Switch to the max layer (Pacman)
                    value = self.alphabeta(depth - 1, 0, successor, alpha, beta)
                else:
                    # Stay in the min layer (Ghosts)
                    value = self.alphabeta(depth, agentIndex + 1, successor, alpha, beta)
                bestValue = min(bestValue, value)
                # Alpha-beta pruning
                if bestValue < alpha:
                    return bestValue
                beta = min(beta, bestValue)
            return bestValue

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        legalActions = gameState.getLegalActions(0)
        bestAction = None
        alpha = float('-inf')
        beta = float('inf')
        bestValue = float('-inf')
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            value = self.alphabeta(self.depth, 1, successor, alpha, beta)
            if value > bestValue:
                bestValue = value
                bestAction = action
            alpha = max(alpha, bestValue)
        return bestAction
        #given at project start
        #util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def expectimax(self, gameState, depth, agentIndex):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return (None, self.evaluationFunction(gameState))

        if agentIndex == 0:
            return self.max_value(gameState, depth)
        else:
            return self.exp_value(gameState, depth, agentIndex)

    def max_value(self, gameState, depth):
        bestAction = (None, float('-inf'))
        for legalAction in gameState.getLegalActions(0):
            nextAgent = (1 if depth % gameState.getNumAgents() == 0 else 0)
            succAction = legalAction if depth != self.depth * gameState.getNumAgents() else None
            succValue = self.expectimax(gameState.generateSuccessor(0, legalAction), depth - 1, nextAgent)
            bestAction = max(bestAction, (legalAction, succValue[1]), key=lambda x: x[1])
        return bestAction

    def exp_value(self, gameState, depth, agentIndex):
        legalActions = gameState.getLegalActions(agentIndex)
        averageScore = 0
        probability = 1.0 / len(legalActions)
        for legalAction in legalActions:
            nextAgent = (agentIndex + 1) % gameState.getNumAgents()
            bestAction = self.expectimax(gameState.generateSuccessor(agentIndex, legalAction), depth - 1, nextAgent)
            averageScore += bestAction[1] * probability
        return (None, averageScore)


    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        maxDepth = self.depth * gameState.getNumAgents()
        return self.expectimax(gameState, maxDepth, 0)[0]

        #util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    #attempt two
    pacmanPos = currentGameState.getPacmanPosition()
    foodGrid = currentGameState.getFood()
    capsuleList = currentGameState.getCapsules()
    ghostStates = currentGameState.getGhostStates()

    # If Pacman wins, return a high score
    if currentGameState.isWin():
        return float('inf')

    # If Pacman loses, return a low score
    if currentGameState.isLose():
        return -float('inf')

    # Initialize evaluation value
    evaluation = 0

    # Prioritize score
    evaluation += 1.5 * currentGameState.getScore()
    score = currentGameState.getScore()

    # Get Pacman's position
    pacmanPos = currentGameState.getPacmanPosition()

    # Evaluate the features
    # Calculate the closest distance to food
    # Prioritize eating food and capsules while penalizing proximity to ghosts
    foodDistances = [manhattanDistance(pacmanPos, food) for food in currentGameState.getFood().asList()]
    closestFoodDistance = min(foodDistances) if foodDistances else 0

    # Calculate the closest distance to capsules
    capsuleDistances = [manhattanDistance(pacmanPos, capsule) for capsule in currentGameState.getCapsules()]
    closestCapsuleDistance = min(capsuleDistances) if capsuleDistances else 0



    # Weigh the features using coefficients
    # The evaluation function combines these features
    # Prioritize eating food
    evaluation += -10 * foodGrid.count()
    # Prioritize eating capsules
    evaluation+= -20 * len(capsuleList)
    # Penalize proximity to ghosts
    evaluation += -5 * min(manhattanDistance(pacmanPos, ghost.getPosition()) for ghost in ghostStates)

    return evaluation
    #util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
