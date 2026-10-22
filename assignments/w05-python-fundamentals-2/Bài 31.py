h, p, giay = map(int, input("Nhập giờ, phút, giây: ").split())
if not (0 <= h < 24 and 0 <= p < 60 and 0 <= giay < 60):
    print("Không hợp lệ")
else:
    tong_giay = h * 3600 + p * 60 + giay
    tong_giay = (tong_giay + 1) % 86400
    h_moi = tong_giay // 3600
    p_moi = (tong_giay % 3600) // 60
    giay_moi = tong_giay % 60
    print(f"{h_moi} {p_moi} {giay_moi}")