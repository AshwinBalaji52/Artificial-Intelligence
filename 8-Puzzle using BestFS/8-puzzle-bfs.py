import copy
import time

def displayVertex(vertex):
    global vertexNumber
    print("|",vertex[0],"|",vertex[1],"|",vertex[2],"|")
    print("|",vertex[3],"|",vertex[4],"|",vertex[5],"|")
    print("|",vertex[6],"|",vertex[7],"|",vertex[8],"|","\n")
    
    print('Vertex:', vertexNumber)
    print('Depth:', len(vertex[9:]))
    print('Actions:', vertex[9:])
    print('____________________________________________________________________')
    print("\n")
    vertexNumber += 1

def checkResult(vertex):
    if vertex[:9]==finalVertex:
        displayVertex(vertex)
        return True
    if vertex[:9] not in visitedList:
        displayVertex(vertex)
        vertexList.append(vertex)
        visitedList.append(vertex[:9])
    return False

def heuristic(vertex):
    
    distance = 0
    for current, final in enumerate(vertex):
        currentRow = int(current/3)
        currentColumn = current%3
        finalRow = int(final/3)
        finalColumn = final%3
        distance += abs(currentRow-finalRow) + abs(currentColumn-finalColumn)
    return distance

if __name__ == '__main__':
    
    print("\t\t8-Puzzle : Greedy Best First Search\n")
    initialVertex = [1,5,4, 
                     3,7,2, 
                     6,8,0]
    
    finalVertex = [0,1,2, 
                   3,4,5, 
                   6,7,8]

    goal = False
    vertexNumber = 0
    visitedList = []
    vertexList = []
    vertexList.append(initialVertex)
    visitedList.append(initialVertex)
    displayVertex(initialVertex)
    t0 = time.time()

    while (not goal and not len(vertexList)==0):
        fList = []
        for vertex in vertexList:
            
            h = heuristic(vertex[:9])
            g = len(vertex[9:])
            f = g + h
            fList.append(f)
            
        currentVertex = vertexList.pop(fList.index(min(fList)))
        emptyPosition = currentVertex.index(0)
        
        if emptyPosition!=0 and emptyPosition!=1 and emptyPosition!=2:
            upVertex = copy.deepcopy(currentVertex)
            upVertex[emptyPosition] = upVertex[emptyPosition-3]
            upVertex[emptyPosition-3] = 0
            upVertex.append('Up')
            goal = checkResult(upVertex)
            
        if emptyPosition!=0 and emptyPosition!=3 and emptyPosition!=6 and goal==False:
            leftVertex = copy.deepcopy(currentVertex)
            leftVertex[emptyPosition] = leftVertex[emptyPosition-1]
            leftVertex[emptyPosition-1] = 0
            leftVertex.append('Left')
            goal = checkResult(leftVertex)
            
        if emptyPosition!=6 and emptyPosition!=7 and emptyPosition!=8 and goal==False:
            downVertex = copy.deepcopy(currentVertex)
            downVertex[emptyPosition] = downVertex[emptyPosition+3]
            downVertex[emptyPosition+3] = 0
            downVertex.append('Down')
            goal = checkResult(downVertex)
            
        if emptyPosition!=2 and emptyPosition!=5 and emptyPosition!=8 and goal==False:
            rightVertex = copy.deepcopy(currentVertex)
            rightVertex[emptyPosition] = rightVertex[emptyPosition+1]
            rightVertex[emptyPosition+1] = 0
            rightVertex.append('Right')
            goal = checkResult(rightVertex)
