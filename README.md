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

## Directory Structure

![Screenshot from 2023-05-24 21-47-23](https://github.com/Vamsi-IITI/turtlesim_assignment/assets/92263050/b6125771-f3c9-4a7d-9627-eed1c464ea0c)
