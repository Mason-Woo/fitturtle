# fitturtle

Fit Turtle is a TurtleBot that tries to improve your posture by evaluating it and giving you audio feedback. The robot looks around and tracks passersby, extracts a model of their skeleton, analyzes their posture, and tells them if it's good or bad.

This repository contains <i>code snippets</i> that can aid in the re-creation of a posture analysis turtlebot (which was developed over a 16-hour hackathon), but does not contain a complete working architecture, since some of the code is proprietary.

# SkeletonBasics.cpp

This is adapted from Skeleton Basics-D2D C++ Sample from MSDN. It contains the logic for following a user and determining the quality of posture. The thresholds for the values corresponding to good and bad posture were determined by analyzing a few samples.

# Audio.py

This received information about whether posture was good or bad, and plays an audio file corresponding to the feedback.

# Motor.py

This operated with ROS and generated commands for the robot to move in a given direction.

# Authors
Keen Sung, Tiago Muck, Martin Marshalek, Andy Shih

# License

MIT License
