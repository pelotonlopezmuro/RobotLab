# -*- coding: utf-8 -*-
"""───────────────────────────────────────────────────────────────────────
                     ┬─┐┌─┐┌┐ ┌─┐┌┬┐  ┬  ┌─┐┌┐                           
                     ├┬┘│ │├┴┐│ │ │   │  ├─┤├┴┐                          
                     ┴└─└─┘└─┘└─┘ ┴   ┴─┘┴ ┴└─┘                          
 ────────────────────────────────────────────────────────────────────────"""
"""
    Project Title: TurtleBot python plotting tamplate
    Author: Juan Lopez Muro, Cecilia Diaz
    Date: 01-21-2024
    Version 1.0
    Description: This template only serves to get the students started 
    recognizing the file variables. It is up to the student to preprocess the 
    data correctly according to their needs.
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

# Read the log file into a DataFrame
log_file_name = 'log_test.txt'  # Replace with your log file name
data = pd.read_csv(log_file_name, delimiter='\t')

# Extract columns from the DataFrame
t = data['T (s)']   # time
lin = data['Lin']   # u1
ang = data['Ang']   # u2
x = data['X']       # x1
y = data['Y']       # x1
yaw = data['yaw']   # x3
vx = data['dx']     # dx1
vy = data['dy']     # dx2
v = data['v']       # sqrt(vx**2 + vy**2)
wz = data['wz']     # dx3

# Number of initial values to disregard (change this value as needed)
n = 10

# Plotting (t, lin) (t, ang) (t, x) (t, y), and (x, t)
plt.figure(figsize=(15, 10))
plt.subplot(3, 3, 1)
plt.plot(t[n:], v[n:], label='2-Norm of Measured Lin Vel VICON')
plt.plot(t[n:], lin[n:], label='Comanded Linear Velocity')
plt.xlabel(r'Time (s)')
plt.ylabel(r'Linear Speed (m/s)')
plt.legend()

plt.subplot(3, 3, 2)
plt.plot(t[n:], wz[n:], label='IMU Angular Velocity')
plt.plot(t[n:], ang[n:], label='Comanded Angular Velocity')

plt.xlabel(r'Time (s)')
plt.ylabel(r'Angular Speed (rad/s)')
plt.legend()

plt.subplot(3, 3, 3)
plt.plot(t[n:], yaw[n:])
plt.xlabel(r'Time (s)')
plt.ylabel(r'$\psi$ (rad)')

plt.subplot(3, 3, 4)
plt.plot(t[n:], x[n:])
plt.xlabel(r'Time (s)')
plt.ylabel(r'x (m)')

plt.subplot(3, 3, 5)
plt.plot(t[n:], y[n:])
plt.xlabel(r'Time (s)')
plt.ylabel(r'y (m)')

plt.subplot(3, 3, 6)
plt.plot(x[n:], y[n:])
plt.xlabel(r'x (m)')
plt.ylabel(r'y (m)')
plt.axis(r'equal')  # Set equal aspect ratio for the plot

plt.subplot(3, 3, 7)
plt.plot(t[n:], vx[n:])
plt.xlabel(r'Time (s)')
plt.ylabel(r'$v_x$ (m/s)')

plt.subplot(3, 3, 8)
plt.plot(t[n:], vy[n:])
plt.xlabel(r'Time (s)')
plt.ylabel(r'$v_y$ (m/s)')

plt.subplot(3, 3, 9)
plt.plot(t[n:], wz[n:])
plt.xlabel(r'Time (s)')
plt.ylabel(r'$\omega$ (rad/s)')

plt.tight_layout()
plt.show()

"""
# Plotting (t, lin) (t, ang) (t, x) (t, y), and (x, t)
#plt.figure(figsize=(15, 10))
plt.figure()

#plt.subplot(3, 3, 6)
plt.plot(x[n:], y[n:])
plt.xlabel(r'x (m)')
plt.ylabel(r'y (m)')
plt.axis(r'equal')  # Set equal aspect ratio for the plot

plt.tight_layout()
plt.show()
"""