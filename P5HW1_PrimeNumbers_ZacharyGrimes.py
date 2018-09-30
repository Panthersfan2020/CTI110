# This project is about prime numbers
# Tuesday September 25, 2018
# CTI-110 P5HW1 - Prime Numbers
# Zachary Grimes
#

def isPrime( userNumber ):
    evenDivisions = 0
    if userNumber <= 1:
        return False
    for userNumber in range(1, userNumber + 1 ):
        if userNumber / userNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
        return True

def main():
    userNumber = int(input( "Please enter a number: " ) )
    print()
    if isPrime( userNumber ):
        print( userNumber, "is a prime number" )
    else:
        print( userNumber, "is NOT a prime number" )


main()
    
