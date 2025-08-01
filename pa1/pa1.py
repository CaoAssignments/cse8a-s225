x_center_str = input("Enter coordinate x_center:")
y_center_str = input("Enter coordinate y_center:")
x_p1_str = input("Enter coordinate x_p1:")
y_p1_str = input("Enter coordinate y_p1:")
x_p2_str = input("Enter coordinate x_p2:")
y_p2_str = input("Enter coordinate y_p2:")

x_center = float(x_center_str)
y_center = float(y_center_str)
x_p1 = float(x_p1_str)
y_p1 = float(y_p1_str)
x_p2 = float(x_p2_str)
y_p2 = float(y_p2_str)

area_circle1 = 3.14 * ((x_center - x_p1)**2 + (y_center - y_p1)**2)
area_circle2 = 3.14 * ((x_center - x_p2)**2 + (y_center - y_p2)**2)

area_ring = abs(area_circle1 - area_circle2)
area_ring_rounded = round(area_ring, 2)

print("Area of ring shape =", area_ring_rounded+1)
