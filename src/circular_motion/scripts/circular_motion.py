#! usr/bin/env/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

# global variables for storing the current pose of the turtle and no. of turns it has completed
x = 0
y = 0
yaw = 0
turns_completed = 0   

def poseCallback(msg):
    global x, y, yaw , turns_completed

    if( yaw < 0 and msg.theta >= 0):
        turns_completed += 1
        rospy.loginfo("Turns completed: {}".format(turns_completed))

    x = msg.x
    y = msg.y
    yaw = msg.theta 
    #rospy.loginfo("Current pose --> x: {}, y: {}, yaw: {}".format(x, y, yaw))

def main():    
    
    rospy.init_node('cirular_motion', anonymous=True)                

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)    # publisher
    rospy.Subscriber('/turtle1/pose', Pose, poseCallback)              # subscriber

    rate = rospy.Rate(10) # 10hz

    rospy.loginfo("Going round and round!")
    
    global x, y, yaw, turns_completed

    while(rospy.is_shutdown() == False):

        if(turns_completed < 2):

            vel_msg = Twist()
            vel_msg.linear.x = 3               # linear velocity = 3
            vel_msg.angular.z = 1.5            # angular velocity = v/r = 3/2 = 1.5
            pub.publish(vel_msg)

        if(turns_completed == 2):              # for stopping the turtle after 2 turns
            vel_msg = Twist()
            vel_msg.linear.x = 0               
            vel_msg.angular.z = 0
            pub.publish(vel_msg)
            rospy.loginfo("Completed the task!")
            rospy.signal_shutdown("Reached the goal!")
            break

        rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass