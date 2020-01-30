from __future__ import division  # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop             = ACPropeller()
Prop.name        = 'APC 24x12E'
Prop.D           = 24 * IN
Prop.Thickness   = 0.5 * IN

Prop.Pitch       = 12 * IN
Prop.dAlpha      = 3.3 * ARCDEG
Prop.Solidity    = 0.0126

Prop.AlphaStall  = 20 * ARCDEG
Prop.AlphaZeroCL = 0 * ARCDEG
Prop.CLSlope     = .078 / ARCDEG  # - 2D airfoil lift slope
Prop.CDCurve     = 2.2  # - 2D curvature of the airfoil drag bucket
Prop.CDp         = .02  # - Parasitic drag

Prop.Weight      = 150 * GRAM * gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W
Prop.PowerUnitName = 'watt'
Prop.MaxTipSpeed = None

#
# These are corrected for standard day
#
# Second set of data taken - concern about first set since taken at night
STD = STDCorrection(30.00 * inHg, (22 + 273.15) * K)

Prop.ThrustData = [(2179 * RPM, 19.28 * OZF * STD),
                   (2459 * RPM, 91 * OZF * STD),
                   (3124 * RPM, 147 * OZF * STD),
                   (3505 * RPM, 187 * OZF * STD),
                   (3693 * RPM, 205 * OZF * STD),
                   (3952 * RPM, 235 * OZF * STD)]  # this point taken after initial points on Hacker A50. Used to verify good data.

# Torque is calculated from motor kv and RPM
# Took torque data in closet with known prop to observe difference between temp
Prop.TorqueData = [(2072 * RPM, (47*STD*OZF*IN)),
                   (2730 * RPM, (81*STD*OZF*IN)),
                   (3182 * RPM, (132*STD*OZF*IN)),
                   (3659 * RPM, (200*STD*OZF*IN)),
                   (4414 * RPM, (331*STD*OZF*IN))],

################################################################################
if __name__ == '__main__':
    print " D     : ", AsUnit(Prop.D, 'in')
    print " Pitch : ", AsUnit(Prop.Pitch, 'in')

    Vmax = 50
    h = 0 * FT
    N = npy.linspace(1000, 6800, 5) * RPM

    Alpha = npy.linspace(-25, 25, 41) * ARCDEG
    V = npy.linspace(0, Vmax, 30) * FT / SEC

    Prop.CoefPlot(Alpha, fig=1)
    Prop.PTPlot(N, V, h, 'V', fig=2)


    N = npy.linspace(0, 13000,31)*RPM
    V = npy.linspace(0,Vmax,5)*FT/SEC

    Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    N = 6024 * RPM
    print
    print "Static Thrust   : ", AsUnit(Prop.T(N, 0 * FT / SEC, h), 'lbf')
    print "Measured Thrust : ", AsUnit(max(npy.array(Prop.ThrustData)[:, 1]), 'lbf')
    N = 6410 * RPM
    print
    print "Static Torque   : ", AsUnit(Prop.P(N, 0 * FT / SEC, h) / N, 'in*ozf')
    print "Measured Torque : ", AsUnit(max(npy.array(Prop.TorqueData)[:, 1]), 'in*ozf')

    pyl.show()