#!/usr/bin/env python
import roslib
import rospy
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
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(2, 656)
    setMotorTargetPositionCommand(3, 656)
    setMotorTargetPositionCommand(4, 358)

    setMotorTargetPositionCommand(5, 300)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(7, 819)
    setMotorTargetPositionCommand(8, 300)   

     
def walkPositionTwo():
    setMotorTargetPositionCommand(1, 205)
    setMotorTargetPositionCommand(2, 512)
    setMotorTargetPositionCommand(3, 799)   #819 Modified to walk straight
    setMotorTargetPositionCommand(4, 512)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(7, 819)
    setMotorTargetPositionCommand(8, 205)
    
def walkTwoToOne():
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(2, 656)
    setMotorTargetPositionCommand(3, 656)
    setMotorTargetPositionCommand(4, 358)
    
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(6, 724)
    setMotorTargetPositionCommand(7, 724)
    setMotorTargetPositionCommand(8, 205)   

def walk(count):
    print count
    if count%4 == 0:
        walkPositionOne()
        count += 1
        print count
        return count
    elif count%4 == 1:
        walkOneToTwo()
        count += 1
        return count
    elif count%4 == 2:
        walkPositionTwo()
        count += 1
        return count
    elif count%4 == 3:
        walkTwoToOne()
        count += 1
        return count
def walkForward():
    walkPositionOne()
    walkOneToTwo()
    walkPositionTwo()
    walkTwoToOne()
        
# walk left

def walkLeftPositionOne():
    setMotorTargetPositionCommand(2, 512)
    setMotorTargetPositionCommand(4, 205)
    setMotorTargetPositionCommand(1, 512)
    setMotorTargetPositionCommand(3, 819)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(7, 819)
    
def walkLeftOneToTwo():
    setMotorTargetPositionCommand(2, 656)
    setMotorTargetPositionCommand(4, 358)
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(3, 656)

    setMotorTargetPositionCommand(6, 724)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(7, 724)   

     
def walkLeftPositionTwo():
    setMotorTargetPositionCommand(2, 779)
    setMotorTargetPositionCommand(4, 512)
    setMotorTargetPositionCommand(1, 205)   #819 Modified to walk straight
    setMotorTargetPositionCommand(3, 512)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(7, 819)
    
def walkLeftTwoToOne():
    setMotorTargetPositionCommand(2, 656)
    setMotorTargetPositionCommand(4, 358)
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(3, 656)
    
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(8, 300)
    setMotorTargetPositionCommand(5, 300)
    setMotorTargetPositionCommand(7, 819)

def walkLeft():
    walkLeftPositionOne()
    walkLeftOneToTwo()
    walkLeftPositionTwo()
    walkLeftTwoToOne()

# walk right

def walkRightPositionOne():
    setMotorTargetPositionCommand(3, 512)
    setMotorTargetPositionCommand(1, 205)
    setMotorTargetPositionCommand(4, 512)
    setMotorTargetPositionCommand(2, 819)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(7, 819)
    
def walkRightOneToTwo():
    setMotorTargetPositionCommand(3, 656)
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(4, 358)
    setMotorTargetPositionCommand(2, 656)

    setMotorTargetPositionCommand(6, 724)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(7, 724)   

     
def walkRightPositionTwo():
    setMotorTargetPositionCommand(3, 819)
    setMotorTargetPositionCommand(1, 462)
    setMotorTargetPositionCommand(4, 205)   #819 Modified to walk straight
    setMotorTargetPositionCommand(2, 512)
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(8, 205)
    setMotorTargetPositionCommand(5, 205)
    setMotorTargetPositionCommand(7, 819)
    
def walkRightTwoToOne():
    setMotorTargetPositionCommand(3, 656)
    setMotorTargetPositionCommand(1, 358)
    setMotorTargetPositionCommand(4, 358)
    setMotorTargetPositionCommand(2, 656)
    
    setMotorTargetPositionCommand(6, 819)
    setMotorTargetPositionCommand(8, 300)
    setMotorTargetPositionCommand(5, 300)
    setMotorTargetPositionCommand(7, 819)

def walkRight():
    walkRightPositionOne()
    walkRightOneToTwo()
    walkRightPositionTwo()
    walkRightTwoToOne()

# right turn

def rightTurn(turnIncrement):

    defaultPosition()
        
    waitUntil = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntil > rospy.Time.now():
        1
        
    setMotorTargetPositionCommand(1, 358 - turnIncrement)
    setMotorTargetPositionCommand(5, 300)

    waitUntilTwo = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilTwo > rospy.Time.now():
        1
    
    setMotorTargetPositionCommand(5, 205)
    
    setMotorTargetPositionCommand(2, 656 - turnIncrement)
    setMotorTargetPositionCommand(6, 724)
    waitUntilThree = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilThree > rospy.Time.now():
        1
    setMotorTargetPositionCommand(6, 819)  
        
    setMotorTargetPositionCommand(4, 358 - turnIncrement)
    setMotorTargetPositionCommand(8, 300)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(8, 205)    
    
    setMotorTargetPositionCommand(3, 656 - turnIncrement)
    setMotorTargetPositionCommand(7, 724)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(7, 819)
    
# left turn

def leftTurn(turnIncrement):

    defaultPosition()
    
    setMotorTargetPositionCommand(2, 656 + turnIncrement)
    setMotorTargetPositionCommand(6, 724)
    waitUntilThree = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilThree > rospy.Time.now():
        1
    setMotorTargetPositionCommand(6, 819)
        
    waitUntil = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntil > rospy.Time.now():
        1
        
    setMotorTargetPositionCommand(1, 358 + turnIncrement)
    setMotorTargetPositionCommand(5, 300)
    waitUntilTwo = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilTwo > rospy.Time.now():
        1
    setMotorTargetPositionCommand(5, 205)
    
    setMotorTargetPositionCommand(3, 656 + turnIncrement)
    setMotorTargetPositionCommand(7, 724)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(7, 819)
    
    setMotorTargetPositionCommand(4, 358 + turnIncrement)
    setMotorTargetPositionCommand(8, 300)
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1)
    while waitUntilFour > rospy.Time.now():
        1
    setMotorTargetPositionCommand(8, 205)

# turn right 90 degrees

def turnRight90Degrees():
    for i in range(0, 4):
        rightTurn(207)

# turn left 90 degrees

def turnLeft90Degrees():
    for i in range(0, 5):
        leftTurn(207)

# turn right 180 degrees

def turnRight180Degrees():
    for i in range(0, 9):
        rightTurn(200)

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
# swim

def swim(DMSThreshold):
    DMSPort = 1
    if DMSThreshold < getSensorValue(DMSPort):
        setMotorTargetPositionCommand(1, 200)
        setMotorTargetPositionCommand(2, 824)
        setMotorTargetPositionCommand(3, 824)
        setMotorTargetPositionCommand(4, 200)
        setMotorTargetPositionCommand(5, 412)
        setMotorTargetPositionCommand(6, 612)
        setMotorTargetPositionCommand(7, 612)
        setMotorTargetPositionCommand(8, 412)
        return True
    return False

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

# balancePositionOne

def balancePositionOne():
    IRPort = 2
    if getSensorValue(IRPort) > 0:
        setMotorTargetPositionCommand(1, 512)
        setMotorTargetPositionCommand(2, 640)
        setMotorTargetPositionCommand(3, 640)
        setMotorTargetPositionCommand(4, 215)
        setMotorTargetPositionCommand(5, 200)
        setMotorTargetPositionCommand(6, 612)
        setMotorTargetPositionCommand(7, 768)
        setMotorTargetPositionCommand(8, 200)
        return True
    return False

# balancePositionTwo

def balancePositionTwo():
    IRPort = 2
    if getSensorValue(IRPort) > 0:
        setMotorTargetPositionCommand(1, 256)
        setMotorTargetPositionCommand(2, 640)
        setMotorTargetPositionCommand(3, 640)
        setMotorTargetPositionCommand(4, 550)
        setMotorTargetPositionCommand(5, 200)
        setMotorTargetPositionCommand(6, 768)
        setMotorTargetPositionCommand(7, 612)
        setMotorTargetPositionCommand(8, 200)
        return True
    return False

# Main function
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group X Control Node...")

    # control loop running at 10hz
    r = rospy.Rate(10) # 10hz
    setAllMotorTargetSpeeds(300)
    defaultPosition()
    walkForwardCount = 0
    walkLeftCount = 0
    walkRightCount = 0
    DMSPort = 1
    IRPortLeft = 2
    IRPortRight = 3
    previousReading = 0
    currentReading = 0
    while not rospy.is_shutdown():
        # call function to get sensor value
        
        sensor_reading = getSensorValue(IRPortLeft)
        #rospy.loginfo("Sensor value at port %d: %f", IRPortLeft, sensor_reading)
        #temp = walk(walk_count)
        #walk_count = temp
        
        #temp = walkAlongWallRight(walk_count)
        if getSensorValue(IRPortLeft) > 100 and getSensorValue(IRPortLeft) < 180:
            previousReading = getSensorValue(IRPortLeft)
            if walkForwardCount == 0:
                walkPositionOne()
                walkForwardCount = 1
            elif walkForwardCount == 1:
                walkOneToTwo()
                walkForwardCount = 2
            elif walkForwardCount == 2:
                walkPositionTwo()
                walkForwardCount = 3
            elif walkForwardCount == 3:
                walkTwoToOne()
                walkForwardCount = 0
            currentReading = getSensorValue(IRPortLeft)
            rospy.loginfo(previousReading - currentReading)
            if currentReading - previousReading > 100:
                rightTurn(200)
            elif  previousReading - currentReading > 40:
                leftTurn(200)
        elif getSensorValue(IRPortLeft) >= 180:
            if walkRightCount == 0:
                walkRightPositionOne()
                walkRightCount = 1
            elif walkRightCount == 1:
                walkRightOneToTwo()
                walkRightCount = 2
            elif walkRightCount == 2:
                walkRightPositionTwo()
                walkRightCount = 3
            elif walkRightCount == 3:
                walkRightTwoToOne()
                walkRightCount = 0
        elif getSensorValue(IRPortLeft) <= 100:
            if walkLeftCount == 0:
                walkLeftPositionOne()
                walkLeftCount = 1
            elif walkLeftCount == 1:
                walkLeftOneToTwo()
                walkLeftCount = 2
            elif walkLeftCount == 2:
                walkLeftPositionTwo()
                walkLeftCount = 3
            elif walkLeftCount == 3:
                walkLeftTwoToOne()
                walkLeftCount = 0
        # call function to set motor position
        # motor_id = 8
        # target_val = 200
        
        # response = setMotorTargetPositionCommand(motor_id, target_val)
        
        #walk()

        # sleep to enforce loop rate
        r.sleep()
