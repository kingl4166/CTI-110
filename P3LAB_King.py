# CTI-110
# P3TLAB: Debugging
# Lafayette King
# 2/28/2018
# program starts



def main ():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    

score = int(input('Enter score:'))

if score >= 90:
    print('Your grade is: A')
elif score >= 80:
    print('Your grade is: B')
elif score >= 70:
    print('Your grade is: C')
elif score >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
    print('You have failed this Test, better luck next time')


main ()

    
    
