# Calculates the area of a square
def calculate_square_area(side: float):
    return side * side

# Calculates the area of a rectangle with given length and width
def calculate_rectangle_area(length: float, width: float): 
    area = length * width
    return area 

# Calculates the area of a circle
def calculate_circle_area(radius: float):
    pi = 3.14
    area = pi * radius ** 2
    return area

# Testing
print("""
---------------
Area calculator
---------------
Select a shape:
""")

# Prompt the user to select a shape and wait
selection = input("""\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
""")

def calculate_area(selection):
    area = 0
# Square
    if selection == 'S':
        side = input("Enter the side: ")
        area = calculate_square_area(float(side))
# Rectangle
    elif selection == 'R':
        length = input("Enter the length: ")
        width = input("Enter the width: ")        
        area = calculate_rectangle_area(float(length), float(width))
# Circle    
    elif selection == 'C':
        radius = input("Enter the radius: ")
        area = calculate_circle_area(float(radius))
    else:
        print("Invalid selection. Choose 'S', 'R' or 'C'.")
    return area
def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    elif tag == 'C':
        shape = "circle"
    return shape 

area = calculate_area(selection)

print(f"The area of the {get_shape_name(selection)} is {area}")
