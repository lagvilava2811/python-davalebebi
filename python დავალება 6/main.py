# ================ დავალება 1 ================
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print(squares)

squares_comprehension = {i: i ** 2 for i in range(1, 11)}
print(squares_comprehension)

# =============== დავალება 2 ================
products = [
    {"cola": {"price": 1.5, "quantity": 10}},
    {"fanta": {"price": 2.5, "quantity": 5}},
    {"snickers": {"price": 3.5, "quantity": 12}},
    {"water": {"price": 4.5, "quantity": 8}},
    {"beer": {"price": 6.5, "quantity": 5}}
]

print("პროდუქტების დასახელებები:")
for product in products:
    for name in product:
        print(f"  - {name}")

total_value = 0
for product in products:
    for name, info in product.items():
        price = info["price"]
        quantity = info["quantity"]
        product_value = price * quantity
        total_value += product_value
        print(f"{name}: {price} × {quantity} = {product_value}")

print(f"\nყველა პროდუქტის ღირებულების ჯამი: {total_value}")

# =============== დავალება 3 ================
# fruit_count = {}

# while True:
#     fruit = input("Enter your favorite fruit: ")
    
#     if fruit == "stop":
#         break
    
#     if fruit in fruit_count:
#         fruit_count[fruit] += 1
#     else:
#         fruit_count[fruit] = 1

# print(fruit_count)















