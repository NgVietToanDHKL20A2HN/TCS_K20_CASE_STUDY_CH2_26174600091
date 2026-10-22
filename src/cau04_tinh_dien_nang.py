cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("--------------------Giá trị------------------------")
print(f"Diện năng tiêu thụ: {dien_nang_kwh} kWh")
print(f"Chi phí điện: {chi_phi} đ")
print("-----------------Kiểu dữ liệu----------------------")
print(f"Diện năng tiêu thụ: {type(dien_nang_kwh)}")
print(f"Chi phí điện: {type(chi_phi)}")