import math

def calculate_circle_area():
  
    radius = float(input("Enter the radius of the circle: "))

    area = math.pi * radius ** 2
    
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

calculate_circle_area()