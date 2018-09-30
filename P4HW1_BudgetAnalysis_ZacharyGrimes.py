# The project is about Budget ANALYSIS
# Thursday September 20 2018
# CTI-110 P4HW1 - Budget Analysis
# Zachary Grimes
#

userBudget = float( input("Please enter how much you've budgeted " + \
                          "for the month: " ))
moreExpenses ="y"
userTotalExpenses = 0

while moreExpenses =="y":
     userExpense = float(input("Enter an expense: " ))
     userTotalExpenses += userExpense
     moreExpenses+= input( "Do you have more expenses?: Type y "+ \
                            "for yes, any key for no: " )

print()
if userTotalExpenses > userBudget:
    print("You were over your budget of","$" + format(userBudget, ",.2f" ), \
          "by","$" + format(userTotalExpenses - userBudget, ",.2f" ) )
elif userTotalExpenses > userBudget:
    print("You were over your budget of","$" + format(userBudget, ",.2f" ), \
          "by","$" + format(userBudget - userTotalExpenses, ",.2f" ) )
else:
    print("You used exactly your budget of", \
          "$" + format( userBudget , ",.2f"),".")
    
          


    
