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

def setAllMotorWheelSpeeds(speed):
    setMotorWheelSpeed(1, speed)
    setMotorWheelSpeed(2, speed)
    setMotorWheelSpeed(3, speed)
    setMotorWheelSpeed(4, speed)
    setMotorWheelSpeed(5, speed)
    setMotorWheelSpeed(6, speed)
    setMotorWheelSpeed(7, speed)
    setMotorWheelSpeed(8, speed)

# walkPositionOne

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
    setMotorTargetPositionCommand(3, 819)
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

def walk():
    walkPositionOne()
        
    waitUntil = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntil > rospy.Time.now():
        1

    walkOneToTwo()

    waitUntilTwo = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntilTwo > rospy.Time.now():
        1

    walkPositionTwo()
        
    waitUntilThree = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntilThree > rospy.Time.now():
        1
            
    walkTwoToOne()
            
    waitUntilFour = rospy.Time.now() + rospy.Duration(0.1);
    while waitUntilFour > rospy.Time.now():
        1

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
    #setAllMotorWheelSpeeds(400)
    #defaultPosition()
    count = 0
    while not rospy.is_shutdown():
        # call function to get sensor value
        port = 2
        IRPort = 2
        DMSPort = 1
        
        # sensor_reading = getSensorValue(DMSPort)
        # rospy.loginfo("Sensor value at port %d: %f", 2, sensor_reading)

        # call function to set motor position
        # motor_id = 8
        # target_val = 200
        
        # response = setMotorTargetPositionCommand(motor_id, target_val)
        
        # walk()

       
        #if val == True:
        #    walkPositionTwo()
        #    val = False
        #else:
        #    walkPositionOne()
        #    val = True

        # sleep to enforce loop rate
        r.sleep()
