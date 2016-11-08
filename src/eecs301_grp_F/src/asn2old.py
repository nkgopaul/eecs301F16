#!/usr/bin/env python
import roslib
import rospy
from math import *
from ast import literal_eval
from map import *
from fw_wrapper.srv import *

# -----------SERVICE DEFINITION-----------
# allcmd REQUEST DATA
# ---------
# string command_type
# int8 device_id
# int16 target_val
# int8 n_dev
# int8[] dev_ids
# int16[] target_vals

# allcmd RESPONSE DATA
# ---------
# int16 val
# --------END SERVICE DEFINITION----------

# ----------COMMAND TYPE LIST-------------
# GetMotorTargetPosition
# GetMotorCurrentPosition
# GetIsMotorMoving
# GetSensorValue
# GetMotorWheelSpeed
# SetMotorTargetPosition
# SetMotorTargetSpeed
# SetMotorTargetPositionsSync
# SetMotorMode
# SetMotorWheelSpeed

# wrapper function to call service to set a motor mode
# 0 = set target positions, 1 = set wheel moving
def setMotorMode(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorMode', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to get motor wheel speed
def getMotorWheelSpeed(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetMotorWheelSpeed', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set motor wheel speed
def setMotorWheelSpeed(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorWheelSpeed', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set motor target speed
def setMotorTargetSpeed(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorTargetSpeed', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to get sensor value
def getSensorValue(port):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetSensorValue', port, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set a motor target position
def setMotorTargetPositionCommand(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorTargetPosition', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to get a motor's current position
def getMotorPositionCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetMotorCurrentPosition', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to check if a motor is currently moving
def getIsMotorMovingCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetIsMotorMoving', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        
# call function to set motor position 
motor_id1 = 1 #(actuators 1, 2, 3, 4...8)
motor_id2 = 2 #(actuators 1, 2, 3, 4...8)
motor_id3 = 3 #(actuators 1, 2, 3, 4...8)
motor_id4 = 4 #(actuators 1, 2, 3, 4...8)
motor_id5 = 5
motor_id6 = 12
motor_id7 = 7
motor_id8 = 8

# Position Variables

sout = 512
rout = 212 # 2 4
lout = 812 # 1 3
rmid = 362
lmid = 662

# motor position values   
out_1 = 362 #0-1024 #for each actuator/motor
out_2 = 662 #0-1024
out_3 = 662 #0-1024
out_4 = 362 #0-1024

down_5 = 182
down_6 = 842
down_7 = 842
down_8 = 182

extend_1 = 212
extend_2 = 812
extend_3 = 812
extend_4 = 212

up_5 = 356
up_6 = 668
up_7 = 668
up_8 = 356

# Flags

up5 = False
up6 = False
up7 = False
up8 = False

extend1 = False
extend2 = False
extand3 = False
extend4 = False

        
#   #   #   #   O U R  F U N C T I O N S  #    #    #   #   #   #   #   #   #   #       
def walkMotion():
    #rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id5, up_5) # 
    response = setMotorTargetPositionCommand(motor_id1, extend_1) # L extend up
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id5, down_5) # 1 down
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id8, up_8)
    response = setMotorTargetPositionCommand(motor_id2, 512)
    response = setMotorTargetPositionCommand(motor_id3, extend_3)
    response = setMotorTargetPositionCommand(motor_id4, 512)
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id8, down_8)
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id6, up_6)
    response = setMotorTargetPositionCommand(motor_id2, extend_2)
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id6, down_6)
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id7, up_7)
    response = setMotorTargetPositionCommand(motor_id1, 512)
    response = setMotorTargetPositionCommand(motor_id4, extend_4)
    response = setMotorTargetPositionCommand(motor_id3, 512)
    rospy.sleep(0)
         
    response = setMotorTargetPositionCommand(motor_id7, down_7)
    rospy.sleep(0)

def turn90(direction): # 8 rounds to turn 90'// hahajklol it's 4
    for i in range(0, 6):
        if direction == "left":
            response = setMotorTargetPositionCommand(motor_id5, up_5) # L up
            response = setMotorTargetPositionCommand(motor_id1, 512) # L extend
            
            response = setMotorTargetPositionCommand(motor_id8, up_8) # L up
            response = setMotorTargetPositionCommand(motor_id4, 512) # L extend
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id5, down_5) # L down
            response = setMotorTargetPositionCommand(motor_id8, down_8) # L down
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id1, out_1)
            response = setMotorTargetPositionCommand(motor_id4, out_4)
            response = setMotorTargetPositionCommand(motor_id6, up_6) #balance?
            response = setMotorTargetPositionCommand(motor_id7, up_7)
            rospy.sleep(0)

            response = setMotorTargetPositionCommand(motor_id7, up_7) # L up
            response = setMotorTargetPositionCommand(motor_id3, extend_3) # L extend
            
            response = setMotorTargetPositionCommand(motor_id6, up_6) # L up
            response = setMotorTargetPositionCommand(motor_id2, extend_2) # L extend
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id7, down_7) # L down
            response = setMotorTargetPositionCommand(motor_id6, down_6) # L down
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id2, out_2)
            response = setMotorTargetPositionCommand(motor_id3, out_3)
            response = setMotorTargetPositionCommand(motor_id5, up_5) #balance?
            response = setMotorTargetPositionCommand(motor_id8, up_8)
            
            
        elif direction == "right":
            response = setMotorTargetPositionCommand(motor_id5, up_5) # L up
            response = setMotorTargetPositionCommand(motor_id1, extend_1) # L extend
            
            response = setMotorTargetPositionCommand(motor_id8, up_8) # L up
            response = setMotorTargetPositionCommand(motor_id4, extend_1) # L extend
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id5, down_5) # L down
            response = setMotorTargetPositionCommand(motor_id8, down_8) # L down
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id1, out_1)
            response = setMotorTargetPositionCommand(motor_id4, out_4)
            response = setMotorTargetPositionCommand(motor_id6, up_6) #balance?
            response = setMotorTargetPositionCommand(motor_id7, up_7)
            rospy.sleep(0)

            response = setMotorTargetPositionCommand(motor_id7, up_7) # L up
            response = setMotorTargetPositionCommand(motor_id3, 512) # L extend
            
            response = setMotorTargetPositionCommand(motor_id6, up_6) # L up
            response = setMotorTargetPositionCommand(motor_id2, 512) # L extend
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id7, down_7) # L down
            response = setMotorTargetPositionCommand(motor_id6, down_6) # L down
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id2, out_2)
            response = setMotorTargetPositionCommand(motor_id3, out_3)
            response = setMotorTargetPositionCommand(motor_id5, up_5) #balance?
            response = setMotorTargetPositionCommand(motor_id8, up_8)
            rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id1, out_1)
    response = setMotorTargetPositionCommand(motor_id2, out_2)
    response = setMotorTargetPositionCommand(motor_id3, out_3)
    response = setMotorTargetPositionCommand(motor_id4, out_4)
            
    response = setMotorTargetPositionCommand(motor_id5, down_5)
    response = setMotorTargetPositionCommand(motor_id6, down_6) 
    response = setMotorTargetPositionCommand(motor_id7, down_7)
    response = setMotorTargetPositionCommand(motor_id8, down_8)
    
def newTurn(td):

    for i in range(0, 4):
        response = setMotorTargetPositionCommand(motor_id1, out_1)
        response = setMotorTargetPositionCommand(motor_id2, out_2)
        response = setMotorTargetPositionCommand(motor_id3, out_3)
        response = setMotorTargetPositionCommand(motor_id4, out_4)
                
        response = setMotorTargetPositionCommand(motor_id5, down_5)
        response = setMotorTargetPositionCommand(motor_id6, down_6) 
        response = setMotorTargetPositionCommand(motor_id7, down_7)
        response = setMotorTargetPositionCommand(motor_id8, down_8)

        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id5, up_5) # L up
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id1, out_1+td) # L extend
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id5, down_5) # L up
        rospy.sleep(0)
        
        response = setMotorTargetPositionCommand(motor_id6, up_6) # L up
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id2, out_2+td) # L extend
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id6, down_6) # L up
        rospy.sleep(0)
        
        response = setMotorTargetPositionCommand(motor_id7, up_7) # L up
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id3, out_3+td) # L extend
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id7, down_7) # L up
        rospy.sleep(0)
        
        response = setMotorTargetPositionCommand(motor_id8, up_8) # L up
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id4, out_4+td) # L extend
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id8, down_8) # L up
        rospy.sleep(0)
        
        response = setMotorTargetPositionCommand(motor_id1, out_1) # L extend
        response = setMotorTargetPositionCommand(motor_id2, out_2) # L extend
        response = setMotorTargetPositionCommand(motor_id3, out_3) # L extend
        response = setMotorTargetPositionCommand(motor_id4, out_4) # L extend
   
    
def walkCell():
    print "Walk Forward"
    walkMotion()
    walkMotion()
    walkMotion()
    walkMotion()
    walkMotion()
    walkMotion()
    #walkMotion()
    #walkMotion()

def rightWalk():
    print "Turn Right"
    #turn90("right") # 5 rounds
    newTurn(-160) # - is right
    walkCell()
    

def leftWalk():
    print "Turn Left"
    #turn90("left") # 6 rounds and sliding
    newTurn(150)
    walkCell()
    
def walk30():
    walkCell()
    walkCell()
    walkCell()
    
def walk03():
    leftWalk()
    walkCell()
    walkCell()
    
def walk22():
    leftWalk()
    walkCell()
    rightWalk()
    walkCell()
    
    
# Sets the cost map to infinity for all spaces
# Used to initialize a cost map we don't know the distances to    
def setMapInf(myMap):
    for i in xrange(8):
        for j in xrange(8):
            myMap.setCost(i, j, "INF")
    
# Uses a breadth first search to find the minimum distance to each
# cell in the map given the obstacles    
def setCostMap(myMap, i, j):
    # Initialize queue
    q = []
    # Insert starting cell
    q.insert(0,(i,j))
    # Set start node cost to 0
    myMap.setCost(i, j, 0)
    
    # While our queue is not empty
    while len(q) > 0:
        # pop the queue entry and get its cost
        item = q.pop()
        cost = myMap.getCost(item[0], item[1])

        # Check neighbors of current item and find ones that are not blocked
        # and have a cost higher than one we can set. If from our current
        # cell we can reach a neighboring cell in a shorter distance than
        # what is currently there, then we update that cell's cost to be
        # our current cell's cost + 1
        
        if ((myMap.getNeighborObstacle(item[0], item[1], 1) == 0 )and (myMap.getNeighborCost(item[0], item[1], 1) > cost+1)): #north
            q.insert(0, (item[0]-1, item[1]))
            myMap.setNeighborCost(item[0], item[1], 1, cost+1)

            
        if ((myMap.getNeighborObstacle(item[0], item[1], 2) == 0) and (myMap.getNeighborCost(item[0], item[1], 2) > cost+1)): #east
            q.insert(0, (item[0], item[1]+1))
            myMap.setNeighborCost(item[0], item[1], 2, cost+1)

        
        if ((myMap.getNeighborObstacle(item[0], item[1], 3) == 0 )and( myMap.getNeighborCost(item[0], item[1], 3) > cost+1)): #south
            q.insert(0, (item[0]+1, item[1]))
            myMap.setNeighborCost(item[0], item[1], 3, cost+1)

        
        if ((myMap.getNeighborObstacle(item[0], item[1], 4) == 0 )and( myMap.getNeighborCost(item[0], item[1], 4) > cost+1)): #west
            q.insert(0, (item[0], item[1]-1))
            myMap.setNeighborCost(item[0], item[1], 4, cost+1)
  

# Find a sequence of commands to get to the goal (unfinished)
def findSequence(myMap, i, j):

    path = []
    cost = myMap.getCost(i,j)
    found = False
    curri = i
    currj = j
    while found == False:
    # north = 3, south = 1, east = 4, west = 2
        for direct in xrange (4):
            if (myMap.getNeighborCost(curri, currj, direct+1) == cost-1 and myMap.getNeighborObstacle(curri, currj, direct+1) == 0):
                 path.insert(0, direct+1)
                 if direct+1 == 1:
                    curri = curri - 1
                 if direct+1 == 2:
                    currj = currj + 1
                 if direct+1 == 3:
                    curri = curri + 1
                 if direct+1 == 4:
                    currj = currj - 1
                 break
        cost = cost - 1
        if cost == 0:
            found = True    
    return path
    
# Find path of cells we need to go through to reach the goal
def findPath(myMap, i, j):

    path = []
    path.insert(0, (i, j))
    cost = myMap.getCost(i,j)
    found = False
    curri = i
    currj = j
    while found == False:
    # north = 3, south = 1, east = 4, west = 2
        for direct in xrange (4):
            if myMap.getNeighborCost(curri, currj, direct+1) == cost-1 and myMap.getNeighborObstacle(curri, currj, direct+1) == 0:
                 #path.insert(0, direct+1)
                 if direct+1 == 1:
                    curri = curri - 1
                    path.insert(0, (curri, currj))
                 if direct+1 == 2:
                    currj = currj + 1
                    path.insert(0, (curri, currj))
                 if direct+1 == 3:
                    curri = curri + 1
                    path.insert(0, (curri, currj))
                 if direct+1 == 4:
                    currj = currj - 1
                    path.insert(0, (curri, currj))
                 break
        cost = cost - 1
        if cost == 0:
            found = True    
    return path

# Unfinished debug
def walkPath(myPath):

    for step in xrange (len(myPath)):
        if myPath[step] == 1:
           walkCell()
        if myPath[step] == 2:
           leftWalk()
        if myPath[step] == 3:
           curri = curri + 1
        if myPath[step] == 4:
           currj = currj - 1
           


def nextStep(head, direct):

# north = 3, south = 1, east = 4, west = 2

    if head == "south":
        if direct == 1:
            walkCell()
            return "south"
        
        elif direct == 2:
            rightWalk()
            return "west"
        
        #elif direct == 3:
        
        elif direct == 4:
            leftWalk()
            return "east"
    
    elif head == "east":
    
        if direct == 1:
            rightWalk()
            return "south"
        
        #elif direct == 2:
        
        elif direct == 3:
            leftWalk()
            return "north"
        
        elif direct == 4:
             walkCell()
             return "east"
    
    elif head == "north":
    
        #if direct == 1:
        
        if direct == 2:
            leftWalk()
            return "west"
        
        elif direct == 3:
             walkCell()
             return "north"
        
        elif direct == 4:
            rightWalk()
            return "east"
    
    elif head == "west":
    
        if direct == 1:
            leftWalk()
            return "south"
        
        elif direct == 2:
             walkCell()
             return "west"
        
        elif direct == 3:
            rightWalk()
            return "north"
        
        #elif direct == 4:
        
def nextCommandPrint(head, direct):

# north = 3, south = 1, east = 4, west = 2

    if head == "south":
        if direct == 1:
            print "Command: Forward"
            print "Heading: South"
            return "south"
        
        elif direct == 2:
            print "Command: Turn Right"
            print "Heading: West"
            return "west"
        
        #elif direct == 3:
        
        elif direct == 4:
            print "Command: Turn Left"
            print "Heading: East"
            return "east"
    
    elif head == "east":
    
        if direct == 1:
            print "Command: Turn Right"
            print "Heading: South"
            return "south"
        
        #elif direct == 2:
        
        elif direct == 3:
            print "Command: Turn Left"
            print "Heading: North"
            return "north"
        
        elif direct == 4:
            print "Command: Forward"
            print "Heading: East"
            return "east"
    
    elif head == "north":
    
        #if direct == 1:
        
        if direct == 2:
            print "Command: Turn Left"
            print "Heading: West"
            return "west"
        
        elif direct == 3:
            print "Command: Forward"
            print "Heading: North"
            return "north"
        
        elif direct == 4:
            print "Command: Turn Right"
            print "Heading: East"
            return "east"
    
    elif head == "west":
    
        if direct == 1:
            print "Command: Turn Left"
            print "Heading: South"
            return "south"
        
        elif direct == 2:
            print "Command: Forward"
            print "Heading: West"
            return "west"
        
        elif direct == 3:
            print "Command: Turn Right"
            print "Heading: North"
            return "north"
        
        #elif direct == 4:
        
        
        
def fixHeading(head, newHead):

# north = 3, south = 1, east = 4, west = 2
    print "Fixing Heading"

    if head == "south":
        if newHead == "north":
            newTurn(150)
            newTurn(150)
        
        elif newHead == "west":
            newTurn(-160)
        
        #elif direct == 3:
        
        elif newHead == "east":
            newTurn(150)
    
    elif head == "east":
    
        if newHead == "south":
            newTurn(-160)
        
        #elif direct == 2:
        
        elif newHead == "north":
            newTurn(150)
        
        elif newHead == "west":
            newTurn(150)
            newTurn(150)
    
    elif head == "north":
    
        #if direct == 1:
        
        if newHead == "east":
            newTurn(-160)
        
        elif newHead == "south":
            newTurn(150)
            newTurn(150)
        
        elif newTurn == "west":
            newTurn(150)
    
    elif head == "west":
    
        if newHead == "east":
            newTurn(150)
            newTurn(150)
        
        elif newHead == "south":
            newTurn(150)
        
        elif newTurn == "north":
            newTurn(-160)
        
        #elif direct == 4:

def runPath(seq, head, endHead):
    
    newDirection = head
    
    for i in xrange (len(seq)):
    
        newDirection = nextStep(newDirection, seq[i])
        print "Heading: " + newDirection
        
    fixHeading(newDirection, endHead) 
    print "Heading: " + endHead
        
def runMaze(start, end, head, endHead):
    
    
    setMapInf(myMap)
    setCostMap(myMap, start[0], start[1]) # START
    
    l = findSequence(myMap, end[0], end[1]) # PATH TO HERE
    
    newDir = head
    
    for i in xrange (len(l)):
    
        newDir = nextCommandPrint(newDir, l[i])
    
    runPath(l, head, endHead)
    

# Main function
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group X Control Node...")
    
    
    
    myMap = EECSMap()
    myMap.printObstacleMap()

    
    startTuple = literal_eval(raw_input("What is starting cell? (tuple) "))
    endTuple = literal_eval(raw_input("What is ending cell? (tuple) "))
    startHeading = (raw_input("what is your start heading? (north, south, east, west)"))
    endHeading = (raw_input("what is your end heading? (north, south, east, west)"))
    
    setMapInf(myMap)
    setCostMap(myMap, startTuple[0], startTuple[1]) # START
    
    myMap.printCostMap()
    
    print "north = 3, south = 1, east = 4, west = 2"
    print findSequence(myMap, endTuple[0], endTuple[1]) # PATH TO HERE
    print findPath(myMap, endTuple[0], endTuple[1]) # PATH TO HERE
    runMaze(startTuple, endTuple, startHeading, endHeading)
    

    # control loop running at 10hz
    r = rospy.Rate(4) # 10hz
    while not rospy.is_shutdown():
        # call function to get sensor value
        port = 5
        sensor_reading = getSensorValue(port)
        #rospy.loginfo("Sensor value at port %d: %f", 5, sensor_reading)

        # call function to set motor position
        motor_id = 1
        target_val = 450
        # response = setMotorTargetPositionCommand(motor_id, target_val)

        # sleep to enforce loop rate
        r.sleep()
