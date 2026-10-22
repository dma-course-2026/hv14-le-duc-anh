n = int(input("Nhập một số nguyên có 3 chữ số: "))
if n < 100 or n > 999:
    print("Số nhập vào không hợp lệ. Vui lòng nhập một số nguyên có 3 chữ số.")
else:
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10

print(f"Hàng trăm = {hang_tram}")
print(f"Hàng chục = {hang_chuc}")
print(f"Hàng đơn vị = {hang_don_vi}")
