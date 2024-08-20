#Bedienoberfläche
num1 = float(input("Gib einen Wert in cm an"))
num2 = float(input("Gib einen wert in mA an"))
num3 = float(input("Gib einen Wert in °C an"))
num4 = float(input("Gib einen Wert in km/h"))
num5 = float(input("Gib einen Wert in kg an"))
#Mathematische Operation
Formel_m = (num1*pow( 10, -2 ))
Formel_mA = (num2*pow( 10, -3 ))
Formel_C = (num3*1.8+32)
Formel_m_s = (num4/3.6)
Formel_t =  (num4*pow(10, -3 ))
#Anzeige
print (" ")
print (num1, "cm", "sind", Formel_m, "Meter",)
print (num2, "mA", "sind", Formel_mA, "A")
print (num3, "°C", "sind", Formel_C, "Fahrenheit")
print (num4, "km/h", "sind", Formel_m_s, "m/s")
print (num5, "kg", "sind", Formel_t, "t")