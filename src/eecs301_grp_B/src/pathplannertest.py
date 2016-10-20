from map import *
from Queue import *

#def backtrackPath(costMap):
    

def pathPlanner(startPos, startHeading, endPos, endHeading):
    currCost = 1
    pathMap = EECSMap()
    pathMap.clearCostMap()
    mapQueue = Queue()
    mapQueue.put(startPos)
    currPos = startPos
    currCost = 0
    pathMap.costMap[currPos[0]][currPos[1]] = 0
    visited = []
    visited.append(currPos)
    while mapQueue.empty() == False:
        currPos = mapQueue.get()
        currCost = pathMap.costMap[currPos[0]][currPos[1]]
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.North) == 0 and ([currPos[0]-1, currPos[1]] in visited) == False:
            mapQueue.put([currPos[0]-1, currPos[1]])
            visited.append([currPos[0]-1, currPos[1]])
            pathMap.costMap[currPos[0]-1][currPos[1]] = currCost+1
            print "North enqueue" + str(currPos[0]-1) + " " + str(currPos[1])
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.East) == 0 and ([currPos[0], currPos[1]+1] in visited) == False:
            mapQueue.put([currPos[0], currPos[1]+1])
            visited.append([currPos[0], currPos[1]+1])
            pathMap.costMap[currPos[0]][currPos[1]+1] = currCost+1
            print "East enqueue" + str(currPos[0]) + " " + str(currPos[1]+1)
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.South) == 0 and ([currPos[0]+1, currPos[1]] in visited) == False:
            mapQueue.put([currPos[0]+1, currPos[1]])
            visited.append([currPos[0]+1, currPos[1]])
            pathMap.costMap[currPos[0]+1][currPos[1]] = currCost+1
            print "South enqueue" + str(currPos[0]+1) + " " + str(currPos[1])
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.West) == 0 and ([currPos[0], currPos[1]-1] in visited) == False:
            mapQueue.put([currPos[0], currPos[1]-1])
            visited.append([currPos[0], currPos[1]-1])
            pathMap.costMap[currPos[0]][currPos[1]-1] = currCost+1
            print "West enqueue" + str(currPos[0]) + " " + str(currPos[1]-1)
        #if currPos == endPos:
        #    break
    pathMap.printCostMap()
    pathMap.printObstacleMap()
        
        
        
pathPlanner([0, 3], 0, [7, 7], 3)
    
    
