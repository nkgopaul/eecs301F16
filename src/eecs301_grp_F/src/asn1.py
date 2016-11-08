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

down_5 = 156
down_6 = 868
down_7 = 868
down_8 = 156

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
    rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id2, extend_2)
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id6, down_6)
    response = setMotorTargetPositionCommand(motor_id7, up_7)
    response = setMotorTargetPositionCommand(motor_id1, 512)
    response = setMotorTargetPositionCommand(motor_id4, extend_4)
    response = setMotorTargetPositionCommand(motor_id3, 512)
    rospy.sleep(0)
         
    response = setMotorTargetPositionCommand(motor_id7, down_7)

    

def newTurn_old():

    rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id5, up_5) # L up
    response = setMotorTargetPositionCommand(motor_id1, extend_1) # L extend
    rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id5, down_5) # L up
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id6, up_6) # L up
    response = setMotorTargetPositionCommand(motor_id6, 512) # L extend
    rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id6, down_6) # L up
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id7, up_7) # L up
    response = setMotorTargetPositionCommand(motor_id3, 512) # L extend
    rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id7, down_7) # L up
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id8, up_8) # L up
    response = setMotorTargetPositionCommand(motor_id4, extend_4) # L extend
    rospy.sleep(0)
    response = setMotorTargetPositionCommand(motor_id8, down_8) # L up
    rospy.sleep(0)
    
    response = setMotorTargetPositionCommand(motor_id1, out_1) # L extend
    response = setMotorTargetPositionCommand(motor_id2, out_2) # L extend
    response = setMotorTargetPositionCommand(motor_id3, out_3) # L extend
    response = setMotorTargetPositionCommand(motor_id4, out_4) # L extend
        
# # # # #  # # # # #  # # # # #  # # # # #  # # # # #  # # # # #  # # # # #  # # # # #  
degree = 0.0
   
def turn90(direction): # 8 rounds to turn 90'// hahajklol it's 4
    for i in range(0, 4):
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
            
def turn180(direction): # 16 rounds to turn 180' // or maybe 8 lel
    for i in range(0, 8):
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
            rospy.sleep(1)
            
            response = setMotorTargetPositionCommand(motor_id1, out_1)
            response = setMotorTargetPositionCommand(motor_id4, out_4)
            response = setMotorTargetPositionCommand(motor_id6, up_6) #balance?
            response = setMotorTargetPositionCommand(motor_id7, up_7)
            rospy.sleep(0)

            response = setMotorTargetPositionCommand(motor_id7, up_7) # L up
            response = setMotorTargetPositionCommand(motor_id3, 512) # L extend
            
            response = setMotorTargetPositionCommand(motor_id6, up_6) # L up
            response = setMotorTargetPositionCommand(motor_id2, 512) # L extend
            #rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id7, down_7) # L down
            response = setMotorTargetPositionCommand(motor_id6, down_6) # L down
            rospy.sleep(0)
            
            response = setMotorTargetPositionCommand(motor_id2, out_2)
            response = setMotorTargetPositionCommand(motor_id3, out_3)
            response = setMotorTargetPositionCommand(motor_id5, up_5) #balance?
            response = setMotorTargetPositionCommand(motor_id8, up_8)
            #rospy.sleep(0)
    # set back to default        
    response = setMotorTargetPositionCommand(motor_id1, out_1)
    response = setMotorTargetPositionCommand(motor_id2, out_2)
    response = setMotorTargetPositionCommand(motor_id3, out_3)
    response = setMotorTargetPositionCommand(motor_id4, out_4)
            
    response = setMotorTargetPositionCommand(motor_id5, down_5)
    response = setMotorTargetPositionCommand(motor_id6, down_6) 
    response = setMotorTargetPositionCommand(motor_id7, down_7)
    response = setMotorTargetPositionCommand(motor_id8, down_8)

def turnOnce(direction, degree):    #   #   #   #   #   #   #   #   #   #   #
    if direction == "left":
    
        response = setMotorTargetPositionCommand(motor_id1, 512)
        response = setMotorTargetPositionCommand(motor_id2, extend_2)
        response = setMotorTargetPositionCommand(motor_id3, 512)
        response = setMotorTargetPositionCommand(motor_id4, extend_4)
    
        response = setMotorTargetPositionCommand(motor_id5, up_5) # L up
        response = setMotorTargetPositionCommand(motor_id1, 512) # L extend
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id5, down_5) # L down
        rospy.sleep(0)
            
        response = setMotorTargetPositionCommand(motor_id8, up_8) # L up
        response = setMotorTargetPositionCommand(motor_id4, 512) # L extend
        rospy.sleep(0)
        response = setMotorTargetPositionCommand(motor_id8, down_8) # L down
        rospy.sleep(0)
            
        #response = setMotorTargetPositionCommand(motor_id5, down_5) # L down
        #response = setMotorTargetPositionCommand(motor_id8, down_8) # L down
        #rospy.sleep(0)
            
        response = setMotorTargetPositionCommand(motor_id1, out_1)
        response = setMotorTargetPositionCommand(motor_id4, out_4)
        
        response = setMotorTargetPositionCommand(motor_id6, up_6) #balance?
        response = setMotorTargetPositionCommand(motor_id7, up_7)
        rospy.sleep(0)

        response = setMotorTargetPositionCommand(motor_id7, up_7) # L up
        response = setMotorTargetPositionCommand(motor_id3, extend_3 * 1-degree) # L extend
            
        response = setMotorTargetPositionCommand(motor_id6, up_6) # L up
        response = setMotorTargetPositionCommand(motor_id2, extend_2 * 1-degree) # L extend
        rospy.sleep(0)
            
        response = setMotorTargetPositionCommand(motor_id7, down_7) # L down
        response = setMotorTargetPositionCommand(motor_id6, down_6) # L down
        rospy.sleep(0)
            
        response = setMotorTargetPositionCommand(motor_id2, out_2)
        response = setMotorTargetPositionCommand(motor_id3, out_3)
        response = setMotorTargetPositionCommand(motor_id5, up_5) #balance?
        #response = setMotorTargetPositionCommand(motor_id8, up_8)
        
            
            
    elif direction == "right": #    #   #   #   #   #   
        response = setMotorTargetPositionCommand(motor_id5, up_5) # L up
        response = setMotorTargetPositionCommand(motor_id1, extend_1 * (1-degree)) # L extend
        
        response = setMotorTargetPositionCommand(motor_id8, up_8) # L up
        response = setMotorTargetPositionCommand(motor_id4, extend_4 * (1-degree)) # L extend
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
        
    # set back to default    
    response = setMotorTargetPositionCommand(motor_id1, out_1)
    response = setMotorTargetPositionCommand(motor_id2, out_2)
    response = setMotorTargetPositionCommand(motor_id3, out_3)
    response = setMotorTargetPositionCommand(motor_id4, out_4)
            
    response = setMotorTargetPositionCommand(motor_id5, down_5)
    response = setMotorTargetPositionCommand(motor_id6, down_6) 
    response = setMotorTargetPositionCommand(motor_id7, down_7)
    response = setMotorTargetPositionCommand(motor_id8, down_8)

def newTurn(td):

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
    response = setMotorTargetPositionCommand(motor_id6, out_2+td) # L extend
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
    
    
def avoidObjects(): #   #   #   #   #   #   #   #   #   #   #   #   #   #
    if IRR_reading > 0: 
        turn90("left")
        turn90("left")
    elif IRL_reading > 0:
        turn90("right")
        turn90("right")
    elif DMS_reading > 250:
        turn180("right")
        turn180("right")
        
        
def wallFollow(): #   #   #   #   #   #   #   #   #   #   #   #   #   #
#speed variable
#too far turn towards
#too close turn away
#proportional control -> how much you turn
#proportional
#take sensor reading from IRL IRR
#multiply by constant
#larger sensor reading turn more

    # wall on left
    #if DMS_reading > 500:
     #   turnOnce("right", 0)
     
    if DMS_reading > 1000: #facing the wall
        rospy.loginfo("facing the wall - turning right")
        turn90("right") #turning right
        turn90("right") #turning right
        walkMotion()
        walkMotion()
        
    elif 0 < IRL_reading < 70: # too far
        rospy.loginfo("too far - turning left")
        #turnOnce("left", IRL_reading/100)
        newTurn((1+(IRL_reading/70))*100) # turning left
        walkMotion()
        walkMotion()
        
    elif IRL_reading == 0: 
        rospy.loginfo("too close - turning right")
        #turnOnce("right", IRL_reading/100)
        #newTurn((1+((IRL_reading-100)/50))*-100) #turning right
        turn90("right")
        walkMotion()
        walkMotion()
        
       
    elif 400 > IRL_reading > 100: # too close
        rospy.loginfo("too close - turning right")
        #turnOnce("right", IRL_reading/100)
        newTurn((1+((IRL_reading-100)/50))*-100) #turning right
        walkMotion()
        walkMotion()
    
    
        
        

def blockTurn(): #   #   #   #   #   #   #   #   #   #   #   #   #   #
    if DMS_reading > 250 and IRR_reading > 0 and IRL_reading > 0: # L R front block
        turn180("right")
        turn180("right")
    elif IRR_reading > 0 and DMS_reading > 250: # L front block
        turn90("left")
        turn90("left")
    elif IRL_reading > 0 and DMS_reading > 250: # R front block
        turn90("right")
        turn90("right")
   

        

# Main function # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group F Control Node...")
   
    #incrementer = 30
   
    # set to out/down neutral position
    response = setMotorTargetPositionCommand(motor_id1, 512)
    response = setMotorTargetPositionCommand(motor_id2, extend_2)
    response = setMotorTargetPositionCommand(motor_id3, 512)
    response = setMotorTargetPositionCommand(motor_id4, extend_4)
            
    response = setMotorTargetPositionCommand(motor_id5, down_5)
    response = setMotorTargetPositionCommand(motor_id6, down_6) 
    response = setMotorTargetPositionCommand(motor_id7, down_7)
    response = setMotorTargetPositionCommand(motor_id8, down_8)
  
    # INITIATE ACTION #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
    
     
    # control loop running at 10hz
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        print getMotorPositionCommand(motor_id5)
        if getMotorPositionCommand(motor_id5) >= up_5-1:
            up5 = True
        else:
            up5 = False
        if getMotorPositionCommand(motor_id6) <= up_6+1:
            up6 = True
        else:
            up6 = False
        if getMotorPositionCommand(motor_id7) <= up_7+1:
            up7 = True
        else:
            up7 = False
        if getMotorPositionCommand(motor_id8) >= up_8-1:
            up8 = True
        else:
            up8 = False
            
        if getMotorPositionCommand(motor_id1) <= extend_1+1:
            extend1 = True
        else:
            extend1 = False
        if getMotorPositionCommand(motor_id2) >= extend_2-1:
            extend2 = True
        else:
            extend2 = False
        if getMotorPositionCommand(motor_id3) >= extend_3-1:
            extend3 = True
        else:
            extend3 = False
        if getMotorPositionCommand(motor_id4) <= extend_4+1:
            extend4 = True
        else:
            extend4 = False
            
        # call function to get sensor value
        port1 = 1 #DMS
        port2 = 2 #IRL
        port6 = 6 #IRR
        DMS_reading = getSensorValue(port1)
        IRL_reading = getSensorValue(port2)
        IRR_reading = getSensorValue(port6)
        
        #rospy.loginfo("Sensor value at port %d: %f", 1, DMS_reading)
        #rospy.loginfo("Sensor value at port %d: %f", 2, IRL_reading)
        #rospy.loginfo("Sensor value at port %d: %f", 6, IRR_reading)


        #   #   #  #   #  Walk Cycle    #   #   #   #   #  #   #   #   #   #  #   #   #  
        
        ### WALKING ###
        walkMotion()
        
        ### REACTIONS ###
        #avoidObjects()
        wallFollow()
        #blockTurn()
        
        ### TURNS ###
        
        #turn90("right")
        #turn90("right")
        
        
        #rospy.sleep(5)
        #turn90("left")
        #turn90("left")
        #rospy.sleep(5)
        
        #rospy.sleep(5)
        #turn180("left")
        #turn180("left")
        #turn180("left")
        #rospy.sleep(5)
        
        #turn180("left")
        #turn180("left")
        
        
        r.sleep()
        
        
        
        
        # 15 cm from IR: 10-20
        # 15 cm from DMS: 1400
        
