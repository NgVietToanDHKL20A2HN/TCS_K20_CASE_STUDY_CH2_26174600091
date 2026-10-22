from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# Dự đoán kết quả phép trừ trước khi chạy: vì bat_dau và ket_thuc được gán bằng hàm datetime, với các số trong ngoặc chỉ năm-tháng-ngày-giờ-phút, nên khi làm phép trừ ket_thuc - bat_dau, sẽ cho ra sự khác biệt về thời gian hoặc khoảng thời gian ngăn cách giữa 2 hàm
# Sự khác nhau giữa datetime, str và timedelta:
# datetime: Cho ra ngày giờ, thời điểm câu lệnh được thực thi
# str: Cho ra một chuỗi ký tự
# timedelta: Sự chênh lệch/khác biệt/khoảng thời gian của 2 hàm thời gian