from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
######################################################################
# THIS PROPELLER WAS AN APC 19X10E THAT WAS CUT TO 18 INCH DIAMETER
######################################################################
Prop = ACPropeller()
Prop.name       = 'APC 18x10E_mod'
Prop.D          = 18*IN
Prop.Thickness  = 0.5*IN

Prop.Pitch      = 10*IN
Prop.dAlpha     = 5.0*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .0725/ARCDEG  #- 2D airfoil lift slope
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .02          #- Parasitic drag

Prop.Weight     = 87*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None

#
# These are corrected for standard day
#
#Standard correction
STD = STDCorrection(30.32*inHg, (5 + 273.15)*K)

#                 RPM,        Thrust
Prop.ThrustData = [(5661 *RPM, 167*OZF*STD),
                   (5010 *RPM, 128*OZF*STD),
                   (4500 *RPM, 102*OZF*STD),
                   (4088 *RPM, 85*OZF*STD),
                   (3514 *RPM, 61*OZF*STD)]

Arm = 19.5*IN*STD
Prop.TorqueData = [(5802  *RPM, (11.1*Arm*OZF)),
                   (5050  *RPM, (8.4*Arm*OZF)),
                   (4580  *RPM, (6.85*Arm*OZF)),
                   (4024  *RPM, (5.3*Arm*OZF)),
                   (3557  *RPM, (4.1*Arm*OZF))]

################################################################################
if __name__ == '__main__':
   
    print " D     : ", AsUnit( Prop.D, 'in')
    print " Pitch : ", AsUnit( Prop.Pitch, 'in')
    
    Vmax = 50
    h=0*FT
    N=npy.linspace(1000, 6800, 5)*RPM
    
    Alpha = npy.linspace(-25,25,41)*ARCDEG
    V     = npy.linspace(0,Vmax,30)*FT/SEC
    
    Prop.CoefPlot(Alpha,fig = 1)
    Prop.PTPlot(N,V,h,'V', fig = 2)

#
#    N = npy.linspace(0, 13000,31)*RPM
#    V = npy.linspace(0,Vmax,5)*FT/SEC
#
#    Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    N = 6024*RPM
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 6410*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show() 