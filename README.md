# turtlesim_assignment

## Instructions 

1. Install Turtlesim :
``` 
sudo apt-get install ros-noetic-turtlesim
```

2. Clone the repository
```
git clone https://github.com/Vamsi-IITI/turtlesim_assignment.git
```

3. Navigate up to the scripts folder of circular_motion ros package ( ```cd ~/turtlesim_assignment/src/circular_motion/scripts``` ) , and make all files executable :

```
chmod +x ./*
```

Now you can navigate back to root level directory and follow next steps .

4. Navigate up to the root level directory ( ```cd ~/turtlesim_assignment``` ) , and execute:

```
catkin_make
source devel/setup.bash
```

5. Finally, to run program 
```
cd ~/turtlesim_assignment
```

**Way 1 ( Using Shell Script ) :**

```
source devel/setup.bash
./src/circular_motion/scripts/move_turtle.sh
```

**Way 2 :**

Open terminal, start ROS Master
```
source devel/setup.bash
roscore
```
Open new terminal,
```
source devel/setup.bash
rosrun turtlesim turtlesim_node
```
Open new terminal,
```
source devel/setup.bash
rosrun circular_motion circular_motion.py
```

## Video-Demo

https://github.com/Vamsi-IITI/turtlesim_assignment/assets/92263050/beed2c30-386e-4fdd-a774-c63b15d04aab

## Directory Structure

![Screenshot from 2023-05-24 21-47-23](https://github.com/Vamsi-IITI/turtlesim_assignment/assets/92263050/b6125771-f3c9-4a7d-9627-eed1c464ea0c)

## Code

```
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
```

## Testing Environment
```
Lenovo Ideapad 5 @ Ryzen 7 5700U
16 GB RAM , 512 GB SSD
OS : Ubuntu 20.04 LTS ( Focal Fossa )
ROS Distro : Noetic
```
