from __future__ import division  # let 5/2 = 2.5 rather than 2

# Optimum Prop None
from Aerothon.ACMotor import ACMotor
import numpy as npy
import cmath as math
from scalar.units import MM, IN, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, LBF, inHg, K
from scalar.units import AsUnit
from Aerothon.AeroUtil import STDCorrection
from Adv2020Aircraft.Hardware.Batteries.Gens_6Cell_5000 import Gens_6Cell_5000

# Set Motor properties
Motor = ACMotor()
Motor.name = 'Hacker_A50_V3'
Motor.Battery = Gens_6Cell_5000
# Manufacturer Data
# Motor.Ri  = 0.026*OHM        #Coil resistance
# Motor.Io  = 1.1*A          #Idle current
# Motor.Kv  = 400*RPM/V      #RPM/Voltage ratio
# Matched data
Motor.Ri = .12 * OHM
Motor.Io = .5 * A
Motor.Kv = 400 * RPM / V

Motor.Vmax = 23.5 * V
Motor.Imax = 55 * A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm = 100000
Motor.Pz = 0.0

Motor.Weight = 445 * GRAM * gacc
Motor.LenDi = [46.8 * MM, 59.98 * MM]

#
# This data has been corrected for standard day
STD = STDCorrection(29.9 * inHg, (23.9 + 273.15) * K)
Arm = 19.5 * IN
#               RPM,          Torque           Current    Voltage
TestData = [(6210 * RPM, (7.5 * Arm * OZF) * STD, 34.8 * A, 23.0 * V),
            (5910 * RPM, (8.7 * Arm * OZF) * STD, 39.0 * A, 21.9 * V),
            (5610 * RPM, (9.9 * Arm * OZF) * STD, 44.2 * A, 21.5 * V),
            (5640 * RPM, (9.3 * Arm * OZF) * STD, 40.5 * A, 21.4 * V)]  # this is actual test data from a test stand

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