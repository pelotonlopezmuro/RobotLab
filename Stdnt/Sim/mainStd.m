% ────────────────────────────────────────────────────────────────────────%
%                     ┬─┐┌─┐┌┐ ┌─┐┌┬┐  ┬  ┌─┐┌┐                           %
%                     ├┬┘│ │├┴┐│ │ │   │  ├─┤├┴┐                          %
%                     ┴└─└─┘└─┘└─┘ ┴   ┴─┘┴ ┴└─┘                          %
% ────────────────────────────────────────────────────────────────────────%
% Project Title: TurtleBot Simulation
% Author: Juan Lopez Muro
% Date: 01-16-2024
% Version 1.0
% Description: In this class, we will apply the concepts studied to an
% example. In the first stage, we will work in a simulated environment.
% Later, we will work on an actual experiment in the lab.
writeTrajectory(tq, xq, xq)
%% Clear workspace and command window
close all;
clear;
clc;
% Before going further, scan the whole script to get an idea of what
% we'll do!
%% Section 0: Data Preparation
obj = Turtlebot();   % Create a Turtlebot object! I named it "obj" because
% I am boring, you can call it something else :)

% Set the initial position and orientation. For now, set them to zero!
x0 = 0;%-2;
y0 = 0;%-0.8750;
psi0 = 0;%pi/2;
obj.set_states(x0, y0, psi0)

% Set the sampling time TS we'll use in this simulation, 0.01 will do!
obj.set_TS(0.01);

%% Section 1: Reference trajectory generation
% Create a time column vector, starting from 0s, up to 10s, in TS steps.
Time = [0:obj.TS:10]';

% Create a x and y reference position column vectors, of the same size as
% the time vector.
% This is an example of a step function, a good start.You can get creative!
xr = Time>1;                    % x position
yr = zeros(size(Time));         % y position
% Or you can use a fucntion, just like this!
[xr, yr] = trajectory(Time);    

% We can also plot the trajectory to see what it looks like! Is it a step?
plotTrajectory(Time, xr, yr) 
%%
log_lines = importdata('myTrajectory.txt').data;
Time = log_lines(:,1);
xr = log_lines(:,4);
yr = log_lines(:,5);
% We are going to store importan variables to ve able to plot them later in
% a data matrix: [ u1, u2, x, y, psi, vx, vy, v, wz]
data = zeros(length(Time), 9);

% This is the main simulation loop.
for i = 1:1:length(Time)    % we seep over the time vector
    % Reference at each time step:
    x_traj= xr(i);
    y_traj= yr(i);

    % Get the information from the sensors!
    [x_sensor, y_sensor, psi_sensor, vx_sensor, vy_sensor, omega_sensor] = obj.get_perfectSensor();
    % Yes, this is a "perfect" sensor that gives us true values. In real
    % life, these values are noisy. We can add some white noise to the
    % measuremnts!
    %     psi_sensor     =   psi_sensor    +  (-0.5 + rand(1,1))*10^-2;

    % Control: This is the importat part where we actually have to work.
    % Let's implement the control algorithm in a separate funtion.
    % [u] = obj.controller__(x_sensor, y_sensor, psi_sensor, x_traj, y_traj);
    [u] = controller(x_sensor, y_sensor, psi_sensor, x_traj, y_traj);

    data(i,:) = obj.get_log(); %[ u1, u2, x, y, psi, vx, vy, v, wz]

    % Bot simulation: Do not modify
    obj.move(u);
end
%%
plotTrajectory(Time, data(:,3), data(:,4))
plotOutputs(obj, Time, data, xr, yr)

%% Prepare for the race!
% In the "way_points_mid.txt" hwe have 3 columns that discrive a set of way
% point. Create a trajectory that 
% points

plotRace(obj, Time, data, xr, yr)
writeTrajectory(Time, xr, yr)
%%

function [xr, yr] = trajectory(Time)
%TRAJECTORY Bild your trajectory
%   This is an example
    xr = Time>1;
    yr = zeros(size(Time));
end

function [u] = controller(x, y, psi, x_traj, y_traj)

    % Position control
    v   = 1;
    yaw = 0;
    % Avoid "u" turns by keeping the error less that pi rad


    % Attitude control
    omg =  2;

    % Saturation
    % -u1sat < u1 < +u1sat
    % -u2sat < u1 < +u2sat

    [u] = [v, omg];
end


% function [u] = controller(x, y, psi, x_traj, y_traj)
% 
%     % Position control
%     x_error = (x_traj - x);
%     y_error = (y_traj - y);
% 
%     k_x = 2;
%     k_y = 2;
% 
%     vx = k_x*x_error;
%     vy = k_y*y_error;
%     v  = sqrt(vx^2 + vy^2);
%     yaw = atan2(vy,vx);
%     % Avoid "u" turns by keeping the error less that pi rad
%     yaw_error = (yaw-psi);
%     if abs(yaw_error) >= pi
%         yaw = yaw - sign(yaw_error)*2*pi;
%     end
%     yaw_error = (yaw-psi);
% 
%     % Attitude control
%     k_yaw = 3;
%     omg =  k_yaw*yaw_error;
% 
%     % Saturation
%     linear_speed_sat = 0.22;    % -u1sat < u1 < +u1sat
%     angular_speed_sat = 2.84;   % -u2sat < u1 < +u2sat
%     v  = max(-linear_speed_sat,  min(v,   linear_speed_sat ));
%     omg = max(-angular_speed_sat, min(omg, angular_speed_sat));
% 
%     [u] = [v, omg];
% end
%% Make some plots:

function plotTrajectory(Time, xr, yr)
%PLOTRAJECTORY Plot some outputs!
    fig = figure;
    ax = axes(fig);
    hold(ax, "on"), grid(ax, "on")
    xlabel(ax, 'Time (s)')
    ylabel(ax, 'x (m)')
    plot(ax, Time, xr, 'k')
    subplot(2,1,1,ax)
    
    ax = axes(fig);
    hold(ax, "on"), grid(ax, "on")
    xlabel(ax, 'Time (s)')
    ylabel(ax, 'y (m)')
    plot(ax, Time, yr, 'k')
    subplot(2,1,2,ax)
end

function plotOutputs(obj, Time, data, xr, yr)
%PLOTUTPUTS Plot some outputs!
    fig = figure;
    ax = axes(fig);
    hold(ax, "on"), grid(ax, "on")
    xlabel(ax, 'Time (s)')
    ylabel(ax, 'ex (m)')
    plot(ax, Time, xr-data(:,3), 'k')
    subplot(4,1,1,ax)
    
    ax = axes(fig);
    hold(ax, "on"), grid(ax, "on")
    xlabel(ax, 'Time (s)')
    ylabel(ax, 'ey (m)')
    plot(ax, Time, yr-data(:,4), 'k')
    subplot(4,1,2,ax)
    
    ax = axes(fig);
    hold(ax, "on"), grid(ax, "on")
    xlabel(ax, 'Time (s)')
    ylabel(ax, 'v (m/s)')
    plot(ax, Time, data(:,1), 'k')
    plot(ax, Time, data(:,8), '--r')
    yline(obj.linear_speed_sat,'--g')
    yline(-obj.linear_speed_sat,'--g')
    legend(ax, 'cmd','real','sat')
    subplot(4,1,3,ax)
    
    ax = axes(fig);
    hold(ax, "on"), grid(ax, "on")
    xlabel(ax, 'Time (s)')
    ylabel(ax, 'wz (rad/s)')
    plot(ax, Time, data(:,2), 'k')
    plot(ax, Time, data(:,9), '--r')
    yline(obj.angular_speed_sat,'--g')
    yline(-obj.angular_speed_sat,'--g')
    legend(ax,'cmd','real','sat')
    subplot(4,1,4,ax)
end
function plotRace(obj, Time, data, xr, yr)
%PLOTRACE Plot the race!
%     k = 0.25;
%     dy = -1.75/2;
%     dx = -2;
    way_points_mid = importdata("way_points_mid.txt").data(:,[2,3]);%+[dx, dy];
    way_points_int = importdata("way_points_int.txt").data(:,[2,3]);%+[dx, dy];
    way_points_ext = importdata("way_points_ext.txt").data(:,[2,3]);%+[dx, dy];
    fig = figure;
    ax = axes(fig);
    xlabel(ax, 'x (m)')
    ylabel(ax, 'y (m)')
    hold(ax, "on")
    plot(ax, way_points_mid(1:end-1,1), way_points_mid(1:end-1,2), '--k', 'LineWidth',2)
    plot(ax, way_points_mid(1,1), way_points_mid(1,2), '^k', 'LineWidth',2)
    plot(ax, way_points_mid(end-1,1), way_points_mid(end-1,2), 'vk', 'LineWidth',2)
    plot(ax, way_points_int(:,1), way_points_int(:,2), 'Color','#D95319', 'LineWidth',2)
    plot(ax, way_points_ext(:,1), way_points_ext(:,2), 'Color','#D95319', 'LineWidth',2)
    axis(ax, "padded", "equal")
    plot(ax, data(:,3), data(:,4),'-g', 'LineWidth',1.5)
end


function writeTrajectory(Time, xr, yr)
%WRITETRAJECTORY This file formats your trajectroy corrctly for the robot

% Sample data to write
saveData = zeros(length(Time),10);
saveData(:,1) = Time;
saveData(:,4) = xr;
saveData(:,5) = yr;

% Open a text file for writing
fid = fopen('myTrajectory.txt', 'w');

% Check if the file was successfully opened
if fid == -1
    error('Could not open the file for writing.');
end

% Write header
header = 'T (s)\tLin\tAng\tX\tY\tyaw\tdx\tdy\tv\twz\n';
fprintf(fid, header);

% Write data to the text file
for i = 1:length(Time)
    fprintf(fid, '%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\n', saveData(i,:));
end

% Close the file
fclose(fid);
end