calSquareArea = lambda side_length:side_length ** 2
calRectangleArea = lambda length, width: length * width
calTriangleArea = lambda base, height: 0.5 * base * height

ts = int(input("Enter the side of the square: "))

print("Enter the base and height of the triangle:")
ht = int(input("Height: "))
bs = int(input("Base: "))

print("Enter the length and breadth of the rectangle:")
l = int(input("Length: "))
b = int(input("Breadth: "))

squareArea = calSquareArea(ts)
print("Area of the square:", squareArea)

triangle_area = calTriangleArea(bs, ht)
print("Area of the triangle:", triangle_area)

rectangle_area = calRectangleArea(l, b)
print("Area of the rectangle:", rectangle_area)
