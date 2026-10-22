tong_phut = 135
cong_suat_w = 250
so_gio_tron_ven = tong_phut // 60
so_phut_con_lai = tong_phut % 60
su_dung_lau = tong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print(su_dung_lau)
print(du_lieu_hop_le)
print("100 + 20 * 3 = ", 100 + 20 * 3)
print("100 + 20 * 3 = ", (100 + 20) * 3)