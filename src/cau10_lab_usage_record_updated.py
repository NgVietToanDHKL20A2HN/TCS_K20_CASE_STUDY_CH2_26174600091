ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất thiết bị (W): "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia = float(input("Nhập đơn giá điện (VND/kWh): "))
from datetime import datetime

dien_nang_tieu_thu = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang_tieu_thu * don_gia
thoi_gian_su_dung = so_phut > 60
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
nhiet_do = so_phut * 1.96 - 18

print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat:.2f} W")
print(f"Nhiệt độ máy: {nhiet_do:.2f} °C")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng tiêu thụ: {dien_nang_tieu_thu:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Thời gian sử dụng có trên 60 phút? {thoi_gian_su_dung}")
print(f"Thời điểm ghi nhận: {thoi_diem_text}")
