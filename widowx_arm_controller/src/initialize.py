#! /bin/bash

rostopic pub /joint_1/command std_msgs/Float64 "data: 0.0"
pid = $!
kill -INT "$pid"
rostopic pub /joint_2/command std_msgs/Float64 "data: 0.0"
pid = $!
kill -INT "$pid"
rostopic pub /joint_3/command std_msgs/Float64 "data: 0.0"
pid = $!
kill -INT "$pid"
rostopic pub /joint_4/command std_msgs/Float64 "data: 0.0"
pid = $!
kill -INT "$pid"
rostopic pub /joint_5/command std_msgs/Float64 "data: 0.0"
pid = $!
kill -INT "$pid"

