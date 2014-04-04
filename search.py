# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    visitados = []
    fringe = util.Stack() #El fringe es una pila
    actual = problem.getStartState() #Llama al estado inicial
    fringe.push((actual,[]))
    while not fringe.isEmpty(): #Mientras aun haya nodos que expandir
        node = fringe.pop()
        if not node[0] in visitados: 
            visitados.append(node[0]) 
            if problem.isGoalState(node[0]):
                return node[1] 
            
            successors = problem.getSuccessors(node[0])
            for successor in successors: 
                path = list(node[1]) 
                path.append(successor[1])
                fringe.push((successor[0], path)) #Anade a la pila las acciones necesarias para llegar a ese sucesor
        
    return failure

   
    
    
def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    visitados = []
    fringe = util.Queue() #Se usa una cola para el fringe
    actual = problem.getStartState() #Llama al estado inicial
    fringe.push((actual,[]))
    while not fringe.isEmpty(): #Mientras aun haya nodos que expandir
        node = fringe.pop() 
        if not node[0] in visitados: 
            visitados.append(node[0]) 
            if problem.isGoalState(node[0]):
                return node[1]             
            successors = problem.getSuccessors(node[0])
            for successor in successors: 
                path = list(node[1])                 
                path.append(successor[1])
                fringe.push((successor[0], path))
        
    return failure

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visitados = set()
    fringe = util.PriorityQueue() #En este caso es una cola de prioridad
    actual = problem.getStartState() #Llama al estado inicial
    fringe.push((actual,[]),0)
    while not fringe.isEmpty(): #Mientras aun haya nodos que expandir
        node = fringe.pop()
      
        if not node[0] in visitados: #Para evitar re-visitar nodos
            visitados.add(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            successors = problem.getSuccessors(node[0])
            for successor in successors:
                path = list(node[1])
                path.append(successor[1])
                fringe.push((successor[0],path),problem.getCostOfActions(path)) #Anade el costo del camino como prioridad a la cola de prioridad
                    
                               
    return failure
    


    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    visitados = set()
    fringe = util.PriorityQueue()
    actual = problem.getStartState() #Llama al estado inicial
    fringe.push((actual,[]),0)
    while not fringe.isEmpty():
        node = fringe.pop()
      
        if not node[0] in visitados: #Para evitar re-visitar nodos
            visitados.add(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            successors = problem.getSuccessors(node[0])
            for successor in successors:
                path = list(node[1])
                path.append(successor[1])
                fringe.push((successor[0],path),problem.getCostOfActions(path)+heuristic(successor[0],problem)) #Parecido a UCS, pero se suma la heuristica de cada estado al costo (backward cost)
                    
                               
    return failure



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
