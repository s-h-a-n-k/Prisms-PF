#!/usr/bin/env python3

# Calculates the total area of the interface

# For 2D systems, it calculates the total intertface length

import sys
from visit import *

loc=sys.argv[1]
var=sys.argv[2]
bound=sys.argv[3]
sloc=sys.argv[4]

# Step 1: Open a database (all time steps)
db=loc+"solution-*.vtu database"
OpenDatabase(db)

# Step 2: Add Contour plot (using variable "n")
# This variable must be in the range [0,1]
# with 0 representing one phase, 1 representing another phase
# and n=0.5 representing the midpoint accross the interface
AddPlot("Contour", var, 1, 1)
ContourAtts = ContourAttributes()
ContourAtts.contourValue = (float(bound))
ContourAtts.contourMethod = ContourAtts.Value
SetPlotOptions(ContourAtts)

#Step 3: Draw the plot
DrawPlots()

# Step 5: Animate through time and save images
intarea=[0.0]*TimeSliderGetNStates()
ofnm=sloc+"iarea_vs_t.txt"
outF = open(ofnm, "w")
print("Step\tTime\tInterfacial Area")
outF.write("Step\tTime\tInterfacial Area\n")
for states in range(TimeSliderGetNStates()):
    try:
        SetTimeSliderState(states)
        Query("Time")
        t = GetQueryOutputValue()
        qresp=Query("Weighted Variable Sum")
        wvs=GetQueryOutputValue()
    #Weighted Variable Sum integrates the value of the order
    #parameter along the area (length) of the contour
    #surface (curve).
    #Since the countour is taken at value n=0.5,
    #We multiply by 2 to obtain the area (or length)
        if wvs == ():
            intarea[states]=0.0
        else:
            intarea[states]=2.0*wvs
    except:intarea[states]=0.0;
    print("% d, %.1f, %.5f" %(states, t, intarea[states]))
    outF.write("%d\t%.1f\t%.5f\n" %(states, t, intarea[states]))
outF.close()
try:DeleteAllPlots();CloseDatabase(db);
except:pass;
sys.exit()
