a = float(input("Nhập chiều dài hình chữ nhật: "))
b = float(input("Nhập chiều rộng hình chữ nhật: "))
s_hinh_chu_nhat = a * b
r = a / 2
s_hinh_tron = 3.14 * r * r
s_con_lai = s_hinh_chu_nhat - s_hinh_tron
print(f"Diện tích còn lại: {s_con_lai:.2f}")