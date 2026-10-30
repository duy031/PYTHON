import requests

print("=== BÀI TẬP 5.1 – GỌI GITHUB API ===")
response_github = requests.get("https://api.github.com/repos/python/cpython")

if response_github.status_code == 200:
    du_lieu_gh = response_github.json()
    print("Ten repository:", du_lieu_gh["full_name"])
    print("So luot gan sao (stars):", du_lieu_gh["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu_gh["language"])
else:
    print("Goi GitHub API that bai, ma loi:", response_github.status_code)

print("\n" + "="*40 + "\n")

print("=== BÀI TẬP 5.2 – GỌI API TỶ GIÁ NGOẠI TỆ ===")
response_rate = requests.get("https://open.er-api.com/v6/latest/USD")

if response_rate.status_code == 200:
    du_lieu_rate = response_rate.json()
    ty_gia_vnd = du_lieu_rate["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi:", response_rate.status_code)