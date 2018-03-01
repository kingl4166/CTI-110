# CTI-110
# P3HW1-Age Classifier
# Lafayette King
# 2/28/2018


# write a program that asks the user to enter a person's age.
# If the person is 1 year old or less, he or she is an infant.
# If the person is older than 1 year. but younger than 13 years, he or she is a
# child
# If the person is at least 13 years old, but less than 20 years old, he or she
# is a teenager.
# If the person is at least 20 years old, he or she is an adult.

def main ():
    yourAge = int(input('Please enter your age:'))
    if yourAge <= 1:
        print('you are an infant')
    elif yourAge < 13:
        print('you are a child')
    elif yourAge < 20:
        print('you are a teenager')
    else:
        print('you are an adult')


main()
