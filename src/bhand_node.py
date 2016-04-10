#!/usr/bin/env python
import rospy
from std_msgs.msg import *
from sensor_msgs.msg import JointState
from bhand_gazebo.srv import *

#individual publishers for the joints
pub_j11=rospy.Publisher("/bh_j11_position_controller/command",Float64, queue_size=5)
pub_j12=rospy.Publisher("/bh_j12_position_controller/command",Float64, queue_size=5)
pub_j22=rospy.Publisher("/bh_j22_position_controller/command",Float64, queue_size=5) 
pub_j32=rospy.Publisher("/bh_j32_position_controller/command",Float64, queue_size=5)



def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s %f", data.name,data.position[3])
    #rospy.loginfo(rospy.get_caller_id() + "OK I heard %f", data.position[4])
    
    #rate = rospy.Rate(5) # 10hz
    #while not rospy.is_shutdown():
    pub_j11.publish(data.position[0])
    pub_j12.publish(data.position[1])
    pub_j22.publish(data.position[2])
    pub_j32.publish(data.position[3])
          #rate.sleep()

def handle_action(req):
    
    if req.action==1:
	pub_j11.publish(0.0)
	pub_j12.publish(0.0)
	pub_j22.publish(0.0)
	pub_j32.publish(0.0)
	print "Setting hand in Initialization mode"
	return True
    elif req.action==2:
	pub_j12.publish(2.44)
	pub_j22.publish(2.44)
	pub_j32.publish(2.44)
	print "Setting hand in Close Grasp mode"
	return True
    elif req.action==3:
	pub_j12.publish(0)
	pub_j22.publish(0)
	pub_j32.publish(0)
	print "Setting hand in Open Grasp mode"
	return True
    elif req.action==4:
	pub_j11.publish(0.0)
	pub_j12.publish(0.0)
	pub_j22.publish(0.0)
	pub_j32.publish(0.0)
	
	print "Setting hand in Grasping mode 1"
	return True
    elif req.action==5:
	pub_j11.publish(3.14)
	pub_j12.publish(0.0)
	pub_j22.publish(0.0)
	pub_j32.publish(0.0)
	
	print "Setting hand in Grasping mode 2"
	return True
    elif req.action==6:
	pub_j12.publish(1.57)
	pub_j22.publish(1.57)
	pub_j32.publish(1.57)
	print "Setting hand in Close Half Grasp mode"
	return True
    else:
	return False


def listener():
     
#Initialize the bhand node
    rospy.init_node('bhand_node', anonymous=False)
#Creating the topic for subscribing commands
    rospy.Subscriber('%s/command'%rospy.get_name(), JointState, callback)
#Creating the service for performing different grasp mode.Always try to start from Initialization mode: rosservice call /bhand_node/actions 1
    rospy.Service('%s/actions'%rospy.get_name(), Actions, handle_action)
    
    
    rospy.spin()


    



if __name__ == '__main__':
    listener()
    
