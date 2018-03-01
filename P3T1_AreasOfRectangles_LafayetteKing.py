# CTI - 110
# P3T1_Areas of Rectangle
# Lafayette King
# 2/22/2018 
# Calculate the area of two Rectangles
# Calculate the largest of the two
# Determine if both are equal


# Calculate Rec1 length and width.
length1 = int(input('Enter the length of Rec1:'))
width1 = int(input('Enter the width of Rec1:'))

# Calculate Rec2 length and width.
length2 = int(input('Enter the length of Rec2:'))
width2 = int(input('Enter the width of Rec2:'))

# Calculate the areas of the Rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Calculate which has the largest area.
if area1 > area2:
    print('Rec1 has the largest area.')
elif area2 > area1:
    print('Rec2 has the largest area.')
else:
    print('Both have the same area.') 
