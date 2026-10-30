import pandas as pd

# Đọc file CSV
df = pd.read_csv("diem_sinh_vien.csv")

print("--- 5 dòng đầu tiên ---")
print(df.head()) # xem 5 dòng đầu

print("\n--- Kích thước dữ liệu (số dòng, số cột) ---")
print(df.shape) # số dòng, số cột

print("\n--- Danh sách tên cột ---")
print(df.columns.tolist()) # danh sách tên cột