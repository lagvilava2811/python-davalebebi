# =============================დავალება 1===============================
# number = int(input("შეიყვანეთ რიცხვი: "))

# factorial = 1

# for i in range(1, number + 1):
#     factorial = factorial * i

# print(f"{number}! = {factorial}")


# =============================დავალება 2===============================

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")
#     print()

# # ==============================დავალება 3===============================

service_cost = 50
remaining = service_cost

print(f"გადასახდელი თანხა: {remaining} ლარი")

while remaining > 0:
    money = int(input("მოათავსეთ კუპიურა (5, 10 ან 20): "))
    
    if money == 5 or money == 10 or money == 20:
        remaining = remaining - money
        
        if remaining > 0:
            print(f"დარჩენილი გადასახდელი: {remaining} ლარი")
        elif remaining == 0:
            print("ხურდა: 0 ლარი")
            print("გმადლობთ სერვისით სარგებლობისთვის!")
        else:
            print(f"ხურდა: {-remaining} ლარი")
            print("გმადლობთ სერვისით სარგებლობისთვის!")
    else:
        print("გთხოვთ შეიტანეთ ვალიდური კუპიურა (5, 10 ან 20)")