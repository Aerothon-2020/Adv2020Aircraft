from __future__ import division  # let 5/2 = 2.5 rather than 2

# Optimum Prop None
from Aerothon.ACMotor import ACMotor
import numpy as npy
import cmath as math
from scalar.units import MM, IN, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, LBF, inHg, K
from scalar.units import AsUnit
from Aerothon.AeroUtil import STDCorrection
from Adv2020Aircraft.Hardware.Batteries.Turnigy_6Cell_3300 import Turnigy_6Cell_3300

# Set Motor properties
Motor = ACMotor()
Motor.name = 'ScorpionSII4035'
Motor.Battery = Turnigy_6Cell_3300
# Manufacturer Data
# Motor.Ri  = 0.02*OHM        #Coil resistance
# Motor.Io  = 1.5*A          #Idle current
# Motor.Kv  = 320*RPM/V      #RPM/Voltage ratio
# Matched Data
Motor.Ri = 0.037 * OHM  # .15
Motor.Io = .69 * A  # 1.5
Motor.Kv = 250 * RPM / V  # 370
#
Motor.Vmax = 41.53 * V
Motor.Imax = 65 * A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm = 100000
Motor.Pz = 0.0

Motor.Weight = 450 * GRAM * gacc
Motor.LenDi = [46.8 * MM, 64.9 * MM]

#
# This data has been corrected for standard day
STD = STDCorrection(30.2 * inHg, (16.1 + 273.15) * K)
Arm = 24 * IN
#            RPM,        Torque                Current    Voltage
TestData = [(2490 * RPM, (38.9 * IN * OZF) * STD, 7.2 * A, 24.44 * V),
            (3743 * RPM, (119 * IN * OZF) * STD, 22.0 * A, 23.24 * V),
            (4470 * RPM, (207.7 * IN * OZF) * STD, 38.4 * A, 22.05 * V),
            (4661 * RPM, (246 * IN * OZF) * STD, 38.7 * A, 21.1 * V),
            (4813 * RPM, (275.3 * IN * OZF) * STD, 50.9 * A, 21.31 * V)]  # this is actual test data from a test stand
1
Motor.TestData = TestData

if __name__ == '__main__':
    import pylab as pyl

    print "V to Motor : ", AsUnit(Motor.Vmotor(Ib=3.75 * A), 'V')
    print "Efficiency : ", Motor.Efficiency(Ib=3.75 * A)
    print "Max efficiency : ", Motor.Effmax()
    print "Max efficiency current : ", AsUnit(Motor.I_Effmax(), 'A')
    print "Max efficiency RPM : ", AsUnit(Motor.N_Effmax(), 'rpm')

    Motor.PlotTestData()

    pyl.show()