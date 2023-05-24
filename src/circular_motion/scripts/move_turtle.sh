#!/bin/sh

# start ros master
gnome-terminal -- bash -c "source ~/turtlesim_assignment/devel/setup.bash";
gnome-terminal -- bash -c "roscore " & 

sleep 5

# launch turtlesim simulator
gnome-terminal -- bash -c "source ~/turtlesim_assignment/devel/setup.bash";
gnome-terminal -- bash -c "rosrun turtlesim turtlesim_node " &

sleep 5

# run ROS node for making turtle move in circle of radius 2 with speed 3
gnome-terminal -- bash -c "source ~/turtlesim_assignment/devel/setup.bash";
gnome-terminal -- bash -c "rosrun circular_motion circular_motion.py " 