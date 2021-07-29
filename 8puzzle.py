try:
   import Queue
except ImportError:
   import queue as Queue

### Part 1: define search state
class EightPuzzleState:
    def __init__(self, numberList):
        self.cells = []
        self.cells = numberList[:]
        for index in range(9):
            if (self.cells[index] == 0):
                self.blankLocation = index

    def goalState(self):
        if (self.cells == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
            return True
        else:
            return False

    def nextActions(self):
        actions = []
        index = self.blankLocation
        if (index%3!=2):
            actions.append('right')
        if (index%3!=0):
            actions.append('left')
        if (index>2):
            actions.append('up')
        if (index<6):
            actions.append('down')
        return actions

    def nextState(self, move):
        index = self.blankLocation
        newState = EightPuzzleState([0,0,0,0,0,0,0,0,0])
        newState.cells = self.cells[:]
        if move == 'up':
            newState.cells[index] = self.cells[index-3]
            newState.cells[index-3] = self.cells[index]
            newState.blankLocation = index-3
        if move == 'down':
            newState.cells[index] = self.cells[index+3]
            newState.cells[index+3] = self.cells[index]
            newState.blankLocation = index+3
        if move == 'right':
            newState.cells[index] = self.cells[index+1]
            newState.cells[index+1] = self.cells[index]
            newState.blankLocation = index+1
        if move == 'left':
            newState.cells[index] = self.cells[index-1]
            newState.cells[index-1] = self.cells[index]
            newState.blankLocation = index-1
        return newState

    def __str__(self):
        lines = []
        lines.append('---------')
        for n in [0, 3, 6]:
            newLine = '|'
            for cell in self.cells[n:n+3]:
                if cell == 0:
                    newLine += ' '
                else:
                    newLine += cell.__str__()
            newLine += '|'
            newLine = ' '.join(newLine)
            lines.append(newLine)
        lines.append('---------')
        lines = '\n'.join(lines)
        return lines

    def __eq__(self, other):
        return (self.cells == other.cells)

    def __hash__(self):
        return hash(str(self.cells))

### Part 2: define seacrh problem
class searchProblem:
    def __init__(self, state):
        self.state = state

    def currentState(self):
        return self.state

    def nextStates(self, state):
        next = []
        for action in state.nextActions():
            next.append((state.nextState(action), action, 1))
        return next

    def theEnd(self, state):
        return state.goalState()

### Part 3: define seacrh method
def missTile(state, problem=None):
    heur = 0
    for index in range(9):
        if state.cells[index] != index:
            heur += 1
    return heur

def algoVisit(problem, algo='ucs', heuristic=missTile):
    """
    'bfs'    = breadth first search
    'dfs'    = depth first search
    'ucs'    = uniform cost search
    'greedy' = greedy search
    'astar'  = A star search
    """    
    if algo == 'dfs':
        fringeQueue = Queue.LifoQueue()
    elif algo == 'bfs':
        fringeQueue = Queue.Queue()
    else:
        fringeQueue = Queue.PriorityQueue()
    visited = set([])
    path = ()
    cost = 0
    heur = 0
    node = problem.currentState()
    fringeQueue.put( (heur, (node, path, cost)) )
    while not fringeQueue.empty():
        # print(len(visited))
        (heur, (node, path, cost)) = fringeQueue.get() 
        if problem.theEnd(node):
            return path, visited
            break
        if node not in visited:
            successors = problem.nextStates(node)
            visited.add(node)   
        else:
            successors = []
        for successor in successors:
            if successor[0] not in visited:
                if algo == 'astar':
                    heur = cost+successor[2] + 1*heuristic(successor[0],problem)
                elif algo == 'greedy':
                    heur = heuristic(successor[0],problem)
                else: # 'ucs'
                    heur = cost+successor[2]
                fringeQueue.put( (heur, (successor[0], path+(successor[1],), cost+successor[2])) )

### Part 4: main program
if __name__ == '__main__':
    algo = 'astar'    # 'bfs', 'dfs', 'ucs', 'greedy', 'astar'
    numberList = [1, 7, 8, 2, 3, 4, 5, 6, 0]
        # [1, 0, 2, 3, 4, 5, 6, 7, 8]     # bfs: 2
        # [1, 2, 5, 3, 4, 8, 6, 7, 0]     # bfs: 16
        # [0, 3, 1, 6, 8, 2, 7, 5, 4]     # bfs: 16
        # [4, 3, 2, 7, 0, 5, 1, 6, 8]     # bfs: 781
        # [1, 2, 5, 7, 6, 8, 0, 4, 3]     # bfs: 3541
        # [5, 1, 3, 4, 0, 2, 6, 7, 8]     # bfs: 3842
        # bfs: 134450, 24
        # ucs: 134127, 24
        # greedy: 314, 66
    state = EightPuzzleState(numberList)
    problem = searchProblem(state)
    path, visited = algoVisit(problem, algo, )

    print('========================================')
    print('Need %d moves to solve this puzzle by %s: %s' %(len(path), algo, str(path)))
    print('========================================')
    print(state)
    i = 1
    for action in path:
        state = state.nextState(action)
        print('move#%d: %s' % (i, action))
        print(state)
        i += 1

    print('Total number of nodes visited by %s: %d ' %(algo, len(visited)))
