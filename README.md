# fitturtle

Fit Turtle is a TurtleBot that tries to improve your posture by evaluating it and giving you audio feedback. The robot looks around and tracks passersby, extracts a model of their skeleton, analyzes their posture, and tells them if it's good or bad.

This repository contains <i>code snippets</i> that can aid in the re-creation of a posture analysis turtlebot (which was developed over a 16-hour hackathon), but does not contain a complete working architecture, since some of the code is proprietary.

# Build/Assembly Instructions
 
FitTurtle is based on the Turtlebot robotics kit (www.turtlebot.com), coupled with a DragonBoard 410c SBC. The Turtlebot robotics kit includes a Microsoft Kinect camera, mountpoints for processing hardware, and a Kobuki (an open robotics platform similar to iRobot’s Roomba). The Kinect and Kobuki are connected via USB to the DragonBoard, which uses the ROS software package and separate skeleton tracking software to control movement of the Turtlebot and the gathering of posture data, respectively.
  
# Usage Instructions
	 
	 FitTurtle is conceived as an autonomous robot that passively roams offices, schools, and gymnasiums and gathers data on posture and other fitness metrics. Posture and form corrections can be delivered directly by FitTurtle, or stored for data metrics on building health and ergonomics, for example. FitTurtle would be designed to be unobtrusive and fit into existing office-style environments. Posture/Fitness data and reports could be generated for health professionals to improve the health and well-being of employees.
	  
# SkeletonBasics.cpp

This is adapted from Skeleton Basics-D2D C++ Sample from MSDN. It contains the logic for following a user and determining the quality of posture. The thresholds for the values corresponding to good and bad posture were determined by analyzing a few samples.

# postureSound_py.py

This received information about whether posture was good or bad, and plays an audio file corresponding to the feedback.

# reader.py

This operated with ROS and generated commands for the robot to move in a given direction.

# Authors
Keen Sung, Tiago Muck, Martin Marshalek, Andy Shih

# License

MIT License
