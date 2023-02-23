# DEMOCRITUS INDUSTRIAL ROBOTICS MANIPULATOR


This is code for DIR's talos manipulator!

## GUIDE

## STEP 1 

Go to the desired location for creating the ws:

$ cd Desktop

$ mkdir my_ws/src

$ cd my_ws

$ mkdir src

$ cd src

$ git clone https://github.com/alexaske/DIR-widowxL-arm-.git

$ cd ..

$ catkin_make

$ source devel/setup.bash


## STEP 2

After connecting the arbotix with your computer 

$ sudo chmod 777 /dev/ttyUSB0
$ roslaunch widowx_arm_bringup arm_moveit.launch

The rviz will open and you can start planning!
# ENJOY
