#function that determine the required paind for walls
import math
height = int(input("enter the height: "))
width = int(input("enter the widthe: "))
# to paint on square foot required 5 liter of paint
def paint(height,width):
    required_paint = height * width /5
    return required_paint


print(paint(height=height,width=width))