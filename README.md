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

$ roslaunch widowx_arm_controller widowx_arm_controller.launch

Give each of these commands in a separate command window 

:warning: Hold the arm so that it doesn't hit anything :warning:

$ rostopic pub -1 /joint_1/command std_msgs/Float64 "data: 0.0"

$ rostopic pub -1 /joint_2/command std_msgs/Float64 "data: 0.0"

$ rostopic pub -1 /joint_3/command std_msgs/Float64 "data: 0.0"

$ rostopic pub -1 /joint_4/command std_msgs/Float64 "data: 0.0"

Now all of the motors should be locked and the arm has been initialized to the default pose!!!

#### :warning: Maybe you need to give execute permissions to some of the packages

![Screenshot_2023-02-24_154146](https://user-images.githubusercontent.com/78262995/221682553-fd1c0dd6-1a8c-4ea8-90bd-db7511e50b51.png)


$chmod +x src/arbotix_ros/arbotix_python/bin/arbotix_driver

After giving permissions you should launch again

## STEP 3
$ roslaunch widowx_arm_bringup arm_moveit.launch sim:=false

The rviz will open and you can start planning!
# HOW TO RUN SIMULATION 

## Do step 1

$ roslaunch widowx_arm_bringup arm_moveit.launch

