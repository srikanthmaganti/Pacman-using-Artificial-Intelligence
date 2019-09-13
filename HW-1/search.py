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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    startState = (problem.getStartState(),[])#Getting start state from searchproblem
    
    visited = []#set of visited nodes
    
    stack = util.Stack()#using stack class in Util 
    
    stack.push(startState)#initiating the stack with starting state
    
    while stack.isEmpty()==False:#iterate with in the loop until stack gets empty
        
        vertex = stack.pop()
        (nextState,actions) = vertex
        if nextState not in visited:#checking next state everytime whether it is already visited or not
            
            visited.append(nextState)
            if(problem.isGoalState(nextState)):#checking whether the pac-man finally found the path
                
                
                return actions#if so return the path
            successorsList = list(problem.getSuccessors(nextState))#list of successors
            
            for k in successorsList:
                if(k[0] not in visited):#checking whether the state already in visited
                    
                    
                    updatedActions = actions + [k[1]]#if so sum up the action with previous actions 
                    
                    stack.push((k[0],updatedActions))#push the state in the stack
    
    return []#return Empty action List if No Solution is Found
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    startState = (problem.getStartState(),[])#Getting start state from searchproblem
    
    visited = []#A set of visited nodes
    #An empty Queue 
    Q = util.Queue()#using queue class in Util
    
    Q.push(startState)#Push the initial state
    while Q.isEmpty() == False:#checking whether the queue is empty or not
        
        vertex = Q.pop()
        nextState,actions = vertex
        if nextState not in visited:#checking next state everytime whether it is already visited or not
            visited.append(nextState)
            if(problem.isGoalState(nextState)):#checking whether the pac-man finally found the path
                return actions#if so return the path
            successorsList = list(problem.getSuccessors(nextState))#list of successors
            for k in successorsList:
                if(k[0] not in visited):#checking whether the state already in visited
                    updatedActions = actions + [k[1]]#if so sum up the action with previous actions
                    Q.push((k[0],updatedActions))#push the state in the Queue
    #return Empty action List if No Solution is Found
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    startState = (problem.getStartState(),[])#Getting start state from searchproblem
    importance  = 0#importance based on cost
    
    visited = []#A set of visited nodes
     
    priorityQ = util.PriorityQueue()#using priorityqueue class in Util
    priorityQ.push(startState,importance)#Push the initial state
    while priorityQ.isEmpty()==False:#checking whether the priorityqueue is empty or not
        vertex = priorityQ.pop()
        (nextState,actions) = vertex
        if nextState not in visited:#checking next state everytime whether it is already visited or not
            visited.append(nextState)
            if(problem.isGoalState(nextState)):#checking whether the pac-man finally found the path
                return actions#if so return the path
            successorsList = list(problem.getSuccessors(nextState))#list of successors
            for k in successorsList:
                if(k[0] not in visited):#checking whether the state already in visited
                    updatedActions = actions + [k[1]]#if so sum up the action with previous actions
                    updated_imp = problem.getCostOfActions(updatedActions)#update the importance of least cost
                    priorityQ.update((k[0],updatedActions),updated_imp)#push the state in the priorityQueue
    #return Empty action List if No Solution is Found
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = (problem.getStartState(),[])#Getting start state from searchproblem
    importance  = heuristic(problem.getStartState(),problem)#importance based on heursitic value and cost 
    #print("assigned importance")
    
    visited = []#A set of visited nodes
    
    priorityQ = util.PriorityQueue()#using priorityqueue class in Util
    priorityQ.push(startState,importance)#Push the initial state
    while priorityQ.isEmpty()==False:#checking whether the priorityqueue is empty or not
        vertex = priorityQ.pop()
        (nextState,actions) = vertex
        if nextState not in visited:#checking next state everytime whether it is already visited or not
            visited.append(nextState)
            if(problem.isGoalState(nextState)):#checking whether the pac-man finally found the path
                return actions#if so return the path
            successorsList = list(problem.getSuccessors(nextState))#list of successors
            for k in successorsList:
                if(k[0] not in visited):#checking whether the state already in visited
                    updatedActions = actions + [k[1]]#if so sum up the action with previous actions
                    updated_imp = heuristic(k[0],problem)+problem.getCostOfActions(updatedActions)#update the importance of least cost and heuristic value
                    priorityQ.update((k[0],updatedActions),updated_imp)#push the state in the priorityQueue
    #return Empty action List if No Solution is Found
    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
