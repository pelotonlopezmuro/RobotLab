# -*- coding: utf-8 -*-
"""───────────────────────────────────────────────────────────────────────
                     ┬─┐┌─┐┌┐ ┌─┐┌┬┐  ┬  ┌─┐┌┐                           
                     ├┬┘│ │├┴┐│ │ │   │  ├─┤├┴┐                          
                     ┴└─└─┘└─┘└─┘ ┴   ┴─┘┴ ┴└─┘                          
 ────────────────────────────────────────────────────────────────────────"""
"""
    Project Title: TurtleBot Implementation
    Author: Juan Lopez Muro, Cecilia Diaz
    Date: 01-16-2024
    Version 1.0
    Description: In this class, we will apply the concepts studied to an
    example. In the first stage, we did work in a simulated environment.
    Now, we will work on an actual experiment in the lab.
"""
"""                    README
Task0:
    0. The controller and the main section are the only methods that need to be modified.
    Both are at the end of this script.

Task1: Record a manual trajectory.
    1.0 Go to the main section, TASK1
    1.1 Uncomment the obj.record_traj("SecXX_LastName_Name.txt") line, and comment out everything else.
    1.2 Modify the string SecXX_LastName_Name.txt, using your section and name.
    1.3 Save the File using File ->Save or ctrl-S.
    1.4 Place the robot in a known spot, position, and orientation.
    1.5 Prepare to teleoperate the TurtleBot3 using the keyboard.
        To do that, on a PowerShell run:
            roslaunch turtlebot3_bringup turtlebot3_robot.launch
    1.6 Prepare to record the teleoperated trajectory.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    1.7 Select the former PowerShell and teleoperate the TurtleBot3 using the keyboard.
        When satisfied with the trajectory, select the later PowerShell and click ctrl-c to quit the recording.
    1.8 Repeat 1.5 and 1.6 until satisfied
    1.9 Press ctrl-c on the former PowerShell to quit the teleoperation.

Task2: Play back the recorded manual trajectory in an open loop.
    1.0 Go to the main section, TASK2
    1.1 Uncomment the obj.play_traj("SecXX_LastName_Name.txt") line, and comment out everything else.
    1.2 Modify the string SecXX_LastName_Name.txt, using your section and name.
    1.3 Save the File using File ->Save or ctrl-S.
    1.4 Place the robot in a known spot, position, and orientation.
    1.5 Be sure that the keyboard teleoperation process is killed. It can interfere.
    1.6 Prepare to play back the teleoperated trajectory.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    1.7 Press ctrl-c on to finish this task. 
 
Task3: Design and code the feedback controller.
    3.0 Go to the main section, TASK3
    3.1 Uncomment the obj.control_traj("rec_SecXX_LastName_Name.txt", "log_ctrl_SecXX_LastName_Name.txt") line,
    and comment everything else.
    3.2 We will follow the same steps we did in the simulation.

    3.2 Place the robot in an x=0, psi=0 pose.
    3.3 Implement a simple x-control using first-order error dynamics. Go to the controller function and 
    follow all the X.0, X.1, X.2, X.3, X.4, and X.5. You only need to write one line of code at each step.
    3.4 Save the File using File ->Save or ctrl-S.
    3.6 Prepare to test your x-position proportional controller.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    3.7 Press ctrl-c on to finish this task.
    3.8 Repeat 3.2 to 3.7 until satisfied.

    3.9 Place the robot in an x=0, psi=0 pose.
    3.10 Implement a simple psi-control using first-order error dynamics. Go to the controller function and 
    follow all the P.0, P.1, P.2, P.3, P.4, and P.5. You only need to write one line of code at each step.
    3.11 Save the File using File ->Save or ctrl-S.
    3.12 Prepare to test your psi-position proportional controller.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    3.13 Press ctrl-c on to finish this task.
    
    3.14 Place the robot in a x=0, y=0, psi=0 pose.
    3.15 Implement a simple y-control using first-order error dynamics. Go to the controller function and 
    follow all the Y.0, Y.1, Y.2, Y.3, Y.4, and Y.5. You only need to write one line of code at each step.
    3.16 Save the File using File ->Save or ctrl-S.
    3.17 Prepare to test your y-position proportional controller.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    3.18 Press ctrl-c on to finish this task. 
 
Task4: Follow the recorded manual trajectory in a closed loop using your controller.
    4.0 Go to the controller function and  uncomment the  x_d = self.x_traj and  y_d = self.y_traj lines.
    4.1 Go to the main section, TASK4
    4.2 Uncomment the obj.control_traj("rec_SecXX_LastName_Name.txt", "log_ctrl_SecXX_LastName_Name.txt") line,
    and comment everything else.
    4.3 Save the File using File ->Save or ctrl-S.
    4.4 Prepare to test your controller.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    4.5 Press ctrl-c on to finish this task.
    
Task5: Follow your desired trajectory in a closed loop using your controller.
    5.0 Go to the main section, TASK5
    5.1 Uncomment the obj.control_traj("NameOfYourFile.txt", "log_NameOfYourFile.txt") line, and comment everything else.
    5.2 Replace NameOfYourFile.txt with the name of your File and log_NameOfYourFile.txt with the name you want.
    5.3 Save the File using File ->Save or ctrl-S.
    5.4 Prepare to test your controller.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    5.5 Press ctrl-c on to finish this task.
    
Task6: RACE. If you did not bring your own trajectory, follow the proposed trajectory in a closed loop using your controller.
    6.0 Go to the main section, TASK6
    6.1 obj.control_traj("trajectoryRU_SOL.txt", "log_ctrl_SecXX_LastName_Name_RU.txt") line, and comment everything else.
    6.2 Replace log_ctrl_SecXX_LastName_Name_RU.txt using your section and name.
    6.3 Save the File using File ->Save or ctrl-S.
    6.4 Prepare to test your controller and race.
        To do that, execute this Python script, on a PowerShell run:
            python mainStd.py
    6.5 Press ctrl-c on to finish this task.

Task7: I will email you all the log files for you to post-process and prepare your presentation.
"""
import sys                      # Importing the sys module to access system-specific parameters and functions
import math                     # Importing the math module for math computations
import time                     # Importing the time module for time-related functions
import rospy                    # Importing rospy, the client library for ROS in Python
import threading                # Importing the threading module for multi-threading capabilities
from datetime import datetime   # Importing the Twist message type from geometry_msgs
from sshkeyboard import listen_keyboard                                     # Importing the function listen_keyboard from the sshkeyboard module
from geometry_msgs.msg import Twist                                  # Importing the Twist message type from geometry_msgs for turtlebot
from geometry_msgs.msg import TwistStamped, PoseStamped              # Importing the Twist message type from geometry_msgs for VICON
from sensor_msgs.msg   import Imu              # Importing the Twist message type from geometry_msgs
from tf.transformations import euler_from_quaternion, quaternion_from_euler # Importing the Twist message type from geometry_msgs


class Turtlebot:
    def __init__(self):
        """ -------- Start of Controller Gains --------- """
        self.vx_traj = 0.0
        self.vy_traj = 0.0
        self.omg_traj = 0.0

        self.x_r = 0.025  # Define your geometric parameters
        self.y_r = 0.025  # Define your geometric parameters
        
        self.k_x   = 1.0  # control proportional gain
        self.k_y   = 1.0  # control proportional gain
        self.k_yaw = 0.05 # control proportional gain
        
        self.k_vx  = 0.0
        self.k_vy  = 0.0
        self.k_omg = 0.0

        self.f_v = 1.0
        self.f_omg = 1.0
        
        self.linear_speed_max = 0.22
        self.angular_speed_max = 2.84
        """ -------- End of Controller Gains --------- """

        # Trajectory attributes
        self.linear_speed_traj  = 0.0
        self.angular_speed_traj = 0.0

        self.x_traj   = 0.0
        self.y_traj   = 0.0
        self.yaw_traj = 0.0

        self.vx_traj  = 0.0
        self.vy_traj  = 0.0
        self.omg_traj = 0.0
        
        # ROS Node Setup
        rospy.init_node('my_node')      # Initialize ROS node
        rospy.loginfo("Initializing...")    
        self.rate = None
        self.exit_requested = False     # Flag to indicate program termination
        self.debug_flag = False
        
        # Initializing variables to store linear and angular speeds
        self.linear_speed = 0.0
        self.angular_speed = 0.0

        # Variable to store log data for post-analysis
        self.start_time = None              # Variable to store the start time
        self.current_idx=0
        self.log_data_buffer = []
        self.log_lines = []                 # List to store lines from the log file
        log_string = f"log_0.txt"           # Default name of the log file
        self.log_file_name = log_string
        read_string = f"log_0.txt"          # Default name of the log file
        self.read_file_name = read_string

        # VICON Pose and twist attributes
        self.position           = (0.0, 0.0, 0.0)       # Initializing position as a tuple (x, y, z)
        self.orientation        = (0.0, 0.0, 0.0, 0.0)  # Initializing orientation as a tuple (x, y, z, w)        
        self.linear_velocity    = (0.0, 0.0, 0.0)       # Initializing linear velocity as a tuple (dx, dy, dz)
        self.angular_velocity   = (0.0, 0.0, 0.0)       # Initializing angular velocity as a tuple (wx, wy, wz)

        # VICON Computed psi and omega attributes
        self.roll   = 0.0
        self.pitch  = 0.0
        self.yaw    = 0.0
        self.omega  = 0.0 

        # Create a Twist message to control the Turtlebot's linear and angular speeds
        self.msg = Twist()

        # Publish the Twist message to the '/cmd_vel' topic using ROS Publisher
        self.speed_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
      
        # Flag to control subscription to the VICON node for PoseStamped and TwistStamped messages
        self.is_pose_subscribed = False
        self.is_twist_subscribed = False
        # Subscription to the VICON
        self.pose_subscriber = None
        self.twist_subscriber = None
        
        # # Flag to control subscription to the own twist
        
        self.is_own_imu_subscribed   = False
        self.is_own_twist_subscribed = False
        # Subscription to the own twist
        self.own_twist_subscriber = None
        self.current_linear_x  = 0
        self.current_angular_z = 0
        self.own_imu_subscriber = None
        self.imu_angular_velocity = (0.0, 0.0, 0.0)       # Initializing angular velocity as a tuple (wx, wy, wz)

    def subscribe_own_twist(self):
        # Subscribe to the TwistStamped topic if not already subscribed
        if not self.is_own_twist_subscribed:
            self.own_twist_subscriber = rospy.Subscriber('/cmd_vel', Twist, self.own_twist_callback)
            self.is_own_twist_subscribed = True
            
    def own_twist_callback(self, twist_msg):
        # Callback function to handle Twist messages
        self.linear_speed  = twist_msg.linear.x
        self.angular_speed = twist_msg.angular.z

    def subscribe_own_imu(self):
        # Subscribe to the TwistStamped topic if not already subscribed
        if not self.is_own_imu_subscribed:
            self.own_imu_subscriber = rospy.Subscriber('/imu', Imu, self.own_imu_callback)
            self.is_own_imu_subscribed = True
            
    def own_imu_callback(self, imu_msg):
        # Callback function to handle Twist messages
        self.imu_angular_velocity  = (imu_msg.angular_velocity.x,
                                      imu_msg.angular_velocity.y,
                                      imu_msg.angular_velocity.z)
                                 
    def publish_speeds(self):       
        # Create a Twist message to control the Turtlebot's linear and angular speeds
        self.msg.linear.x  = self.linear_speed   # Set linear speed
        self.msg.angular.z = self.angular_speed  # Set angular speed
        # Publish the Twist message to the '/cmd_vel' topic using ROS Publisher
        self.speed_publisher.publish(self.msg)

    def log_to_buffer(self):
        if self.start_time is None:
            self.start_time = rospy.get_time()

        current_time = rospy.get_time() - self.start_time
        if self.debug_flag is False:
            log_data = f"{current_time:.4f}\t{self.linear_speed:.4f}\t{self.angular_speed:.4f}\t" \
                       f"{self.position[0]:.4f}\t{self.position[1]:.4f}\t" \
                       f"{self.yaw:.4f}\t" \
                       f"{self.linear_velocity[0]:.4f}\t{self.linear_velocity[1]:.4f}\t" \
                       f"{math.sqrt(math.pow(self.linear_velocity[0], 2) + math.pow(self.linear_velocity[1], 2)):.4f}\t" \
                       f"{self.imu_angular_velocity[2]:.4f}\n"
        else:   
            log_data = f"{current_time:.4f}\t{self.linear_speed:.4f}\t{self.angular_speed:.4f}\t" \
                       f"{self.position[0]:.4f}\t{self.position[1]:.4f}\t{self.position[2]:.4f}\t" \
                       f"{self.orientation[0]:.4f}\t{self.orientation[1]:.4f}\t{self.orientation[2]:.4f}\t{self.orientation[3]:.4f}\t" \
                       f"{self.roll:.4f}\t{self.pitch:.4f}\t{self.yaw:.4f}\t" \
                       f"{self.linear_velocity[0]:.4f}\t{self.linear_velocity[1]:.4f}\t{self.linear_velocity[2]:.4f}\t" \
                       f"{self.angular_velocity[0]:.4f}\t{self.angular_velocity[1]:.4f}\t{self.angular_velocity[2]:.4f}\n"
        # Append log data to buffer for post-analysis
        self.log_data_buffer.append(log_data)

    def write_log_data_to_file(self, log_file_name=None):
        if log_file_name is None:
            log_file_name = self.log_file_name
        else:
            self.log_file_name = log_file_name
        # Write accumulated log data to a file at the end of the program
        with open(log_file_name, 'w') as file:
            if self.debug_flag is False:
                header = "T (s)\tLin\tAng\tX\tY\tyaw\tdx\tdy\tv\twz\n"
            else:
                header = "T (s)\tLin\tAng\tX\tY\tZ\tq0\tq1\tq2\tq3\troll\tpitch\tyaw\tdx\tdy\tdz\twx\twy\twz\n"
            file.write(header)
            file.writelines(self.log_data_buffer)

    def read_from_file(self, read_file_name=None):        
        if read_file_name is None:
            self.read_file_name = self.log_file_name
        else:
            self.read_file_name = read_file_name
            
        # Open the log file in read mode
        with open(self.read_file_name, 'r') as file:
            # Skip the first line (header) in the log file
            file.readline()
            # Read each line in the log file, split by tabs, and store them in log_lines list
            for line in file:
                self.log_lines.append(line.split('\t'))

    def update_speeds(self):
        start_time = time.time()

        if self.log_lines:
            # Start updating speeds from the first entry
            if self.current_idx < len(self.log_lines) - 1:
                # current_time = float(self.log_lines[self.current_idx][0])
                # next_time = float(self.log_lines[self.current_idx + 1][0])
                self.linear_speed = float(self.log_lines[self.current_idx][1])
                self.angular_speed = float(self.log_lines[self.current_idx][2])
                self.current_idx += 1
            else:
                self.linear_speed  = 0.0
                self.angular_speed = 0.0
                self.exit_requested = True
                
    def update_traj(self):
        if self.log_lines:
            # Start updating speeds from the first entry
#            current_time = float(self.log_lines[self.current_idx][0])
#            next_time = float(self.log_lines[self.current_idx + 1][0])            
            if self.current_idx < len(self.log_lines) - 1:
                if self.debug_flag is False:
                    self.linear_speed_traj  = float(self.log_lines[self.current_idx][1])
                    self.angular_speed_traj = float(self.log_lines[self.current_idx][2])

                    self.x_traj   = float(self.log_lines[self.current_idx][3])
                    self.y_traj   = float(self.log_lines[self.current_idx][4])
                    self.yaw_traj = float(self.log_lines[self.current_idx][5])

                    self.vx_traj  = float(self.log_lines[self.current_idx][6])
                    self.vy_traj  = float(self.log_lines[self.current_idx][7])
                    self.omg_traj = float(self.log_lines[self.current_idx][9])
                else:
                    self.linear_speed_traj  = float(self.log_lines[self.current_idx][1])
                    self.angular_speed_traj = float(self.log_lines[self.current_idx][2])

                    self.x_traj   = float(self.log_lines[self.current_idx][3])
                    self.y_traj   = float(self.log_lines[self.current_idx][4])
                    self.yaw_traj = float(self.log_lines[self.current_idx][12])

                    self.vx_traj  = float(self.log_lines[self.current_idx][13])
                    self.vy_traj  = float(self.log_lines[self.current_idx][14])
                    self.omg_traj = float(self.log_lines[self.current_idx][18])                
                self.current_idx += 1
                
            elif self.current_idx == len(self.log_lines) - 1:
                self.linear_speed_traj  = 0.0
                self.angular_speed_traj = 0.0

                self.x_traj   = float(self.log_lines[self.current_idx][3])
                self.y_traj   = float(self.log_lines[self.current_idx][4])
                self.yaw_traj = float(self.log_lines[self.current_idx][5])

                self.vx_traj  = 0.0
                self.vy_traj  = 0.0
                self.omg_traj = 0.0

    def subscribe_vicon(self):
        # Subscribe to the PoseStamped topic if not already subscribed
        if not self.is_pose_subscribed:
            self.pose_subscriber = rospy.Subscriber(
                '/vrpn_client_node/turtlebot_1/pose',
                PoseStamped,
                self.pose_callback
            )
            self.is_pose_subscribed = True

        # Subscribe to the TwistStamped topic if not already subscribed
        if not self.is_twist_subscribed:
            self.twist_subscriber = rospy.Subscriber(
                '/vrpn_client_node/turtlebot_1/twist',  # Replace with your TwistStamped topic
                TwistStamped,
                self.twist_callback
            )
            self.is_twist_subscribed = True

    def unsubscribe_vicon(self):
        # Unsubscribe from the PoseStamped topic if already subscribed
        if self.is_pose_subscribed:
            if self.pose_subscriber is not None:
                self.pose_subscriber.unregister()
                self.pose_subscriber = None
            self.is_pose_subscribed = False

        # Unsubscribe from the TwistStamped topic if already subscribed
        if self.is_twist_subscribed:
            if self.twist_subscriber is not None:
                self.twist_subscriber.unregister()
                self.twist_subscriber = None
            self.is_twist_subscribed = False

    def pose_callback(self, data):
        # Callback function to handle PoseStamped messages
        self.position = (data.pose.position.x,
                         data.pose.position.y, data.pose.position.z)
        self.orientation = (
            data.pose.orientation.x,
            data.pose.orientation.y,
            data.pose.orientation.z,
            data.pose.orientation.w
        )
        # Update other attributes as needed
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion (self.orientation)
        

    def twist_callback(self, data):
        # Callback function to handle TwistStamped messages
        # Access linear and angular velocities from TwistStamped message
        self.linear_velocity = (data.twist.linear.x,
                                data.twist.linear.y, data.twist.linear.z)
        self.angular_velocity = (data.twist.angular.x,
                                 data.twist.angular.y, data.twist.angular.z)

        # Handle TwistStamped data here
        # Update other attributes or perform any necessary computations

        self.omega = 0.0  # Initializing yaw angle rate

    def controller(self):                                   # CONTROL ALGORITHM
        
        # Sensor current position and orientation
        x_sensor = self.position[0]
        y_sensor = self.position[1]
        psi_sensor = self.yaw
        
        '''Controller'''        
        # Desired trajectory attributes
        # Step X.0: Define a desired x position, other that 0.0.
        x_d =  0.0
        # Step Y.0: Define a desired psi oriantation
        """..."""

        # TASK4: uncomment these lines.
        # x_d = self.x_traj
        # y_d = self.y_traj
        
        # Step X.1: select the controller proportional gain, other that 0.0.
        k_x   = 0.0
        # Step Y.1: select the controller proportional gain
        """..."""
        # Step P.1: select the controller proportional gain
        """..."""
        
        # Feedback Terms
        # Step X.2: Compute the position error
        x_error = 0.0
        # Step Y.2: Compute the position error
        """..."""

        # Step X.3: Compute the desired velocity x-component.
        vx = 0.0
        # Step Y.3: Compute the desired velocity y-component.

        # Step X.4: Compute the feedback velocity command.
        # Step Y.4: Recompute the feedback velocity command.
        # HINT: if needed you can use math.sqrt() and math.pow(...,2) to compute 1/2 and 2 powers. 
        v_fb  = 0.0

        # Step P.0: DEFINE a desired yaw angle. Also set x_d =  0.0 such that the robor only turns.
        """..."""
        # Step Y.5: COMPUTE the desired yaw angle.
        # HINT: if needed you can use math.atan2(y,x) atan2(y, x) to compute the the angle ψ between
        # the positive x-axis and the ray from the origin to the point (x, y), confined to (−π, π].
        """..."""

        # Step P.2: Compute the orientation error
        """..."""
        
        # Step Avoid "U" turns
        # HINT: if needed you can use the math.copysign(1,x) to return the sign of the x variable and math.pi to return the value of π.
        # You can uncomment these 3 lines and follow the same structure
#        if abs("""...""") >= math.pi:
#            """...""" = """...""" - math.copysign(1,"""...""")*2*math.pi
#        """...""" = ("""..."""-"""...""")
 
        # Step P.4: Compute the desired angular velocity.
        """..."""

        # Step Feedfordward Terms
        """..."""
        """..."""
        
        # Step  Feedfordward + Feedback Terms
        """..."""
        """..."""


        # Step X.5: Sent the linear velocity command.
        self.linear_speed  = 0.0
        # Step Y.5: Sent the linear velocity command.
        self.linear_speed  = 0.0
        # Step P.5: Compute angular velocity command.
        self.angular_speed  = 0.0
        
        # Step Saturation: Saturate self.linear_speed and self.angular_speed
        # HINT: if needed you can use the max(x,y) and min(x,y) to compute the min and max between two values.
        # linear_speed_max = +self.linear_speed_max
        # linear_speed_min = -self.linear_speed_max
        # linear_speed_max = +self.linear_speed_max
        # linear_speed_min = -self.linear_speed_min
        
#        self.linear_speed  = max(-0.0,  min(0.0,   0.0))
#        self.angular_speed = max(-0.0,  min(0.0,   0.0))

        if self.current_idx >= len(self.log_lines):
            self.linear_speed  = 0
            self.angular_speed = 0       

    def cleanup(self):      
        # Shutdown ROS node
        rospy.signal_shutdown("Cleanup and exit")
        
        # Wait for rospy to finish shutting down
        while not rospy.is_shutdown():
            pass
        rospy.loginfo("KeyboardInterrupt received. Exiting gracefully...")
        # Exit Python script
        sys.exit(0)

    def record_traj(self, log_file_name=None):    
        # Subscribe to the topics
        self.subscribe_own_twist()
        self.subscribe_own_imu()
        self.subscribe_vicon()  
        try:
            rospy.loginfo("Running...")        
            self.rate = rospy.Rate(100) # 10hz
            while not rospy.is_shutdown() and not self.exit_requested:
                self.log_to_buffer()
                self.rate.sleep()
        except KeyboardInterrupt:
            pass
        finally:
            print("")
            self.exit_requested = True      # Set exit flag to True
            self.write_log_data_to_file(log_file_name)
            self.cleanup()
            
    def play_traj(self, read_file_name=None, log_file_name=None):      
        # Open the log file in read mode
        self.read_from_file(read_file_name) 
        # Subscribe to the topics
        self.subscribe_own_twist()
        self.subscribe_own_imu()
        self.subscribe_vicon()
        try:
            self.rate = rospy.Rate(100) # 10hz
            while not rospy.is_shutdown() and not self.exit_requested:
                # Update speeds from the first entry
                self.update_speeds()
                # Start publishing twist messages for robot movement
                self.publish_speeds()
                # Start logging speeds if the log flag is set
                self.log_to_buffer()
                self.rate.sleep()
        except KeyboardInterrupt:
            pass
        finally:
            print("")
            self.exit_requested = True      # Set exit flag to True
            self.write_log_data_to_file(log_file_name)
            self.cleanup()
                
    def control_traj(self, read_file_name=None, log_file_name=None):  
        # Open the log file in read mode
        self.read_from_file(read_file_name) 
        # Subscribe to the topics
        self.subscribe_own_twist()
        self.subscribe_own_imu()
        self.subscribe_vicon()
        try:
            self.rate = rospy.Rate(100) # 10hz
            while not rospy.is_shutdown() and not self.exit_requested:
                self.update_traj() # Update speeds from the first entry
                self.controller()
#                # Update speeds from the first entry
 #               self.update_speeds()
                # Start publishing twist messages for robot movement
                self.publish_speeds()
                # Start logging speeds if the log flag is set
                self.log_to_buffer()
                self.rate.sleep()
        except KeyboardInterrupt:
            pass
        finally:
            print("")
            self.exit_requested = True      # Set exit flag to True
            self.write_log_data_to_file(log_file_name)
            self.cleanup()
    
if __name__ == '__main__':
    obj = Turtlebot()   # Create an instance of the Turtlebot class
    #obj.record_traj()   # Execute the record_traj method to record the turtlebot manual trajectory
    #obj.record_traj("log_SecXX_LastName_Name.txt")
    #obj.play_traj()     # Execute the record_traj method to play back the turtlebot manual trajectory
    #obj.play_traj("log_SecXX_LastName_Name.txt", "log_plybck_SecXX_LastName_Name.txt")
    #obj.control_traj("log_SecXX_LastName_Name.txt", "log_ctrl_SecXX_LastName_Name.txt")  # Execute the control_traj method to feed back control the turtlebot trajectory
    
    
        # Uncomment only one line of code to execute:   
    
    # TASK1
    obj.record_traj("log_SecXX_LastName_Name.txt")      # Execute the record_traj  method to record            the turtlebot manual trajectory
    
    # TASK2
    #obj.play_traj("log_SecXX_LastName_Name.txt", "log_plybck_SecXX_LastName_Name.txt")        # Execute the record_traj  method to play back         the turtlebot manual trajectory

    # TASK3 and TASK 4
    #obj.control_traj("log_SecXX_LastName_Name.txt", "log_ctrl_SecXX_LastName_Name.txt")               # Execute the control_traj method to feed back control the turtlebot        trajectory
    
    # TASK5
    #obj.control_traj("NameOfYourFile.txt", "log_NameOfYourFile.txt")               # Execute the control_traj method to feed back control the turtlebot        trajectory        
     
    # TASK6
    #obj.control_traj("trajectoryRU_SOL.txt", "log_ctrl_SecXX_LastName_Name_RU.txt")               # Execute the control_traj method to feed back control the turtlebot        trajectory    
    