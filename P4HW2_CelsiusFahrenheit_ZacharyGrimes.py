#This project ia sbout celcious to fahrenheit
 # Thursday September 20 2018
 # CTI-110 P4HW2 - Celsius to Fahrenheit Table
 # Zachary Grimes
 #

 
print("Celsius temperature\tFahrenheit Equivalent" )
for currentCelsiusTemperature in range( 21 ):
    fahrenheitTemperatureEquivalent = ( 9 / 5 ) * currentCelsiusTemperature + 32
    print(currentCelsiusTemperature,"\t\t\t\t", \
          format( fahrenheitTemperatureEquivalent, ".1f" ) )
    

           
          
