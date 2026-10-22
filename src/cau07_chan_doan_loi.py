ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Lỗi 1:
# Tên tệp: /home/ndrew6075/TCS_K20/CASE_STUDY_CH2_MSSV/src/cau07_chan_doan_loi.py
# Số dòng: line 6
# Loại lỗi: SyntaxError (Lỗi cú pháp)
# Thông báo lỗi: '(' was never closed (Dấu '(' chưa được đóng)

# Nguyên nhân: Câu lệnh print ở dòng số 6 chưa được đóng ngoặc ')'
# Cách sửa: Thêm dấu ')' vào cuối câu lệnh ở dòng 6

# Lỗi 2:
# Tên tệp: /home/ndrew6075/TCS_K20/CASE_STUDY_CH2_MSSV/src/cau07_chan_doan_loi.py
# Số dòng: line 4
# Loại lỗi: TypeError (Lỗi kiểu)
# Thông báo lỗi: unsupported operand type(s) for *: 'str' and 'int' (Không hỗ trợ phép nhân giữa 'str' và 'int')

# Nguyên nhân: Biến 'cong_suat_w' là chuỗi (str), nhưng lại được sử dụng trong phép nhân với số nguyên (int)
# Cách sửa: Thêm (float) hoặc (int) trước input("Nhập công suất W: ") rồi mới nhân

# Lỗi 3:
# Tên tệp: /home/ndrew6075/TCS_K20/CASE_STUDY_CH2_MSSV/src/cau07_chan_doan_loi.py
# Số dòng: line 6
# Loại lỗi: NameError (Lỗi tên)
# Thông báo lỗi: name 'dien_nang' is not defined (Tên 'dien_nang' chưa được định nghĩa)

# Nguyên nhân: Biến 'dien_nang' chưa được định nghĩa trước khi sử dụng trong câu lệnh print
# Cách sửa: Thay 'dien_nang' bằng 'dien_nang_kwh' trong câu lệnh print ở dòng 6