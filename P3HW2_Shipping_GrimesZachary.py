# CTI-110 
# P3HW2 - Shipping Charges 
# Zachary Grimes 
# Wednesday September 12, 2018
#

useWeightOfPackage = int(input( "Please enter the weight of the package: " ))

if useWeightOfPackage <= 2:
    shippingCharges = 1.50
elif useWeightOfPackage < 7:
    shippingCharges = 3.00
elif useWeightOfPackage < 11:
    shippingCharges = 4.00
else:
    shippingCharges = 4.75
print()

print("For a package weighing " + str( useWeightOfPackage ) + \
      ", you'll pay $" + format( shippingCharges, ",.2f" ) + " per pound.")

