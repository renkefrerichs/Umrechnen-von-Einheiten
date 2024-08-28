#Menü
print("""Umrechnen von Grundrechenarten
         
         (1) Umrechnen von cm in m
         (2) Umrechnen von mA in A
         (3) Umrechnen von °C in F
         (4) Umrechnen von Km/h in m/s
         (5) Umrechnen von kg in g
         """)

num10= float(input("Wähle deine Umrechnung  "))

#Funktion ungültige Eingabe
if num10>5:
    print("ungültige Eingabe starte den Prozess neu")
if num10== 0:
    print("ungültige Eingabe starte den Prozess neu")

#Funktionen zur Berechnung bei Eingaben von 1-5
    
if num10== 1:
    #Wertangabe für cm Umrechnung
    num1= float(input("Gebe einen Wert in cm ein  "))
    #Formel
    Formel_m = (num1*pow( 10, -2 ))
    #Ausgabe
    print (num1, "cm", "sind", Formel_m, "Meter",)
    
if num10== 2:
    #Wertangabe für mA Umrechnung
    num2 = float(input("Gib einen wert in mA an  "))
    #Formel
    Formel_mA = (num2*pow( 10, -3 ))
    #Ausgabe
    print(" ")
    print (num2, "mA", "sind", Formel_mA, "A")

if num10== 3:
    #Werteingabe für °C Umrechnung
    num3 = float(input("Gib einen Wert in °C an  "))
    #Formel
    Formel_C = (num3*1.8+32)
    #Ausgabe
    print (" ")
    print (num3, "°C", "sind", Formel_C, "Fahrenheit")
    
if num10== 4:
    #Werteingabe für km/h Umrechnung
    num4 = float(input("Gib einen Wert in km/h  "))
    #Formel
    Formel_m_s = (num4/3.6)
    #Ausgabe
    print (" ")
    print (num4, "km/h", "sind", Formel_m_s, "m/s")
    
if num10== 5:
    #Werteingabe für kg Umrechnung
    num5 = float(input("Gib einen Wert in kg an  "  ))
    #Formel
    Formel_t =  (num5*pow(10, -3 ))
    #Ausgabe
    print(" ")
    print (num5, "kg", "sind", Formel_t, "t")
          
