



# Test Grade Average
# 4/17/2018
# CTI-110 P5WH1- Test Average and Grade
# Lafayette King
#
# sc1 is my short version of score.
def main():
    
    A = 90 - 100
    B = 80 - 89
    C = 70 - 79
    D = 60 - 69
    F =  0 - 59

    score = int(input("Please enter score "))
    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif score > 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    print("Your grade is", grade)
    print()
main()
def calc_average():
 sc1=int(input("Enter score " ))
 sc2=int(input("Enter score " ))
 sc3=int(input("Enter score " ))
 sc4=int(input("Enter score " ))
 sc5=int(input("Enter score " ))

 calc_average=(sc1+sc2+sc3+sc4+sc5)/5
 print("Your average is",calc_average)
 if calc_average>=90:
                grade="A"
 elif calc_average>=80:
                grade="B"
 elif calc_average>=70:
                grade="C" 
 elif calc_average>=60:
                grade="D"
 elif calc_average<=60:
                grade="F"

calc_average()
    
main()    
          
              
          
          
       










          



         


    



