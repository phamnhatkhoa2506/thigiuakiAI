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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    from util import Stack

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    frontier = Stack()  # Stack to store nodes to be explored
    frontier.push((problem.getStartState(), [], set()))  # (state, path, visited set)
    
    while not frontier.isEmpty():
        state, path, visited = frontier.pop()
        
        if problem.isGoalState(state):
            
            print(path)
            print(len(visited))
            return path  # Return the path if goal is found
        
        if state not in visited:
            visited.add(state)
            
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    frontier.push((successor, path + [action], visited.copy()))
    
    return []  # Return an empty path if no solution is foundS

def breadthFirstSearch(problem):
    from util import Queue

    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """Search the shallowest nodes in the search tree first."""
    frontier = Queue()  # Hàng đợi để duyệt BFS
    start_state = problem.getStartState()
    frontier.push((start_state, []))  # Mỗi phần tử trong queue là (state, path)
    visited = set()

    while not frontier.isEmpty():
        state, path = frontier.pop()

        if state in visited:
            continue  # Bỏ qua các trạng thái đã thăm

        visited.add(state)

        if problem.isGoalState(state):
            print(len(path))
            return path  # Trả về đường đi nếu tìm thấy goal

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                frontier.push((successor, path + [action]))

    return []  # Trả về rỗng nếu không tìm thấy đường đi

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    from util import PriorityQueue

    frontier = util.PriorityQueue()  # Hàng đợi ưu tiên
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)  # (state, path, cost), priority = cost

    exploredSet = {}  # Lưu trạng thái đã thăm với chi phí tốt nhất

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()  # Lấy nút có chi phí thấp nhất

        if problem.isGoalState(state):
            print(len(path))
            return path  # Trả về đường đi đến goal

        if state not in exploredSet or cost < exploredSet[state]:  
            exploredSet[state] = cost  # Cập nhật chi phí nhỏ nhất

            for successor, action, stepCost in problem.getSuccessors(state):
                new_cost = cost + stepCost
                frontier.push((successor, path + [action], new_cost), new_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
