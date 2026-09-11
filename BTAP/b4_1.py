# int("abc")
# Lỗi ValueError

# int("3.14")
# Lỗi ValueError vì "3.14" phải qua float() trước

so_hop_le = int(float("3.14"))

print(so_hop_le)