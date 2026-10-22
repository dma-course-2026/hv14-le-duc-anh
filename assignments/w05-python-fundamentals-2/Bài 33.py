import math
x0, y0, R = map(float, input("Nhập tâm (x0,y0) và bán kính R: ").split())
xa, ya = map(float, input("Nhập tọa độ điểm A: ").split())
d = math.sqrt((xa - x0)**2 + (ya - y0)**2)
if d < R:
    print("Điểm A nằm trong đường tròn")
elif d == R:
    print("Điểm A nằm trên đường tròn")
else:
    print("Điểm A nằm ngoài đường tròn")