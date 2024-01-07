
import math
height = int(input("enter the height"))
width = int(input("enter the widthe"))

def paint_required(height,width):
    area = height* width
    color = math.ceil(area /5)
    return color
name = paint_required(height,width)
print(name)