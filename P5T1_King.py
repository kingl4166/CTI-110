

# CTI-110
# P5T1_Kilometer Converter
# Lafayette King
# 4/10/2018


# get the distance in kilometers.

xfactor = 0.6214
def main():
 

 kilometers = float(input("Enter distance in kilometers: "))
 Miles = kilometers * xfactor
 show_miles(kilometers)

def show_miles(km):
   
    miles = km * xfactor
    print(km,"kilometers equals",format(miles, ".2f"),"miles") 


main()


    
                      
