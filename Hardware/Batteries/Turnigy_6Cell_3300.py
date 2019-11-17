
from scalar.units import GRAM, gacc, A, V, mAh, IN, LBF
from scalar.units import AsUnit
from Aerothon.ACMotor import ACBattery

Weight = []
Power = []

#Thunder Power

Turnigy_6Cell_3300 = ACBattery()
Turnigy_6Cell_3300.Voltage = 22.2*V
Turnigy_6Cell_3300.Cells = 6
Turnigy_6Cell_3300.Capacity = 3300*mAh
Turnigy_6Cell_3300.C_Rating = 25
Turnigy_6Cell_3300.Weight = .915*LBF
Turnigy_6Cell_3300.LWH = (1.375*IN,1.875*IN,6.0*IN) #inaccurate dimensions

Power.append( Turnigy_6Cell_3300.Power() )
Weight.append( Turnigy_6Cell_3300.Weight )

if __name__ == '__main__':
    print AsUnit( Turnigy_6Cell_3300.Imax, 'A' )