#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:44:24 2020

@author: dj-leech
"""

import matplotlib.pyplot as plt
import numpy as np

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele + '\n'  
    return str1 

# Name of g-code file
objectname = 'TEST'

strlist = []

# Starting positions
StartX = 60
StartY = 60

# Upper limit of print
UpperLimX = 140
UpperLimY = 140

# Number of 180 degree turns to be completed per layer
NoOfTurns = 25

# Offsetting the lower-left portion of the scaffold
CrossX = 1.1*StartX
CrossY = 0.9*StartY

CrossUpperX = UpperLimX - 0.1*StartX
CrossUpperY = UpperLimY + 0.1*StartY

# Preparing the printer for cold extrusion, relative coordinates and homing
strlist.append('M302 P1')
strlist.append('M83')
strlist.append('G28')
strlist.append('G1 X' + str(StartX) + ' Y' + str(StartY))

YDelta = (UpperLimY - StartY)/NoOfTurns

XDelta = (CrossUpperX - CrossX)/NoOfTurns

XCoord = StartX
YCoord = StartY

# Extrusion Multiplier
EMultiplier = 1
# Z-Height, amount to raise by per layer
ZPerLayer = 0.2

FullList = []
FullList.append([XCoord, YCoord])

# First layer
for i in range(NoOfTurns):
    if i%2 == 0:
        XCoord = UpperLimX
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        YCoord = YCoord + YDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
    else:
        XCoord = StartX
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        YCoord = YCoord + YDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])

# Depending on odd/even number bends, move to edge accordingly
if i%2 == 0:
    XCoord = StartX
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])
else:
    XCoord = UpperLimX
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])
    
FullList.append([XCoord, YCoord])

# Move up and out the way of the print whilst preparing for second layer
Command = 'G1 Z5 E10'
strlist.append(Command)
XCoord = 0.5*StartX
Command = 'G1 X' + str(XCoord)
strlist.append(Command)
FullList.append([XCoord, YCoord])
YCoord = 0.5*StartY
Command = 'G1 Y' + str(YCoord)
strlist.append(Command)
FullList.append([XCoord, YCoord])
Command = 'G1 X' + str(CrossX) + ' Y' + str(CrossY) + ' Z' + str(ZPerLayer)
strlist.append(Command)
XCoord = CrossX
YCoord = CrossY
FullList.append([XCoord, YCoord])

XCoord = CrossX
YCoord = CrossY

FullList.append([XCoord, YCoord])
    
# Second layer 
for i in range(NoOfTurns):
    if i%2 == 0:
        YCoord = CrossUpperY
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(ZPerLayer) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        XCoord = XCoord + XDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(ZPerLayer) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
    else:
        YCoord = CrossY
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(ZPerLayer) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        XCoord = XCoord + XDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(ZPerLayer) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        
if i%2 == 0:
    YCoord = CrossY
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])
else:
    YCoord = CrossUpperY
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])


Command = 'G1 Z5 E10'
strlist.append(Command)
XCoord = 0.5*StartX
Command = 'G1 X' + str(XCoord)
strlist.append(Command)
FullList.append([XCoord, YCoord])
YCoord = 0.5*StartY
Command = 'G1 Y' + str(YCoord)
strlist.append(Command)
FullList.append([XCoord, YCoord])
Command = 'G1 X' + str(CrossX) + ' Y' + str(CrossY) + ' Z' + str(ZPerLayer)
strlist.append(Command)
XCoord = StartX
YCoord = StartX
FullList.append([XCoord, YCoord])

# Third layer
for i in range(NoOfTurns):
    if i%2 == 0:
        XCoord = UpperLimX
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(2*ZPerLayer) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        YCoord = YCoord + YDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(2*ZPerLayer) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
    else:
        XCoord = StartX
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(2*ZPerLayer) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        YCoord = YCoord + YDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(2*ZPerLayer) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])

if i%2 == 0:
    XCoord = StartX
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])
else:
    XCoord = UpperLimX
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])


Command = 'G1 Z5 E10'
strlist.append(Command)
XCoord = 0.5*StartX
Command = 'G1 X' + str(XCoord)
strlist.append(Command)
FullList.append([XCoord, YCoord])
YCoord = 0.5*StartY
Command = 'G1 Y' + str(YCoord)
strlist.append(Command)
FullList.append([XCoord, YCoord])
Command = 'G1 X' + str(CrossX) + ' Y' + str(CrossY) + ' Z' + str(ZPerLayer)
strlist.append(Command)
XCoord = CrossX
YCoord = CrossY
FullList.append([XCoord, YCoord])

# Fourth layer (delete as applicable)
for i in range(NoOfTurns):
    if i%2 == 0:
        YCoord = CrossUpperY
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(3*ZPerLayer) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        XCoord = XCoord + XDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(3*ZPerLayer) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
    else:
        YCoord = CrossY
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(3*ZPerLayer) + ' E-' + str(5*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        XCoord = XCoord + XDelta
        Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord) + ' Z' + str(3*ZPerLayer) + ' E-' + str(1*EMultiplier)
        strlist.append(Command)
        FullList.append([XCoord, YCoord])
        
if i%2 == 0:
    YCoord = CrossY
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])
else:
    YCoord = CrossUpperY
    Command = 'G1 X' + str(XCoord) + ' Y' + str(YCoord)
    strlist.append(Command)
    FullList.append([XCoord, YCoord])

# Collate all instructions      
FullList = np.array(FullList)

Command = 'G1 Z10 E100'
strlist.append(Command)

strlist = listToString(strlist) 

# Write GCode file
text_file = open(objectname + '.gcode', 'w')
text_file.write(strlist)

# Plot rough movement, useful for visual checks of process
plt.plot(FullList[:,0],FullList[:,1])
