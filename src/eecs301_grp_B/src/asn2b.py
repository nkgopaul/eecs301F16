#!/usr/bin/env python
import roslib
import signal
import sys
import rospy
from fw_wrapper.srv import *
from map import *
from math import floor
from Queue import *
import operator
import numpy

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
def setMotorMode(motor_id, target_val): #set target val to 1, to run setmotorwheelspeed, wheels will keep spinning after shutdown, need to catch that and set to zero 
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

# setAllMotorWheelSpeeds

def setAllMotorTargetSpeeds(speed):
    setMotorTargetSpeed(1, speed)
    setMotorTargetSpeed(2, speed)
    setMotorTargetSpeed(3, speed)
    setMotorTargetSpeed(4, speed)
    setMotorTargetSpeed(5, speed)
    setMotorTargetSpeed(6, speed)
    setMotorTargetSpeed(7, speed)
    setMotorTargetSpeed(8, speed)

# walk forward

def walkPositionOne():
    setMotorTargetPositionCommand(1, 512)
    setMotorTargetPositionCommand(2, 819)
    setMotorTargetPositionCommand(3, 512)
    setMotorTargetPositionCommand(4, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(7, 819)
    setMotorTargetPositionCommand(8, 205)
    
def walkOneToTwo():
    setMotorTargetPositionCommand(5, 300)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(7, 819)
    setMotorTargetPositionCommand(8, 300) 

    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(2, 666)
    setMotorTargetPositionCommand(3, 666)
    setMotorTargetPositionCommand(4, 358) 
    
    #setMotorTargetPositionCommand(8, 300) #300
   

     
def walkPositionTwo():
    setMotorTargetPositionCommand(2, 512)
    setMotorTargetPositionCommand(1, 205)
    
    setMotorTargetPositionCommand(4, 512)
    setMotorTargetPositionCommand(3, 819)   
    
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(5, 205)
    
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(7, 819)
    
    
def walkTwoToOne():
    setMotorTargetPositionCommand(6, 724)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(7, 724)

    setMotorTargetPositionCommand(2, 666)
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(4, 358)
    setMotorTargetPositionCommand(3, 666)    
    #setMotorTargetPositionCommand(7, 724) #724   

def walkForward():
    walkPositionOne()
    walkOneToTwo()
    walkPositionTwo()
    walkTwoToOne()
    print("walked one step")

# right turn

def rightTurn(turnIncrement):
    turnDegree = turnIncrement
    if turnIncrement > 230:
        turnDegree = 230
    defaultPosition()
        
    waitUntil = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntil > rospy.Time.now():
        1
        
    setMotorTargetPositionCommand(1, 358 - turnDegree)
    setMotorTargetPositionCommand(5, 300)

    waitUntilTwo = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilTwo > rospy.Time.now():
        1
    
    setMotorTargetPositionCommand(5, 205)
    
    setMotorTargetPositionCommand(2, 656 - turnDegree)
    setMotorTargetPositionCommand(6, 724)
    waitUntilThree = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilThree > rospy.Time.now():
        1
    setMotorTargetPositionCommand(6, 819)  
        
    setMotorTargetPositionCommand(4, 358 - turnDegree)
    setMotorTargetPositionCommand(8, 300)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(8, 205)    
    
    setMotorTargetPositionCommand(3, 656 - turnDegree)
    setMotorTargetPositionCommand(7, 724)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(7, 819)
    
# left turn

def leftTurn(turnIncrement):
    turnDegree = turnIncrement
    if turnIncrement > 230:
        turnDegree = 230
    
    defaultPosition()
    
    setMotorTargetPositionCommand(2, 656 + turnDegree)
    setMotorTargetPositionCommand(6, 724)
    waitUntilThree = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilThree > rospy.Time.now():
        1
    setMotorTargetPositionCommand(6, 819)
        
    waitUntil = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntil > rospy.Time.now():
        1
        
    setMotorTargetPositionCommand(1, 358 + turnDegree)
    setMotorTargetPositionCommand(5, 300)
    waitUntilTwo = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilTwo > rospy.Time.now():
        1
    setMotorTargetPositionCommand(5, 205)
    
    setMotorTargetPositionCommand(3, 656 + turnDegree)
    setMotorTargetPositionCommand(7, 724)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(7, 819)
    
    setMotorTargetPositionCommand(4, 358 + turnDegree)
    setMotorTargetPositionCommand(8, 300)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(8, 205)

# turn right 90 degrees

def turnRight90Degrees():
    for i in range(0, 5):
        rightTurn(175)
    defaultPosition()

# turn left 90 degrees

def turnLeft90Degrees():
    for i in range(0, 5):
        leftTurn(175)
    defaultPosition()

# turn right 180 degrees

def turnRight180Degrees():
    for i in range(0, 2):
        turnRight90Degrees()
    defaultPosition()

# walk along wall right
def walkAlongWallRight(count):
    if getSensorValue(3) > 80 and getSensorValue(3) < 220:
        return walk(count)
    elif getSensorValue(3) >= 190: #150 center value
        leftTurn(100)
        return count
    else:
        rightTurn(100)
        return count

# defaultPosition

def defaultPosition():
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(2, 656)
    setMotorTargetPositionCommand(3, 656)
    setMotorTargetPositionCommand(4, 358)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(7, 819)
    setMotorTargetPositionCommand(8, 205)

# walk 1 tile forward
def walkForwardSquare(squares):

    if squares==1:
        cycles = 2*squares
        for i in range(0,int(floor(cycles))):
            walkForward()
        walkPositionOne()
    elif squares==2:
        cycles = 2*squares
        for i in range(0,int(floor(cycles))):
            walkForward()
        
        walkPositionOne()
        walkOneToTwo()
        walkPositionTwo()
    
    
    #if (floor(cycles) - cycles*2.5) != 0:
    #    walkPositionOne()
    #    walkOneToTwo()
    #    walkPositionTwo()

# Wheel Functions

def wait(seconds):
    initialTime = rospy.Time.now()
    while rospy.Time.now() < initialTime + rospy.Duration(seconds):
        continue


# set modes of all motors 
def setMotorModes():
    setMotorMode(1, 1)
    setMotorMode(2, 1)
    setMotorMode(3, 1)
    setMotorMode(4, 1)

# set speed of all motors

# shutdown all motors
def shutdown(sig, stackframe):
    rospy.loginfo("Setting wheels to zero")
    for wheel in [1, 2, 3, 4]:
        setMotorWheelSpeed(wheel, 0)
    sys.exit(0)

#set all wheel speeds to zero
def setWheelsToZero():
    for wheel in [4, 1, 3, 2]:
        setMotorWheelSpeed(wheel, 0)

#Drive forward (numberOfSquares)

def driveForward(time):
    IRPortLeft = 2
    IRPortRight = 3   
    
    setMotorWheelSpeed(1, 509)
    setMotorWheelSpeed(2, 1533)
    setMotorWheelSpeed(3, 509)
    setMotorWheelSpeed(4, 1533)
    wait(time)
    setWheelsToZero()


#Turn left

def wTurnRight():
    setMotorWheelSpeed(1, 460)
    setMotorWheelSpeed(2, 460)
    setMotorWheelSpeed(3, 460)
    setMotorWheelSpeed(4, 460)
    wait(2)
    setWheelsToZero()
    #left wheels forward, right wheels backwards
    #time, then set motor wheel speed to zero for each, or just cont driving straight
    return
    
#Turn right

def wTurnLeft():
    setMotorWheelSpeed(1, 1500)
    setMotorWheelSpeed(2, 1400)
    setMotorWheelSpeed(3, 1400)
    setMotorWheelSpeed(4, 1500)
    wait(2.45)
    setWheelsToZero()
    return

#Turn around

def wTurnAround():
    wTurnRight()
    wTurnRight()
    return

# path planner

def pathPlanner(s1, s2, startHeading, e1, e2):
    startPos = [int(s1), int(s2)]
    endPos = [int(e1), int(e2)]
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
        
        if minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.North) and pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.North) == 0:
            
            currPos = [currPos[0]-1, currPos[1]]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

        elif minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.East) and pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.East) == 0:

            currPos = [currPos[0], currPos[1]+1]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

        elif minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.South) and pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.South) == 0:
            
            currPos = [currPos[0]+1, currPos[1]]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

        elif minCost == pathMap.getNeighborCost(currPos[0],currPos[1], DIRECTION.West) and pathMap.getNeighborObstacle(currPos[0], currPos[1], DIRECTION.West) == 0:

            currPos = [currPos[0], currPos[1]-1]
            positions.append(currPos)
            directions.append(list(map(operator.sub, currPos, lastPos)))
            lastPos = currPos

    print startPos
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

    while i < len(commands):
            count = 1
            if i+count < len(commands)-1:
                while commands[i+count] == "straight":
                    count = count + 1
                    if i+count > len(commands)-1:
                        break;
            print str(i) + "th command is " + commands[i]
            if commands[i] == "straight":
                DriveForward()
            elif commands[i] == "left":
                wTurnLeft()
                DriveForward()
            elif commands[i] == "right":
                wTurnRight()
                DriveForward()
            elif commands[i] == "reverse":
                wTurnAround()
                DriveForward()
                
    return currHeading

def updateWheelSpeed():

    feedbackConstant = .01

    DMSPort = 1
    IRPortLeft = 2
    IRPortRight = 3
    desiredIRLeft = 300 #630 # need to change this to be equal on both sides
    desiredIRRight = 300 #1150 
    
    wheelSpeedLeft = 500
    wheelSpeedRight = 1028+500

    if getSensorValue(IRPortLeft) != 0 and getSensorValue(IRPortLeft) > desiredIRLeft:
        wheelSpeedRight = wheelSpeedRight + feedbackConstant*(desiredIRLeft-getSensorValue(IRPortLeft))
    elif getSensorValue(IRPortRight) != 0 and getSensorValue(IRPortRight) > desiredIRRight:
        wheelSpeedLeft = wheelSpeedLeft + feedbackConstant*(desiredIRRight-getSensorValue(IRPortRight))

    setMotorWheelSpeed(1, wheelSpeedLeft)
    setMotorWheelSpeed(2, wheelSpeedRight)
    setMotorWheelSpeed(3, wheelSpeedLeft)
    setMotorWheelSpeed(4, wheelSpeedRight)



def DriveForward():

    cumulativeTime = 0
    walkTime = 0.78  # should be unit time for a square
    
    while cumulativeTime < walkTime:
        
        updateWheelSpeed()
        currentTime = rospy.Time.now() + rospy.Duration(0.1)
        
        while currentTime > rospy.Time.now():
            1

        cumulativeTime = cumulativeTime + 0.1

    setMotorWheelSpeed(1, 0)
    setMotorWheelSpeed(2, 0)
    setMotorWheelSpeed(3, 0)
    setMotorWheelSpeed(4, 0)

def HeadingConvert(heading):

    if heading > 4:
        heading = heading - 4
    elif heading < 1:
        heading = heading + 4
        
    return heading

def CheckExplored(currHeading, direction, currPos, visitedMap):
    
    if direction == "straight":
        if currHeading == 1 and currPos[0]-1 >= 0:
            return visitedMap[currPos[0]-1, currPos[1]]
        elif currHeading == 2 and currPos[1]+1 <= 7:
            return visitedMap[currPos[0], currPos[1]+1]
        elif currHeading == 3 and currPos[0]+1 <= 7:
            return visitedMap[currPos[0]+1, currPos[1]]
        elif currHeading == 4 and currPos[1]-1 >= 0:
            return visitedMap[currPos[0], currPos[1]-1]
    elif direction == "right":
        if currHeading == 1 and currPos[1]+1 <= 7:
            return visitedMap[currPos[0], currPos[1]+1]
        elif currHeading == 2 and currPos[0]+1 <= 7:
            return visitedMap[currPos[0]+1, currPos[1]]
        elif currHeading == 3 and currPos[1]-1 >= 0:
            return visitedMap[currPos[0], currPos[1]-1]
        elif currHeading == 4 and currPos[0]-1 >= 0:
            return visitedMap[currPos[0]-1, currPos[1]]
    elif direction == "left":
        if currHeading == 1 and currPos[1]-1 >= 0:
            return visitedMap[currPos[0], currPos[1]-1]
        elif currHeading == 2 and currPos[0]-1 >= 0:
            return visitedMap[currPos[0]-1, currPos[1]]
        elif (currHeading == 3) and (currPos[1]+1 <= 7):
            return visitedMap[currPos[0], currPos[1]+1]
        elif currHeading == 4 and currPos[0]+1 <= 7:
            return visitedMap[currPos[0]+1, currPos[1]]
            
def UpdateCurrentPosition(currPos, currHeading):

    if currHeading == 1:
        return [currPos[0]-1, currPos[1]]
    elif currHeading == 2:
        return [currPos[0], currPos[1]+1]
    elif currHeading == 3:
        return [currPos[0]+1, currPos[1]]
    elif currHeading == 4:
        return [currPos[0], currPos[1]-1]
        

# Main function
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group X Control Node...")
    
    signal.signal(signal.SIGINT, shutdown)
    # control loop running at 10hz
    r = rospy.Rate(10) # 10hz
    setMotorModes();


    DMSPort = 1
    IRPortLeft = 2
    IRPortRight = 3
    TIME_FORWARD = 3.4
    DMSThreshold = 1200
    IR_RIGHT_THRESHOLD = 1150
    IR_LEFT_THRESHOLD = 630
    
    currHeading = 3
    currPos = [0,0]
    visitedMap = numpy.zeros((8,8))
    decisionPosArr = []
    
    pathMap = EECSMap()
    
    while not rospy.is_shutdown():
            
        
        #print getSensorValue(IRPortRight)
        
        # call function to get sensor value
        
        #rospy.loginfo("Sensor value at port %d: %f", IRPortLeft, sensor_reading)
        #startPos = [int(sys.argv[0][1])

        print currPos
        print decisionPosArr
        visitedMap[currPos[0], currPos[1]] = 1        

        DMS = getSensorValue(DMSPort)
        rospy.loginfo("Sensor value at port %d: %f", DMSPort, DMS)
        IRRight = getSensorValue(IRPortRight)
        IRLeft = getSensorValue(IRPortLeft)
        
        if (DMS < DMSThreshold) and (IRRight > 0) and (IRLeft > 0):
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS >= DMSThreshold) and (IRRight == 0) and (IRLeft > 0):
            wTurnRight()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            currHeading = HeadingConvert((currHeading+1)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS >= DMSThreshold) and (IRRight > 0) and (IRLeft == 0):
            wTurnLeft()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            currHeading = HeadingConvert((currHeading+3)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
            ######################################################## multiple unexplored #############################################################################################
            
        elif (DMS < DMSThreshold) and (IRRight == 0) and (IRLeft > 0) and (not CheckExplored(currHeading, "right", currPos, visitedMap)) and (not CheckExplored(currHeading, "straight", currPos, visitedMap)):        
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            decisionPosArr.append(currPos)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS < DMSThreshold) and (IRRight > 0) and (IRLeft == 0) and (not CheckExplored(currHeading, "left", currPos, visitedMap)) and (not CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            decisionPosArr.append(currPos)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS >= DMSThreshold) and (IRRight == 0) and (IRLeft == 0) and (not CheckExplored(currHeading, "right", currPos, visitedMap)) and (not CheckExplored(currHeading, "left", currPos, visitedMap)):
       
            wTurnRight()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            decisionPosArr.append(currPos)
            currHeading = HeadingConvert((currHeading+1)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS < DMSThreshold) and (IRRight == 0) and (IRLeft == 0) and (not CheckExplored(currHeading, "right", currPos, visitedMap)) and (not CheckExplored(currHeading, "left", currPos, visitedMap)) and (not CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            decisionPosArr.append(currPos)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
            ################################################################ unexplored and explored #################################################################
            
        elif (DMS < DMSThreshold) and (IRRight == 0) and (IRLeft > 0) and (CheckExplored(currHeading, "right", currPos, visitedMap)) and (not CheckExplored(currHeading, "straight", currPos, visitedMap)):
       
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            currPos = UpdateCurrentPosition(temp, currHeading)
            
        elif (DMS < DMSThreshold) and (IRRight == 0) and (IRLeft > 0) and (not CheckExplored(currHeading, "right", currPos, visitedMap)) and (CheckExplored(currHeading, "straight", currPos, visitedMap)):
       
            wTurnRight()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            currHeading = HeadingConvert((currHeading+1)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS < DMSThreshold) and (IRRight > 0) and (IRLeft == 0) and (CheckExplored(currHeading, "left", currPos, visitedMap)) and (not CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS < DMSThreshold) and (IRRight > 0) and (IRLeft == 0) and (not CheckExplored(currHeading, "left", currPos, visitedMap)) and (CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
            wTurnLeft()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, currHeading)
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            currHeading = HeadingConvert((currHeading+3)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS >= DMSThreshold) and (IRRight == 0) and (IRLeft == 0) and (CheckExplored(currHeading, "left", currPos, visitedMap)) and (not CheckExplored(currHeading, "right", currPos, visitedMap)):
        
            wTurnRight()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            currHeading = HeadingConvert((currHeading+1)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
        elif (DMS >= DMSThreshold) and (IRRight == 0) and (IRLeft == 0) and (not CheckExplored(currHeading, "left", currPos, visitedMap)) and (CheckExplored(currHeading, "right", currPos, visitedMap)):
        
            wTurnLeft()
            DriveForward()
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+3)%4))
            pathMap.setObstacle(currPos[0], currPos[1], 0, HeadingConvert((currHeading+1)%4))
            currHeading = HeadingConvert((currHeading+3)%4)
            currPos = UpdateCurrentPosition(currPos, currHeading)
            
            
            
            

            
        ################################################################### multiple explored openings ########################################################
            
        elif (DMS < DMSThreshold) and (IRRight == 0) and (IRLeft > 0) and (CheckExplored(currHeading, "right", currPos, visitedMap)) and (CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
           currHeading = pathPlanner(currPos[0], currPos[1], currHeading, decisionPosArr[-1][0], decisionPosArr[-1][1])
           currPos = [decisionPosArr[-1][0], decisionPosArr[-1][1]]
           decisionPosArr.pop([-1])
            
        elif (DMS < DMSThreshold) and (IRRight > 0) and (IRLeft == 0) and (CheckExplored(currHeading, "left", currPos, visitedMap)) and (CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
            currHeading = pathPlanner(currPos[0], currPos[1], currHeading, decisionPosArr[-1][0], decisionPosArr[-1][1])
            currPos = [decisionPosArr[-1][0], decisionPosArr[-1][1]]
            decisionPosArr.pop([-1])
            
        elif (DMS >= DMSThreshold) and (IRRight == 0) and (IRLeft == 0) and (CheckExplored(currHeading, "right", currPos, visitedMap)) and (CheckExplored(currHeading, "left", currPos, visitedMap)):
       
            currHeading = pathPlanner(currPos[0], currPos[1], currHeading, decisionPosArr[-1][0], decisionPosArr[-1][1])
            currPos = [decisionPosArr[-1][0], decisionPosArr[-1][1]]
            decisionPosArr.pop([-1])
            
        elif (DMS < DMSThreshold) and (IRRight == 0) and (IRLeft == 0) and (CheckExplored(currHeading, "right", currPos, visitedMap)) and (CheckExplored(currHeading, "left", currPos, visitedMap)) and (not CheckExplored(currHeading, "straight", currPos, visitedMap)):
        
            currHeading = pathPlanner(currPos[0], currPos[1], currHeading, decisionPosArr[-1][0], decisionPosArr[-1][1])
            currPos = [decisionPosArr[-1][0], decisionPosArr[-1][1]]
            decisionPosArr.pop([-1])      

        else:    
            currHeading = pathPlanner(currPos[0], currPos[1], currHeading, decisionPosArr[-1][0], decisionPosArr[-1][1])
            currPos = [decisionPosArr[-1][0], decisionPosArr[-1][1]]
            decisionPosArr.pop([-1])
       
        pathMap.printObstacleMap()
       
       
        r.sleep()