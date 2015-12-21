This is a package for simulating Barrett hand in Gazebo.

The existing simulation package for Barrett hand does not provide the needed service call to simulate the hand exactly like the hardware. The joint bh_j11_position_controller (spread) only moves the 1st finger on spread.

This package provides the needed action services exactly as the robot in hardware. Also the two spread joints for two fingers are included.

To run the robot in simulation first import the Barrett hand in Gazebo by any existing package. Then run

	roslaunch bhand_gazebo bhand_controller_gazebo.launch

The needed topics and action services will be up. 
nodes:

	/bhand_node/command

services:
	
	/bhand_node/actions

To run the robot as in the robot in hardware:

	rosservice call /bhand_node/actions <grasp mode>
	
	rosservice call /bhand_node/actions 1

will put the hand in initialization mode. The grasp modes are identified in Service.msg exactly as the hardware.

INIT_HAND = 1
CLOSE_GRASP = 2
OPEN_GRASP = 3
SET_GRASP_1 = 4
SET_GRASP_2 = 5
CLOSE_HALF_GRASP = 6

To run the robot by publishing positions to the topic:


rostopic pub /bhand_node/command sensor_msgs/JointState "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: ['j11_joint', 'j12_joint', 'j21_joint', 'j22_joint','j32_joint']
position: [0.5 , 0.5, 0.5, 0.5, 1.5]
velocity: [0]
effort: [0]" 


