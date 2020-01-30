from scalar.units import GRAM, gacc, A, V, mAh, IN, LBF
from scalar.units import AsUnit
from Aerothon.ACMotor import ACBattery

Weight = []
Power = []

#Gens Ace

Gens_6Cell_5000 = ACBattery()
Gens_6Cell_5000.Voltage = 22.2*V
Gens_6Cell_5000.Cells = 6
Gens_6Cell_5000.Capacity = 5000*mAh
Gens_6Cell_5000.C_Rating = 45
Gens_6Cell_5000.Weight = 1.6*LBF
Gens_6Cell_5000.LWH = (1.84*IN,1.84*IN,6.1*IN) #inaccurate dimensions

Power.append( Gens_6Cell_5000.Power() )
Weight.append( Gens_6Cell_5000.Weight )

if __name__ == '__main__':
    print AsUnit( Gens_6Cell_5000.Imax, 'A' )