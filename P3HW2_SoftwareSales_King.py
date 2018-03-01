# CTI-110
# P3HW2_SoftwareSales
# Lafayette King
# 2/28/2018



# A software company sells a package that retails for $99.

# Discounts are given based on quantity.
# Quantity 10-19: 10% discount
# Quantity 20-49: 20% discount
# Quantity 50-99: 30% discount
# Quantity 100+:  40% discount

# write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount and
# The total purchase cost with the discount applied.

def main ():
    

    NumberOfPackages = int(input('Enter the NumberOfPackages bought:'))

    PackagePrice = 99

    if NumberOfPackages < 10:
       discount = 0;
    elif NumberOfPackages < 20:
       discount = 0.10
    elif NumberOfPackages < 50:
       discount = 0.20
    elif NumberOfPackages < 100:
       discount = 0.30
    else:
       discount = 0.40
    PurchaseCost = NumberOfPackages * PackagePrice
    TotalDiscount = discount * PurchaseCost
    FinalCost = PurchaseCost - TotalDiscount
    print('Amount of discount: $' + format(TotalDiscount,',.2f'))
    print('FinalCost: $' + format(FinalCost,',.2f'))

main()
