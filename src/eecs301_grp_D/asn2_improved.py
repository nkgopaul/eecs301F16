#!/usr/bin/env python
import roslib
import rospy
from fw_wrapper.srv import *
from map import *
import time
import Queue
from numpy import median

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

visited = list()


############################################################################
#BUILT IN FUNCTIONS#########################################################

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


############################################################################
#STANDARD FUNCTIONS#########################################################

def waitForCompletion(motor_id):
    while(getIsMotorMovingCommand(motor_id)!=0):
        pass  
    return None

def reset_motors():
    setMotorMode(2,1)
    setMotorWheelSpeed(2,0)
    setMotorMode(3,1)
    setMotorWheelSpeed(3,0)
    return None

def take_readings():
    data = [0,0,0]
    DMS = 2
    IRR = 4
    IRL = 3
    data[0] = getSensorValue(DMS)
    data[1] = getSensorValue(IRR)
    data[2] = getSensorValue(IRL)
    #rospy.loginfo("   IRR: %10.2f   DMS: %10.2f   IRL: %10.2f",data[1],data[0],data[2]) 
    return data

################################################################################
#BLOCKED REACTIVE CONTROL#######################################################

def turn_when_blocked():
    data = take_readings()
    rblk = right_blocked()
    lblk = left_blocked()
    fblk = front_blocked()
    if rblk and fblk and not lblk:
        turn_left()
    elif lblk and fblk and not rblk:
        turn_right()
    elif rblk and fblk and lblk:
        turn_around()
    else:
        pass
    return None

'''
def right_blocked():
    data_right = 0
    data_length = 5
    rblk = False
    for i in range(0,data_length):
        sensors = take_readings()
        data_right += sensors[1]
    right_ave = data_right/data_length
    if right_ave >= 75:
        rblk = True
    return rblk 

def left_blocked():
    data_left = 0
    data_length = 5
    lblk = False
    for i in range(0,data_length):
        sensors = take_readings()
        data_left += sensors[2]
    left_ave = data_left/data_length
    if left_ave >= 75:
        lblk = True
    return lblk 

def front_blocked(): 
    data_front = 0
    data_length = 5
    fblk = False
    for i in range(0,data_length):
        sensors = take_readings()
        data_front += sensors[0]
    front_ave = data_front/data_length
    if front_ave >= 1300:
        fblk = True
    return fblk 
'''    
    
    
    
def right_blocked():
    data_right = []
    data_length = 5
    rblk = False
    for i in range(0,data_length):
        sensors = take_readings()
        data_right.append(sensors[1])
    right_ave = median(data_right)
    if right_ave >= 60:
        rblk = True
    return rblk 

def left_blocked():
    data_left = []
    data_length = 5
    lblk = False
    for i in range(0,data_length):
        sensors = take_readings()
        data_left.append(sensors[2])
    left_ave = median(data_left)
    if left_ave >= 60:
        lblk = True
    return lblk 

def front_blocked(): 
    data_front = []
    data_length = 5
    fblk = False
    for i in range(0,data_length):
        sensors = take_readings()
        data_front.append(sensors[0])
    front_ave = median(data_front)
    if front_ave >= 900:
        fblk = True
    return fblk 

############################################################################################


def follow_path(path):
    for goal in path:
        rospy.set_param('goal',goal)
        go_to_dir()
        side = where_am_i()
        rospy.loginfo(side)
        data = take_readings()
        if side == 'left':
            desired = 275.0
            current = data[2]
        elif side == 'right':
            desired = 275.0
            current = data[1]
        elif side == 'nowall':
            desired = 0
            current = 0
        set_control(rospy.get_param('kp'),rospy.get_param('kd'),rospy.get_param('ki'),desired-current,rospy.get_param('eint'))
        move_one_cell(side)
    return None

def go_to_dir():
    goal = rospy.get_param('goal')
    heading = rospy.get_param('heading')
    result = goal - heading
    if result == 1 or result == -3:
        rospy.loginfo('Turning Right!')
        turn_right()
    elif result == -1 or result == 3:
        rospy.loginfo('Turning Left!')
        turn_left()
    elif result == -2 or result == 2:
        rospy.loginfo('Turning Around!')
        turn_around()
    rospy.set_param('heading',goal)
    return None
    
def go_to_dir_safe(last=False):
    goal = rospy.get_param('goal_print')
    heading = rospy.get_param('heading_print')
    result = goal - heading
    if result == 1 or result == -3:
        rospy.loginfo('Turning Right!')
       # turn_right()
    elif result == -1 or result == 3:
        rospy.loginfo('Turning Left!')
       # turn_left()
    elif result == -2 or result == 2:
        rospy.loginfo('Turning Around!')
       # turn_around()
    rospy.set_param('heading_print',goal)
    
    if not last:
        rospy.loginfo('move one cell')
    return None


#############################################################################################
# Follow wall

def set_control(kp,kd,ki,prev,eint):
    rospy.set_param('kp',kp)
    rospy.set_param('kd',kd)
    rospy.set_param('ki',ki)
    rospy.set_param('prev',prev)
    rospy.set_param('eint',eint)
    return None

def get_control():
    kp = rospy.get_param('kp')
    kd = rospy.get_param('kd')
    ki = rospy.get_param('ki')
    derr = rospy.get_param('prev')
    eint = rospy.get_param('eint')
    return kp,kd,ki,derr,eint

def wall_controller(side):
    data = take_readings()
    if side == 'left':
        desired = 255.0
        current = data[2]
        if current < 150:
            return 0
    elif side == 'right':
        desired = 180.0
        current = data[1]
        if current < 150:
            return 0
    elif side == 'nowall':
        return 0
    kp,kd,ki,prev,eint = get_control()
    err = desired-current
    derr = err-prev
    eint = err+eint
    rospy.set_param('prev',err)
    rospy.set_param('eint',eint)
    u = float(kp)*err+float(kd)*derr+float(ki)*eint
    if u>100:
        u=100
    elif u<-100:
        u=-100
    return u


def c(speed):
    speed = speed*0.987
    return speed

def move_one_cell(side):
    n = 1023
    setMotorMode(2,1)
    setMotorMode(3,1)
    
    # Start both motorsa
    setMotorWheelSpeed(2,c(256+n))
    setMotorWheelSpeed(3,256)

    setMotorWheelSpeed(2,c(512+n))
    setMotorWheelSpeed(3,512)
    start = rospy.get_rostime()
    
    now = rospy.Time()
    while (now-start)<rospy.Duration(3.5):
        # Wall control
        u = wall_controller(side)
        rospy.loginfo(int(u))
        if side == 'right':
            if u>0:
                u = u*1
            setMotorWheelSpeed(2,c(512+n-int(u)))
            setMotorWheelSpeed(3,512+int(u))
        elif side == 'left':
            if u>0:
                u = u*1
            setMotorWheelSpeed(2,c(512+n+int(u)))
            setMotorWheelSpeed(3,512-int(u))
        else:
            setMotorWheelSpeed(2,c(512+n))
            setMotorWheelSpeed(3,512)

        now = rospy.get_rostime()
    
    # Stop both motors
    setMotorWheelSpeed(2,c(256+n))
    setMotorWheelSpeed(3,256)
    setMotorWheelSpeed(3,0)
    setMotorWheelSpeed(2,c(0))
    #front_back_adjust()
    return None

def front_back_adjust():
    n = 1023
    data = take_readings()
    if data[0]>2400:
        # too close, move backwards
        rospy.loginfo("too close to wall")
        setMotorWheelSpeed(2,512)
        setMotorWheelSpeed(3,512+n)
        setMotorWheelSpeed(3,256+n)
        setMotorWheelSpeed(2,256)
        while data[0]>2650:
            data = take_readings()
        setMotorWheelSpeed(2,256)
        setMotorWheelSpeed(3,256+n)
        setMotorWheelSpeed(3,0)
        setMotorWheelSpeed(2,0)
    elif data[0]<2000 and data[0]>1200:
        rospy.loginfo("too far from wall")
        # too far away, move forward
        setMotorWheelSpeed(3,256)
        setMotorWheelSpeed(2,256+n)
        setMotorWheelSpeed(2,512+n)
        setMotorWheelSpeed(3,512)
        while data[0]<2150:
            data = take_readings()
        setMotorWheelSpeed(2,256+n)
        setMotorWheelSpeed(3,256)
        setMotorWheelSpeed(3,0)
        setMotorWheelSpeed(2,0)
    return None

def turn_right():
    n = 1023
    setMotorMode(2,1)
    setMotorMode(3,1)
    setMotorWheelSpeed(3,1023)
    setMotorWheelSpeed(2,1023)
    time.sleep(0.39)
    setMotorWheelSpeed(3,0)
    setMotorWheelSpeed(2,0)
    return None

def turn_left():
    n = 1023
    setMotorMode(2,1)
    setMotorMode(3,1)
    setMotorWheelSpeed(3,1023+n)
    setMotorWheelSpeed(2,1023+n)
    time.sleep(0.39)
    setMotorWheelSpeed(3,0)
    setMotorWheelSpeed(2,0)
    return None

def turn_around():
    n = 1023
    setMotorMode(2,1)
    setMotorMode(3,1)
    setMotorWheelSpeed(3,1023+n)
    setMotorWheelSpeed(2,1023+n)
    time.sleep(0.799)
    setMotorWheelSpeed(3,0)
    setMotorWheelSpeed(2,0)
    return None

def where_am_i():
    right = "right"
    left = "left"
    nowall = "nowall"

    ir_blocked = 300
    data = take_readings()

    if data[1] > 25:
        side = right
        rospy.loginfo("right wall detected")
    elif data[2] > 25:
        side = left
        rospy.loginfo("left wall detected")
    else:
        rospy.loginfo("no wall detected")
        side = nowall

    return side

def where_are_walls():
    walls = [0, 0, 0]
    data = take_readings()
    rblk = right_blocked()
    lblk = left_blocked()
    fblk = front_blocked()
    if rblk:
        walls[1] = 1
        rospy.loginfo("right wall detected")
    if lblk:
        walls[2] = 1
        rospy.loginfo("left wall detected")
    if fblk:
        walls[0] = 1
        rospy.loginfo("front wall detected")
    
    return walls
    
#############################################################################################
# Map functions
def getValidNeighbors(csmap, i, j):
    n = True
    e = True
    s = True
    w = True

    if(csmap.horizontalWalls[i][j]):
        n = False 
    if(csmap.horizontalWalls[i+1][j]):
        s = False
    if(csmap.verticalWalls[i][j]):
        w = False
    if(csmap.verticalWalls[i][j+1]): 
        e = False         
    return n, e, s, w

def setInfCosts(csmap):
    for i in range (0,8):
        for j in range(0,8):
            csmap.setCost(i,j,1000)
    return None


def setAllCosts(csmap, xs, ys, xe, ye):
    setInfCosts(csmap)
    csmap.setCost(xe, ye, 0)
    visited.append((xe,ye))
    nodes = Queue.Queue()
    nodes = add_neighbs(csmap, xe, ye, nodes)
    
    while not nodes.empty():
        # pair struct: [(neighborx, neighbory), (parentx, parenty)]
        pair = nodes.get()
        
        currx = pair[0][0]
        curry = pair[0][1]
        parentx = pair[1][0]
        parenty = pair[1][1]
            
        parent_cost = csmap.getCost(parentx, parenty)
        curr_cost = csmap.getCost(currx, curry)
        
        if (curr_cost > parent_cost + 1):
            csmap.setCost(currx, curry, parent_cost + 1)
            
        if (currx == xs and curry == ys):
            break
            
        visited.append((currx, curry))
        nodes = add_neighbs(csmap, currx, curry, nodes)
    
    
def add_neighbs(csmap, x, y, queue):
    # queue struct: [(neighborx, neighbory), (parentx, parenty)]

    n, e, s, w = getValidNeighbors(csmap, x, y)
    if n:
        if (x-1, y) not in visited:
            queue.put([(x-1, y), (x, y)])
    if e:
        if (x, y+1) not in visited:
            queue.put([(x, y+1), (x, y)])
    if s:
        if (x+1, y) not in visited:
            queue.put([(x+1, y), (x, y)])
    if w:
        if (x, y-1) not in visited:
            queue.put([(x, y-1), (x, y)])
            
    return queue

def generate_path():
    # cmdlist = heading_i, x_i, y_i,heading_f, x_f, y_f
    # parse command list
    commandlist = [int(x) for x in rospy.get_param('cmdlist').split(',')]
    rospy.loginfo(commandlist)
    rospy.set_param('heading',commandlist[0])
    rospy.set_param('heading_print',commandlist[0])
    rospy.set_param('final_heading',commandlist[3])
    start_end = [commandlist[1],commandlist[2],commandlist[4],commandlist[5]]
    
    # initialize map and set all costs
    my_map = EECSMap()
    setAllCosts(my_map, start_end[0], start_end[1], start_end[2], start_end[3])
    my_map.printCostMap()
    my_map.printObstacleMap()
    
    # follow costs to generate path
    path = list()
    curr_x = start_end[0]
    curr_y = start_end[1]
    end_x = start_end[2]
    end_y = start_end[3]
    
    # Main iterative loop
    while not (curr_x == end_x and curr_y == end_y):
        curr_cost = my_map.getCost(curr_x, curr_y)
        n, e, s, w = getValidNeighbors(my_map, curr_x, curr_y)
        #rospy.loginfo("%5d %5d",curr_x, curr_y)
        if n:
            neighb_cost = my_map.getNeighborCost(curr_x, curr_y, 1)
            if neighb_cost == curr_cost - 1:
                path.append(translate(curr_x, curr_y, curr_x - 1, curr_y))
                curr_x = curr_x - 1
                rospy.loginfo("%d, %d",curr_x,curr_y)
                continue
        if e:
            neighb_cost = my_map.getNeighborCost(curr_x, curr_y, 2)
            if neighb_cost == curr_cost - 1:
                path.append(translate(curr_x, curr_y, curr_x, curr_y + 1))
                curr_y = curr_y + 1
                rospy.loginfo("%d, %d",curr_x,curr_y)
                continue
        if s:
            neighb_cost = my_map.getNeighborCost(curr_x, curr_y, 3)
            if neighb_cost == curr_cost - 1:
                path.append(translate(curr_x, curr_y, curr_x + 1, curr_y))
                curr_x = curr_x + 1
                rospy.loginfo("%d, %d",curr_x,curr_y)
                continue
        if w:
            neighb_cost = my_map.getNeighborCost(curr_x, curr_y, 4)
            if neighb_cost == curr_cost - 1:
                path.append(translate(curr_x, curr_y, curr_x, curr_y - 1))
                curr_y = curr_y - 1
                rospy.loginfo("%d, %d",curr_x,curr_y)
                continue
    return path

def print_path(path):
    for goal in path:
        rospy.set_param('goal_print',goal)
        go_to_dir_safe()
    rospy.set_param('goal_print',rospy.get_param('final_heading'))
    go_to_dir_safe(True)

def translate(xc, yc, xn, yn):
    if xn > xc:
        return 2
    if xn < xc: 
        return 0
    if yn > yc:
        return 1
    if yn < yc:
        return 3
    else:
        return None
        
#############################################################################################
# Wandering functions
# N = 1, E = 2, S = 3, W = 4
def printCSMap(csmap):
    print "Obstacle Map: "
    for i in xrange(8):
        for j in xrange(8):
            if (csmap.horizontalWalls[i][j] == 0):
                sys.stdout.write("    ")
            else:
                sys.stdout.write(" ---")

        print " "
        for j in xrange(8):
            if (csmap.verticalWalls[i][j] == 0):
                sys.stdout.write("  O ")
            else:
                sys.stdout.write("| O ")
        print " "
    print " "

def wander():
    my_map = EECSMap()
    my_map.clearCostMap()
    my_map.clearObstacleMap()
    rospy.set_param('heading',0)
    rospy.set_param('curr_x',1)
    rospy.set_param('curr_y',6)
    rospy.set_param('curr_h',0)
    stack = [[1, 6]]
    visited = [[1, 6]]
    explore_maze(stack, visited, my_map)
    my_map.printCostMap()
    printCSMap(my_map)
    
    return my_map
    
def setWalls(x, y, heading, csmap):
    walls = where_are_walls()
    if walls[0] == 1:
        mod = 1
        new_head = (heading+mod)%4
        if new_head == 0:
            new_head = 4
        csmap.setObstacle(x, y, 1, (new_head))
    if walls[1] == 1:
        mod = 2
        new_head = (heading+mod)%4
        if new_head == 0:
            new_head = 4
        csmap.setObstacle(x, y, 1, (new_head))
    if walls[2] == 1:
        mod = 4
        new_head = (heading+mod)%4
        if new_head == 0:
            new_head = 4
        csmap.setObstacle(x, y, 1, (new_head))
    return csmap
        
def setValidNeighbors(csmap, i, j, visited):
    n = True
    e = True
    s = True
    w = True
    
    rospy.loginfo(i)
    rospy.loginfo(j)

    if(csmap.horizontalWalls[i][j] or ([i-1, j] in visited)):
        n = False 
    if(csmap.verticalWalls[i][j+1] or ([i, j+1] in visited) ):
        e = False
    if(csmap.horizontalWalls[i+1][j] or ([i+1, j] in visited)):
        s = False
    if(csmap.verticalWalls[i][j] or ([i, j-1] in visited)):
        w = False         
    return n, e, s, w
        

def explore_maze(stack, visited, csmap):
    
    
    while len(stack) != 0:
        printCSMap(csmap)
        csmap.printCostMap()
        curr_x = rospy.get_param('curr_x')
        curr_y = rospy.get_param('curr_y')
        curr_h = rospy.get_param('curr_h')
        rospy.loginfo(rospy.get_param('curr_x'))
        rospy.loginfo(rospy.get_param('curr_y'))
        rospy.loginfo(rospy.get_param('curr_h'))
        rospy.loginfo(stack)
        rospy.loginfo(visited)
        
        csmap = setWalls(curr_x, curr_y, curr_h, csmap)
        n, e, s, w = setValidNeighbors(csmap, curr_x, curr_y, visited)
        rospy.loginfo([n,e,s,w])
        if n or e or s or w:
            if n:
            
                stack.append([curr_x-1,curr_y])
                rospy.set_param('goal',0)
                go_to_dir()
                move_one_cell('nowall')
                rospy.set_param('curr_h',0)
                rospy.set_param('curr_x',curr_x-1)
                rospy.set_param('curr_y',curr_y)
                visited.append([curr_x-1,curr_y])
                csmap.setCost(curr_x-1, curr_y, 1)
                #visited.append([curr_x,curr_y])
                #csmap.setCost(curr_x, curr_y, 1)
                #explore_maze(stack, visited, csmap)
            elif e:
                stack.append([curr_x,curr_y+1])
                rospy.set_param('goal',1)
                go_to_dir()
                move_one_cell('nowall')
                rospy.set_param('curr_h',1)
                rospy.set_param('curr_x',curr_x)
                rospy.set_param('curr_y',curr_y+1)
                visited.append([curr_x,curr_y+1])
                csmap.setCost(curr_x, curr_y+1, 1)
                #visited.append([curr_x,curr_y])
                #csmap.setCost(curr_x, curr_y, 1)
                #explore_maze(stack, visited, csmap)
            elif s:
                stack.append([curr_x+1,curr_y])
                rospy.set_param('goal',2)
                go_to_dir()
                move_one_cell('nowall')
                rospy.set_param('curr_h',2)
                rospy.set_param('curr_x',curr_x+1)
                rospy.set_param('curr_y',curr_y)
                visited.append([curr_x+1,curr_y])
                csmap.setCost(curr_x+1, curr_y, 1)
                #visited.append([curr_x,curr_y])
                #csmap.setCost(curr_x, curr_y, 1)
                #explore_maze(stack, visited, csmap)
            elif w:
                stack.append([curr_x,curr_y-1])
                rospy.set_param('goal',3)
                go_to_dir()
                move_one_cell('nowall')
                rospy.set_param('curr_h',3)
                rospy.set_param('curr_x',curr_x)
                rospy.set_param('curr_y',curr_y-1)
                visited.append([curr_x,curr_y-1])
                csmap.setCost(curr_x, curr_y-1, 1)
                #visited.append([curr_x,curr_y])
                #csmap.setCost(curr_x, curr_y, 1)
                #explore_maze(stack, visited, csmap)
            else:
                rospy.loginfo("Um, what are you doin to me... Plz stahp")
        else:
            stack = stack[0:len(stack)-1]
            rospy.loginfo("else case")
            rospy.set_param('cmdlist',str(curr_h)+str(curr_x)+str(curr_y)+str(curr_h)+str(stack[-1][0])+str(stack[-1][0]))
            path = generate_path()
            follow_path(path)
            '''
            turn_around()
            move_one_cell('nowall')
            turn_around()
            '''
            #visited.append([curr_x,curr_y])
            #csmap.setCost(curr_x, curr_y, 1)
            rospy.set_param('curr_x',stack[-1][0])
            rospy.set_param('curr_y',stack[-1][1])
            #explore_maze(stack, visited, csmap)
    return None

'''
def explore_maze(stack, visited, csmap):
    
    printCSMap(csmap)
    csmap.printCostMap()
    curr_x = rospy.get_param('curr_x')
    curr_y = rospy.get_param('curr_y')
    curr_h = rospy.get_param('curr_h')
    rospy.loginfo(rospy.get_param('curr_x'))
    rospy.loginfo(rospy.get_param('curr_y'))
    rospy.loginfo(rospy.get_param('curr_h'))
    rospy.loginfo(stack)
    rospy.loginfo(visited)
    
    csmap = setWalls(curr_x, curr_y, curr_h, csmap)
    n, e, s, w = setValidNeighbors(csmap, curr_x, curr_y, visited)
    if n or e or s or w:
        if n:
            stack.append([curr_x-1,curr_y])
            rospy.set_param('goal',0)
            go_to_dir()
            move_one_cell('nowall')
            rospy.set_param('curr_h',0)
            rospy.set_param('curr_x',curr_x-1)
            rospy.set_param('curr_y',curr_y)
            visited.append([curr_x-1,curr_y])
            csmap.setCost(curr_x-1, curr_y, 1)
            #visited.append([curr_x,curr_y])
            #csmap.setCost(curr_x, curr_y, 1)
            explore_maze(stack, visited, csmap)
        elif e:
            stack.append([curr_x,curr_y+1])
            rospy.set_param('goal',1)
            go_to_dir()
            move_one_cell('nowall')
            rospy.set_param('curr_h',1)
            rospy.set_param('curr_x',curr_x)
            rospy.set_param('curr_y',curr_y+1)
            visited.append([curr_x,curr_y+1])
            csmap.setCost(curr_x, curr_y+1, 1)
            #visited.append([curr_x,curr_y])
            #csmap.setCost(curr_x, curr_y, 1)
            explore_maze(stack, visited, csmap)
        elif s:
            stack.append([curr_x+1,curr_y])
            rospy.set_param('goal',2)
            go_to_dir()
            move_one_cell('nowall')
            rospy.set_param('curr_h',2)
            rospy.set_param('curr_x',curr_x+1)
            rospy.set_param('curr_y',curr_y)
            visited.append([curr_x+1,curr_y])
            csmap.setCost(curr_x+1, curr_y, 1)
            #visited.append([curr_x,curr_y])
            #csmap.setCost(curr_x, curr_y, 1)
            explore_maze(stack, visited, csmap)
        elif w:
            stack.append([curr_x,curr_y-1])
            rospy.set_param('goal',3)
            go_to_dir()
            move_one_cell('nowall')
            rospy.set_param('curr_h',3)
            rospy.set_param('curr_x',curr_x)
            rospy.set_param('curr_y',curr_y-1)
            visited.append([curr_x,curr_y-1])
            csmap.setCost(curr_x, curr_y-1, 1)
            #visited.append([curr_x,curr_y])
            #csmap.setCost(curr_x, curr_y, 1)
            explore_maze(stack, visited, csmap)
        else:
            rospy.loginfo("Um, what are you doin to me... Plz stahp")
    else:
        stack = stack[0:len(stack)-1]
        if len(stack) != 0:
            rospy.loginfo("else case")
            turn_around()
            move_one_cell('nowall')
            turn_around()
            visited.append([curr_x,curr_y])
            csmap.setCost(curr_x, curr_y, 1)
            rospy.set_param('curr_x',stack[-1][0])
            rospy.set_param('curr_y',stack[-1][1])
            explore_maze(stack, visited, csmap)
        else:
            return None
'''
    
            
        
#############################################################################################
# Main function
def myhook():
    reset_motors()
    rospy.set_param('reset',0)

if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group X Control Node...")
    rospy.on_shutdown(myhook)
    r = rospy.Rate(10) # 10hz
    print("WANDER")
    wander()
    
    '''
    # Initialize parameters
    rospy.set_param('goal',1)
    rospy.set_param('goal_print',1)
    rospy.set_param('heading',0)
    rospy.set_param('heading_print',0)
    rospy.set_param('cmdlist','0,0,0,0,0,0')
    rospy.set_param('finished',0)
    rospy.set_param('reset', 0)
    set_control(0.3,0.5,0.0,0.0,0.0)
    done = False

    # Reset wheel motors to wheel mode and 0 speed
    #path = generate_path()
    #rospy.loginfo(path)
    
    while rospy.get_param('cmdlist') == '0,0,0,0,0,0':
        continue
        
    path = generate_path()
    #path = [2,2,1,1]
    rospy.loginfo(path)
    print_path(path)

    while not rospy.is_shutdown():
        if not done:
            follow_path(path)
            
            #final heading adjustment
            rospy.set_param('goal',rospy.get_param('final_heading'))
            go_to_dir()
            
            done = True
        else:
            pass
        r.sleep()
    '''
        # sleep to enforce loop rate
