
while True :
    #Bedienoberfläche
    print("""          Umrechnen von Grundrechenarten
         _________________________________
        | (1) Umrechnen von cm in m       |
        | (2) Umrechnen von mA in A       |
        | (3) Umrechnen von °C in         |
        | (4) Umrechnen von Km/h in m/s   |
        | (5) Umrechnen von kg in g       |
        |                                 |
        | (0) Programm beenden            |
        |_________________________________|                                
        
        """)
        
    num10= float(input("Wähle deine Umrechnung  "))


    #Funktion ungültige Eingabe
    
    if num10>5:
        print("ungültige Eingabe starte den Prozess neu")
    if num10== 0:
        break
        
    #Funktionen zur Berechnung bei Eingaben von 1-5    
    if num10== 1:
        #Wertangabe für cm Umrechnung
        num1 = input("Gebe einen Wert in cm ein  ")
        num1 = num1.replace ("," , ".")
        num1 = float (num1)
        #Formel
        Formel_m = (num1*pow( 10, -2 ))
        #Ausgabe
        print (f"\n{num1} cm sind {Formel_m} Meter")
    
    if num10== 2:
        #Wertangabe für mA Umrechnung
        num2 = input("Gib einen wert in mA an  ")
        num2 = num2.replace ("," , ".")
        num2 = float (num2)
        #Formel
        Formel_mA = (num2*pow( 10, -3 ))
        #Ausgabe
        print (f"\n {num2} mA sind {Formel_mA} A")

    if num10== 3:
       #Werteingabe für °C Umrechnung
        num3 = input("Gib einen Wert in °C an  ")
        #Eingabefehlervorsorge 
        num3 = num3.replace ("," , ".")
        num3 = float (num3)
        #Formel
        Formel_C = (num3*1.8+32)
        #Ausgabe
        print (f"\n {num3} °C sind {Formel_C} Fahrenheit")
    
    if num10== 4:
        #Werteingabe für km/h Umrechnung
        num4 = input("Gib einen Wert in km/h  ")
        #Eingabefehlervorsorge
        num4 = num4.replace("," , ".")
        num4 = float (num4)
        #Formel
        Formel_m_s = (num4/3.6)
        #Ausgabe
        print (f"\n {num4} km/h sind {Formel_m_s} m/s")
    
    if num10== 5:
        #Werteingabe für kg Umrechnung
        num5 = input("Gib einen Wert in kg an  "  )
        #Eingabefehlervorsorge
        num5 = num5.replace("," , ".")
        num5 = float (num5)
        #Formel
        Formel_t =  (num5*pow(10, -3 ))
        #Ausgabe
        print (f"\n {num5} kg sind {Formel_t} t")
        
        #Neustart option
    neustart=input("\nmöchtest du neustarten? (y/n): ")
    if neustart == "n":
        
        break
        
    
        
