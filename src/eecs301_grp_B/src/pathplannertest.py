from map import *
from Queue import *
import operator

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


    currPos = endPos
    lastPos = endPos
    currHeading = startHeading
    directions = []
    positions = []
    positions.append(endPos)
    
    while currPos != startPos:
        #print currHeading
        print currPos
        
        neighborsCost = []
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.North) == 0:
            neighborsCost.append(pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.North))
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.East) == 0:
            neighborsCost.append(pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.East))
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.South) == 0:
            neighborsCost.append(pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.South))
        if pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.West) == 0:
            neighborsCost.append(pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.West))
    
        #print neighborsCost
        
        minCost = min(neighborsCost)
        
        #DIRECTION = enum(North=1, East=2, South=3, West=4)
        
        if minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.North):
            
            currPos = [currPos[0]-1, currPos[1]]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

        elif minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.East):

            currPos = [currPos[0], currPos[1]+1]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

        elif minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.South):
            
            currPos = [currPos[0]+1, currPos[1]]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

        elif minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.West):

            currPos = [currPos[0], currPos[1]-1]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos


    commands = []
    for i in range(0,len(directions)):

        if ((directions[-i-1] == [-1,0] and currHeading == 3) or
            (directions[-i-1] == [0,-1] and currHeading == 2) or
            (directions[-i-1] == [1, 0] and currHeading == 1) or
            (directions[-i-1] == [0, 1] and currHeading == 4) ):
            commands.append("straight")
            currHeading = currHeading
        elif ((directions[-i-1] == [-1,0] and currHeading == 4) or
            (directions[-i-1] == [0,-1] and currHeading == 3) or
            (directions[-i-1] == [1, 0] and currHeading == 2) or
            (directions[-i-1] == [0, 1] and currHeading == 1) ):
            commands.append("left")
            currHeading = (currHeading + 3)%4
        elif ((directions[-i-1] == [-1,0] and currHeading == 1) or
            (directions[-i-1] == [0,-1] and currHeading == 4) or
            (directions[-i-1] == [1, 0] and currHeading == 3) or
            (directions[-i-1] == [0, 1] and currHeading == 2) ):
            commands.append("reverse")
            currHeading = (currHeading + 2)%4
        elif ((directions[-i-1] == [-1,0] and currHeading == 2) or
              (directions[-i-1] == [0,-1] and currHeading == 1) or
              (directions[-i-1] == [1, 0] and currHeading == 4) or
              (directions[-i-1] == [0, 1] and currHeading == 3) ):
            commands.append("right")
            currHeading = (currHeading + 1)%4
                
        if currHeading > 4:
            currHeading = currHeading - 4
        elif currHeading < 1:
            currHeading = currHeading + 4

    if (currHeading-endHeading)==1 or (currHeading-endHeading)==-3:
        commands.append("left turn")
    elif (currHeading-endHeading)==-1 or (currHeading-endHeading)==3:
        commands.append("right turn")
    elif (currHeading-endHeading)==2 or (currHeading-endHeading)==-2:
        commands.append("turn around")
    
    print commands
    return commands


pathPlanner([7, 6], 2, [0, 6], 1)
#DIRECTION = enum(North=1, East=2, South=3, West=4)
#directions north [1,0] east [0,-1] south [-1,0] west [0,1]

    
    
