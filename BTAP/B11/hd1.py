import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5] # list Python thuan
diem_array = np.array(diem_list) # chuyen sang mang NumPy (ndarray)

print("Type list:", type(diem_list))
print("Type array:", type(diem_array))

# Phép toán vector hóa: cộng trực tiếp 0.5 vào TOÀN BỘ mảng
diem_cong_them = diem_array + 0.5
print("Mảng NumPy sau khi cộng:", diem_cong_them)

# So sánh với list thuần (cần dùng list comprehension)
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("List Python sau khi cộng:", diem_cong_them_list)

print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)