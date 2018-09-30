# CTI-110 
# P3LAB- Debugging
# Zachary Grimes
# Wednesday September 12, 2018
#

def main():
    #This program takes a number grade and outputs a letter grade.

    #system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores

    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score > B_score:
            print('Your grade is: B')
        else:
            print('Your grade is: F') # TO DO: finish this


#Program start
main()
