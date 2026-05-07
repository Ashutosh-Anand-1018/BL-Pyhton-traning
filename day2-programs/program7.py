def convert_to_inches(length:int, width:int):
    """
    This function takes the length and width of a rectangle in centimeters and converts them to inches.
    """
    length_in_inches = length / 2.54
    width_in_inches = width / 2.54
    return length_in_inches, width_in_inches
def calculate_perimeter(length, width):
    """
    This function takes the length and width of a rectangle in inches and calculates its perimeter.
    """
    length_in_inches, width_in_inches = convert_to_inches(length, width)
    perimeter = 2 * (length_in_inches + width_in_inches)
    return perimeter
def calculate_area(length, width):
    """
    This function takes the length and width of a rectangle in inches and calculates its area.
    """
    length_in_inches, width_in_inches = convert_to_inches(length, width)
    area = length_in_inches * width_in_inches
    return area

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

perimeter = calculate_perimeter(length, width)
area = calculate_area(length, width)
print(f"Perimeter of the rectangle: {perimeter:.2f} inches and the area of the rectangle: {area:.2f} square inches")