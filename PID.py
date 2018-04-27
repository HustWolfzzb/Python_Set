# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(2,GPIO.OUT)
# GPIO.setup(3,GPIO.OUT)
# GPIO.setup(4,GPIO.OUT)
# pwm=GPIO.PWM(2,80)
# pwm.start(20)
# GPIO.output(3,True)
# GPIO.output(4,False)
# file=open("/sys/class/thermal/thermal_zone0/temp") 
# Real_T=float(file.read())/1000 
# file.close()
# Ideal_T=28
# Delta=[0.6]
# Kp=11
# Ti=10000
# Td=0
# Output_PWM=20
# # times=0

# def All_of_List(a):
#     s=0
#     for i in range(len(a)):
#         s=s+a[i]
#     return s

# def Real_Temp():
#     file=open("/sys/class/thermal/thermal_zone0/temp") 
#     global Real_T
#     Real_T=float(file.read())/1000 
#     file.close()

# def Init():   
#     Real_Temp()
#     global Ideal_T
#     Ideal_T=33
#     global Delta
#     Delta=[0]
#     global Kp
#     Kp=8
#     global Ti
#     Ti=1
#     global Output_PWM
#     Output_PWM=20

# def update_Output(Time_Gap):
#     global Ideal_T
#     global Delta
#     global Kp
#     global Ti
#     global Td
#     global Output_PWM
#     global Real_T
#     P=Kp
#     I=Time_Gap/Ti
#     D=Td/Time_Gap
#     Increase=0
#     Real_Temp()
#     Delta.append(Real_T-Ideal_T)
#     # if Delta[-1]>-0.5 and  Delta[-1]<0.5:
#     Increase=P*(Delta[-1] + I * All_of_List(Delta) + D * (Delta[-1]-Delta[-2]))
#     Output_PWM=Output_PWM+Increase
#     if Output_PWM>100:
#         Output_PWM=100
#     elif Output_PWM<20:
#         Output_PWM=20


# Usage_time=[]
# # times=0

# def Find_Kp():
#     global Ideal_T
#     global Usage_time
#     global Delta
#     global Kp
#     global Ti
#     global Td
#     global Output_PWM
#     global Real_T
#     times=0
#     while True:
#         times=times+1
#         # if(times>100):
#         #     times=0
#         #     Init()
#         Time_Gap=1
#         time.sleep(Time_Gap)
#         if Delta[-1]<0.2 and Delta[-1]>-0.2:
#             Usage_time.append(times)
#             break
#         update_Output(Time_Gap)
#         global Output_PWM
#         pwm.ChangeDutyCycle(Output_PWM)
#         print "%d:%0.3f "%(times,Real_T)
#     delay=30
#     pwm.ChangeDutyCycle(10)
#     while delay>0:
#         time.sleep(1)
#         delay=delay-1
    


# x=10
# while x>0：
#     Find_Kp()
#     Kp=Kp-1
#     x=x-1

# for i in range(len(Usage_time)):
#     print Usage_time[i]


#coding: UTF-8
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
pwm=GPIO.PWM(2,80)
pwm.start(20)
GPIO.output(3,True)
GPIO.output(4,False)
file=open("/sys/class/thermal/thermal_zone0/temp")
Real_T=float(file.read())/1000
file.close()
Ideal_T=float(sys.argv[2])
Delta=[0.6]
Kp=float(sys.argv[1])
Ti=1000000
Td=0
Output_PWM=20
# times=0
def All_of_List(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]
    return s

def Real_Temp():
    file=open("/sys/class/thermal/thermal_zone0/temp")
    global Real_T
    Real_T=float(file.read())/1000
    file.close()

def Init(): 
    Real_Temp()
    global Ideal_T
    Ideal_T=33
    global Delta
    Delta=[0]
    global Kp
    Kp=8
    global Ti
    Ti=1
    global Output_PWM
    Output_PWM=20

def update_Output(Time_Gap,Kp):
    global Ideal_T
    global Delta
    global Ti
    global Td
    global Output_PWM
    global Real_T
    P=Kp
    I=Time_Gap/Ti
    D=Td/Time_Gap
    Increase=0
    Real_Temp()
    Delta.append(Real_T-Ideal_T)
    # if Delta[-1]>-0.5 and Delta[-1]<0.5:
    Increase=P*(Delta[-1] + I * All_of_List(Delta) + D * (Delta[-1]-Delta[-2]))
    Output_PWM=Output_PWM+Increase
    if Output_PWM>100:
        Output_PWM=100
    elif Output_PWM<10:
        Output_PWM=10

Usage_time=[]
# times=0

def Find_Kp(Kp):
    times=0
    while True:
        times=times+1
        # if(times>100):
        # times=0
        # Init()
        Time_Gap=1
        time.sleep(Time_Gap,Kp)
        if Delta[-1]<0.2 and Delta[-1]>-0.2 and times>100:
            Usage_time.append(times)
            print times
            break
        update_Output(Time_Gap)
        global Output_PWM
        pwm.ChangeDutyCycle(Output_PWM)
        print "%d:Temp %0.3f,Speed %0.3f"%(times,Real_T,Output_PWM)
    pwm.ChangeDutyCycle(5)
    delay=0

    # pwm.ChangeDutyCycle(0)
TryTime=10
while TryTime>0:
    Real_Temp()
    while Real_T<35:
        pass
    time.sleep(1)
    Find_Kp(Kp)
    Kp=1.2*Kp
    TryTime=TryTime-1



#!/usr/bin/python
#
# This file is part of IvPID.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# IvPID is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IvPID is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# title           :PID.py
# description     :python pid controller
# author          :Caner Durmusoglu
# date            :20151218
# version         :0.1
# notes           :
# python_version  :2.7
# ==============================================================================

"""Ivmech PID Controller is simple implementation of a Proportional-Integral-Derivative (PID) Controller in the Python Programming Language.
More information about PID Controller: http://en.wikipedia.org/wiki/PID_controller
"""
# import time

# class PID:
#     """PID Controller
#     """

#     def __init__(self, P=0.2, I=0.0, D=0.0):

#         self.Kp = P
#         self.Ki = I
#         self.Kd = D

#         self.sample_time = 0.00
#         self.current_time = time.time()
#         self.last_time = self.current_time

#         self.clear()

#     def clear(self):
#         """Clears PID computations and coefficients"""
#         self.SetPoint = 0.0

#         self.PTerm = 0.0
#         self.ITerm = 0.0
#         self.DTerm = 0.0
#         self.last_error = 0.0

#         # Windup Guard
#         self.int_error = 0.0
#         self.windup_guard = 20.0

#         self.output = 0.0

#     def update(self, feedback_value):
#         """Calculates PID value for given reference feedback
#         .. math::
#             u(t) = K_p e(t) + K_i \int_{0}^{t} e(t)dt + K_d {de}/{dt}
#         .. figure:: images/pid_1.png
#            :align:   center
#            Test PID with Kp=1.2, Ki=1, Kd=0.001 (test_pid.py)
#         """
#         error = self.SetPoint - feedback_value

#         self.current_time = time.time()
#         delta_time = self.current_time - self.last_time
#         delta_error = error - self.last_error

#         if (delta_time >= self.sample_time):
#             self.PTerm = self.Kp * error
#             self.ITerm += error * delta_time

#             if (self.ITerm < -self.windup_guard):
#                 self.ITerm = -self.windup_guard
#             elif (self.ITerm > self.windup_guard):
#                 self.ITerm = self.windup_guard

#             self.DTerm = 0.0
#             if delta_time > 0:
#                 self.DTerm = delta_error / delta_time

#             # Remember last time and last error for next calculation
#             self.last_time = self.current_time
#             self.last_error = error

#             self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

#     def setKp(self, proportional_gain):
#         """Determines how aggressively the PID reacts to the current error with setting Proportional Gain"""
#         self.Kp = proportional_gain

#     def setKi(self, integral_gain):
#         """Determines how aggressively the PID reacts to the current error with setting Integral Gain"""
#         self.Ki = integral_gain

#     def setKd(self, derivative_gain):
#         """Determines how aggressively the PID reacts to the current error with setting Derivative Gain"""
#         self.Kd = derivative_gain

#     def setWindup(self, windup):
#         """Integral windup, also known as integrator windup or reset windup,
#         refers to the situation in a PID feedback controller where
#         a large change in setpoint occurs (say a positive change)
#         and the integral terms accumulates a significant error
#         during the rise (windup), thus overshooting and continuing
#         to increase as this accumulated error is unwound
#         (offset by errors in the other direction).
#         The specific problem is the excess overshooting.
#         """
#         self.windup_guard = windup

#     def setSampleTime(self, sample_time):
#         """PID that should be updated at a regular interval.
#         Based on a pre-determined sampe time, the PID decides if it should compute or return immediately.
#         """
#         self.sample_time = sample_time