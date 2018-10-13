# The project is called kilometer converter
# Monday september 24, 2018
# CTI-110 P5T1_KilometerConverter 
# Zachary Grimes
#
CONVERSION_FACTOR = 0.6214
def main():
    kilometers= float(input('Enter a distance in kilometers: '))

    show_miles(kilometers)

def show_miles(km):

    miles = km * CONVERSION_FACTOR


    print(km, 'kilometers equals ', miles, 'miles.')
    

main()
    
