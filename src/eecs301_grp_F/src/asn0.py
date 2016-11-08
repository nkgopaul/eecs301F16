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

# Main function # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group F Control Node...")
    
    # call function to set motor position 
    motor_id1 = 1 #(actuators 1, 2, 3, 4...8)
    motor_id2 = 2 #(actuators 1, 2, 3, 4...8)
    motor_id3 = 3 #(actuators 1, 2, 3, 4...8)
    motor_id4 = 4 #(actuators 1, 2, 3, 4...8)
    motor_id5 = 5
    motor_id6 = 6
    motor_id7 = 7
    motor_id8 = 8
        
    target_val1 = 450 #0-1024 #for each actuator/motor
    target_val2 = 450 #0-1024
    target_val3 = 450 #0-1024
    target_val4 = 450 #0-1024
    target_val5 = 200
    target_val6 = 800
    target_val7 = 800
    target_val8 = 200
            
    response = setMotorTargetPositionCommand(motor_id5, target_val5)
    response = setMotorTargetPositionCommand(motor_id6, target_val6)
            
    response = setMotorTargetPositionCommand(motor_id7, target_val7)
    response = setMotorTargetPositionCommand(motor_id8, target_val8)
            
    incrementer = 30
     
    # control loop running at 10hz
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # call function to get sensor value
        port1 = 1 #DMS
        port2 = 2 #IR
        sensor_reading1 = getSensorValue(port1)
        sensor_reading2 = getSensorValue(port2)
        rospy.loginfo("Sensor value at port %d: %f", 1, sensor_reading1)
        rospy.loginfo("Sensor value at port %d: %f", 2, sensor_reading2)

        
        #   BEHAVIOR 1 - SPIN
        if sensor_reading2 > 250:
            response = setMotorTargetPositionCommand(motor_id1, target_val1)
            response = setMotorTargetPositionCommand(motor_id2, target_val2)
            response = setMotorTargetPositionCommand(motor_id3, target_val3)
            response = setMotorTargetPositionCommand(motor_id4, target_val4)
            
            target_val1 += incrementer
            target_val2 += incrementer
            target_val3 += incrementer
            target_val4 += incrementer
            
        if target_val1 > 600:
            incrementer = -30
        elif target_val1 < 400:
            incrementer = 30
        

        
        #   BEHAVIOR 2 - TETRIS
        if sensor_reading1 > 1800:
            #response = setMotorTargetPositionCommand(motor_id5, 200)
            #response = setMotorTargetPositionCommand(motor_id7, 800)
            
            response = setMotorTargetPositionCommand(motor_id6, 512)
            response = setMotorTargetPositionCommand(motor_id8, 512)
            
            # sleep to enforce loop rate
            rospy.sleep(1.5)
        
            response = setMotorTargetPositionCommand(motor_id5, 512)
            response = setMotorTargetPositionCommand(motor_id7, 512)
            
            response = setMotorTargetPositionCommand(motor_id6, 800)
            response = setMotorTargetPositionCommand(motor_id8, 200)
            
            # sleep to enforce loop rate
            rospy.sleep(1.5)
            
            response = setMotorTargetPositionCommand(motor_id5, target_val5)
            response = setMotorTargetPositionCommand(motor_id6, target_val6)
            
            response = setMotorTargetPositionCommand(motor_id7, target_val7)
            response = setMotorTargetPositionCommand(motor_id8, target_val8)
        
        # sleep to enforce loop rate
        r.sleep()
        
