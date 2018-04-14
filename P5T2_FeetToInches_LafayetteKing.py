
# Convert Feet to Inches
# 4/13/2018
# CTI-110 P5T2_FeetToInches
# Lafayette King
#

# constant for the number of inches per foot
Inches_Per_Foot = 12

def main():
    feet = int(input("Enter a number of feet: "))
    print(feet, "equals", feet_to_inches(feet), " inches,") 


def feet_to_inches(feet):
    return feet * Inches_Per_Foot

main() 
