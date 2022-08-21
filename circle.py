# Promt user to enter the coordinates of the center 
x1,y1 = eval(input("Enter the coordinates of the center: "))

# Promt user to enter the radius of the circle
radius = eval(input("Enter the radius of the circle: "))

# Promt user to enter the coordinates of the point
x2,y2 = eval(input("Enter the coordinates of the point: "))

# Distance of the point from the center
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Print point lies inside, if its inside the circle
if distance < radius :
	print("Point lies inside the circle!")

# Print point lies outside, if its outside the circle 
if distance > radius :
	print("Point lies outside the circle!")