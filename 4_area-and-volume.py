"""You will write four functions for this exercise. The functions area() and perimeter() have
length and width parameters and the functions volume() and surfaceArea() have length,
width, and height parameters. These functions return the area, perimeter, volume, and surface
area, respectively."""

def area(length, width):
    return length * width

def perimeter(length, width):
    return length + width + length + width

def surfaceArea(length,width,height):
    return ((length * width *2) + (length * height * 2) + (width * height * 2))

def volume(length, width,height):
    return length * width * height

print(surfaceArea(20,10,7))