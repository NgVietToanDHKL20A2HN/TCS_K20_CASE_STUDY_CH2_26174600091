ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut_su_dung = int(input("Nhập số phút: "))
don_gia = float(input("Nhập đơn giá: "))
dien_nang_kwh = cong_suat_w * so_phut_su_dung / 60 / 1000
chi_phi = dien_nang_kwh * don_gia

print(f"Máy: {ma_may}")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} đ")