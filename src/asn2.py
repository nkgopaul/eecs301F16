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
    
def newTurnOld(td):

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
   
   
def make90Turn(direction):

    if direction == "right":
    
        setMotorWheelSpeed(10, 512) 
        setMotorWheelSpeed(11, 512) 
        rospy.sleep(0.92)
        
    if direction == "left":
    
        setMotorWheelSpeed(10, 1023+512) 
        setMotorWheelSpeed(11, 1023+512)
        rospy.sleep(0.97)
        
    setMotorWheelSpeed(10, 0) 
    setMotorWheelSpeed(11, 0)
    
        
    
def walkCell():
    print "Walk Forward"
    #walkMotion()
    #walkMotion()
    #walkMotion()
    #walkMotion()
    #walkMotion()
    #walkMotion()
    #walkMotion()
    #walkMotion()
    setMotorWheelSpeed(10, 512) ##
    setMotorWheelSpeed(11, 1023+522) ## + + turn right, + - move fwd

    
    rospy.sleep(3.65) # 3.75
    setMotorWheelSpeed(10, 0)
    setMotorWheelSpeed(11, 0)
    
def walkBack():
    print "Walk Back"
    setMotorWheelSpeed(10, 1023+512)
    setMotorWheelSpeed(11, 512)
    rospy.sleep(3.5)
    setMotorWheelSpeed(10, 0)
    setMotorWheelSpeed(11, 0)
    
def rightWalk():
    print "Turn Right"
    #turn90("right") # 5 rounds
    
    setMotorWheelSpeed(10, 512) 
    setMotorWheelSpeed(11, 512) 
    rospy.sleep(0.92) # 0.92
    
    walkCell()
    

def leftWalk():
    print "Turn Left"
    #turn90("left") # 6 rounds and sliding
    setMotorWheelSpeed(10, 1023+512) 
    setMotorWheelSpeed(11, 1023+512)
    rospy.sleep(0.93) # 0.97
    
    walkCell()

def stopWalk():
    setMotorWheelSpeed(10, 0)
    setMotorWheelSpeed(11, 0)
    
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
        if (item[0] < 0) or (item[0] >= myMap.getCostmapSize(True)) or (item[1] < 0) or (item[1] >= myMap.getCostmapSize(False)):
            continue
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
            make90Turn("left")
            make90Turn("left")
        
        elif newHead == "west":
            make90Turn("right")
        
        #elif direct == 3:
        
        elif newHead == "east":
            make90Turn("left")
    
    elif head == "east":
    
        if newHead == "south":
            make90Turn("right")
        
        #elif direct == 2:
        
        elif newHead == "north":
            make90Turn("left")
        
        elif newHead == "west":
            make90Turn("left")
            make90Turn("left")
    
    elif head == "north":
    
        #if direct == 1:
        
        if newHead == "east":
            make90Turn("right")
        
        elif newHead == "south":
            make90Turn("left")
            make90Turn("left")
        
        elif newHead == "west":
            make90Turn("left")
    
    elif head == "west":
    
        if newHead == "east":
            make90Turn("left")
            make90Turn("left")
        
        elif newHead == "south":
            make90Turn("left")
        
        elif newHead == "north":
            make90Turn("right")
        
        #elif direct == 4:


def retHeading(head, direction):

#DIRECTION = enum(North=1, East=2, South=3, West=4)

    if head == "south":
        if direction == "right":
            return 4
        
        elif direction == "left":
            return 2

        elif direction == "forward":
            return 3
    
    elif head == "east":
    
        if direction == "right":
            return 3
        
        elif direction == "left":
            return 1

        elif direction == "forward":
            return 2
    
    elif head == "north":
    
        if direction == "right":
            return 2
        
        elif direction == "left":
            return 4

        elif direction == "forward":
            return 1
    
    elif head == "west":
    
       if direction == "right":
            return 1
        
       elif direction == "left":
            return 3

       elif direction == "forward":
            return 4

def retCell(curr, dirr):

#DIRECTION = enum(North=1, East=2, South=3, West=4)

    if dirr == 1:
        return (curr[0]-1, curr[1])
    
    elif dirr == 2:
        return (curr[0], curr[1]+1)
    
    elif dirr == 3:
        return (curr[0]+1, curr[1])
        
    elif dirr == 4:
        return (curr[0], curr[1]-1)

def makeMove(curr, target, head):

#DIRECTION = enum(North=1, East=2, South=3, West=4)
    print(curr[0])
    print(target[0])
    print(head)
    if head == "south":
        if curr[0] < target[0]: #south
            walkCell()
            return "south"
            
        elif curr[0] > target[0]: #north
            walkBack()
            return "south"

        elif curr[1] > target[1]:#west
            rightWalk()
            return "west"
            
        elif curr[1] < target[1]: #east
            leftWalk()
            return "east"
    
    elif head == "east":
    
        if curr[0] < target[0]:
            rightWalk()
            return "south"
        
        elif curr[0] > target[0]:
            leftWalk()
            return "north"

        elif curr[1] > target[1]:
            walkBack()
            return "east"
            
        elif curr[1] < target[1]:
            walkCell()
            return "east"
    
    elif head == "north":
    
        if curr[0] < target[0]:
            walkBack()
            return "north"
        
        elif curr[0] > target[0]:
            walkCell()
            return "north"

        elif curr[1] > target[1]:
            leftWalk()
            return "west"
            
        elif curr[1] < target[1]:
            rightWalk()
            return "east"
    
    elif head == "west":
    
        if curr[0] < target[0]:
            leftWalk()
            return "south"
        
        elif curr[0] > target[0]:
            rightWalk()
            return "north"

        elif curr[1] > target[1]:
            walkCell()
            return "west"
            
        elif curr[1] < target[1]:
            walkBack()
            return "west"


def runPath(seq, head, endHead):
    
    newDirection = head
    
    for i in xrange (len(seq)):
    
        try:
            newDirection = nextStep(newDirection, seq[i])
            print "Heading: " + newDirection
            
        except KeyboardInterrupt:
            stopWalk()
            break  
        
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
    
def makeMap(start, head):

    stack = []
    stack.append(start)
    
    visitedMap = EECSMap()
    visitedMap.clearCostMap()
    visitedMap.clearObstacleMap()
    
    currHead = head;
    prev = start
    
    while len(stack) > 0:
        
        current = stack.pop()
        
        right_reading = getMedian(6)
        left_reading = getMedian(2)
        dms_reading = getMedian(1)
        
        #Backtracking
        
        if right_reading > 40 and left_reading > 40 and dms_reading > 1000:
        
            tempMap = visitedMap
            setMapInf(tempMap)
            setCostMap(tempMap, current[0], current[1]) # START
            runMaze(prev, current, currHead, "south")
            currHead = "south"
            
        elif (current != start):

            currHead = makeMove(prev, current, currHead)
            rospy.sleep(0)
    
        visitedMap.setCost(current[0], current[1], 1)
    
       

        #Set walls
        if right_reading > 40:
            visitedMap.setObstacle(current[0], current[1], 1, retHeading(currHead, "right"))
        if left_reading > 40:
            visitedMap.setObstacle(current[0], current[1], 1, retHeading(currHead, "left"))
        if dms_reading > 1000:
            visitedMap.setObstacle(current[0], current[1], 1, retHeading(currHead, "forward")) 
     
        # Add Cells to Stack
        
        if visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "right")) == 0 and visitedMap.getNeighborCost(current[0], current[1], retHeading(currHead, "right")) == 0:
        
            stack.append(retCell(current, retHeading(currHead, "right")))
            
            
        if visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "left")) == 0 and visitedMap.getNeighborCost(current[0], current[1], retHeading(currHead, "left")) == 0:
        
            stack.append(retCell(current, retHeading(currHead, "left")))
            
        if visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "forward")) == 0 and visitedMap.getNeighborCost(current[0], current[1], retHeading(currHead, "forward")) == 0:
        
            stack.append(retCell(current, retHeading(currHead, "forward")))
        
        # Set new prev
        prev = current
        visitedMap.printObstacleMap()
        print stack
        rospy.loginfo("Sensor Right at port %d: %f", 6, right_reading)
        rospy.loginfo("Sensor Left at port %d: %f", 2, left_reading)
        rospy.loginfo("Sensor Front at port %d: %f", 1, dms_reading)

def newDirection(head, direct):

#DIRECTION = enum(North=1, East=2, South=3, West=4)

    if head == "south":
        if direct == "right":
            return "west"
            
        elif direct == "left":
            return "east"
    
    elif head == "east":
    
        if direct == "right":
            return "south"
            
        elif direct == "left":
            return "north"
    
    elif head == "north":
    
        if direct == "right":
            return "east"
            
        elif direct == "left":
            return "west"
    
    elif head == "west":
    
        if direct == "right":
            return "north"
            
        elif direct == "left":
            return "south"

def keepRightWalk(start, head): # # # # # # # #  # # # # # # # #  # # # # # # # #  # # # # # # # #  
        
    visitedMap = EECSMap()
    visitedMap.clearCostMap()
    visitedMap.clearObstacleMap()
    
    currHead = head
    current = start
    
    while (True):
    
        try:
    
            right_reading = getMedian(6)
            left_reading = getMedian(2)
            dms_reading = getMedian(1)
            
            #Set walls
            if right_reading > 40:
                visitedMap.setObstacle(current[0], current[1], 1, retHeading(currHead, "right"))
            if left_reading > 40:
                visitedMap.setObstacle(current[0], current[1], 1, retHeading(currHead, "left"))
            if dms_reading > 1000:
                visitedMap.setObstacle(current[0], current[1], 1, retHeading(currHead, "forward")) 
         
            if visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "right")) == 0:
            
                make90Turn("right")
                currHead = newDirection(currHead, "right")
                rospy.sleep(0)
       
            elif visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "right")) == 1 and visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "forward")) == 1: 
            
                make90Turn("left")
                currHead = newDirection(currHead, "left")
                rospy.sleep(0)
                
            if visitedMap.getNeighborObstacle(current[0], current[1], retHeading(currHead, "forward")) == 0:
                walkCell()
                visitedMap.setCost(current[0], current[1], 1)
                current = retCell(current, retHeading(currHead, "forward"))
        
            visitedMap.printObstacleMap()    
            visitedMap.printCostMap()
            
            if (current == start):
                break
        
        except KeyboardInterrupt:
            stopWalk()
            return visitedMap
            break  
            
    return visitedMap
    

def getMedian(sensorPort):
    l = []
    for i in xrange(7):
        l.append(getSensorValue(sensorPort))
    l.sort()
    print l
    return l[3]
    
    
# Main function
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True, disable_signals=True)
    rospy.loginfo("Starting Group X Control Node...")
    
    # set wheels
    setMotorMode(10, 1) # left
    setMotorMode(11, 1) # right
    
    
    #makeMap((0,0), "south")
    
    stopWalk()
    
    myMap = EECSMap()#keepRightWalk((0,7), "south")
    setMapInf(myMap)
    myMap.printObstacleMap()
    myMap.printCostMap()

    
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
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # call function to get sensor value
        # sensor readings
        
        #right_reading = getSensorValue(6)
        #left_reading = getSensorValue(2)
        #dms_reading = getSensorValue(1)
        

        # call function to set motor position
        motor_id = 1
        target_val = 450
        # response = setMotorTargetPositionCommand(motor_id, target_val)

        # sleep to enforce loop rate
        r.sleep()
    
