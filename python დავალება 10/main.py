# ============== დავალება 1 ===================

# my_list = [(1, 3), (4, 2), (2, 5)]

# sorted_list = sorted(my_list, key=lambda x: x[1])

# print(sorted_list)

# ============== დავალება 2 ===================

# def divide_numbers():
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
        
#         result = num1 / num2
        
#         return result
    
#     except ValueError:
#         return "Error: Please enter valid integers only!"
    
#     except ZeroDivisionError:
#         return "Error: Cannot divide by zero!"


# print(divide_numbers())

# ============== დავალება 3 ===================

# from functools import reduce

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]

# cheap_products = filter(lambda p: p["price"] < 100, products)
# print("Products under 100:")
# for product in cheap_products:
#     print(product)

# print()

# product_info = map(lambda p: f"{p['name']} - {p['price']}$", products)
# print("All products:")
# for info in product_info:
#     print(info)

# print()

# sorted_products = sorted(products, key=lambda p: p["price"])
# print("Products sorted by price:")
# for product in sorted_products:
#     print(product)

# print()

# total_price = reduce(lambda total, p: total + p["price"], products, 0)
# print(f"Total price of all products: {total_price}$")

# ================= დავალება 4 ====================

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

print(sum_numbers(5))  
print(sum_numbers(10))