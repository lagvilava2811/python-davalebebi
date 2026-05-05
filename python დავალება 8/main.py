# ============ დავალება 1 ============

# def analyze_text(text):
#     uppercase_count = 0
    
#     for char in text:
#         if char.isupper():
#             uppercase_count += 1
    
#     uppercase_text = text.upper()
    
#     return uppercase_count, uppercase_text

# user_input = input("Enter your text: ")

# count, upper_result = analyze_text(user_input)

# print(f"Uppercase letters count: {count}")
# print(f"Uppercase text: {upper_result}")

# ============ დავალება 2 ============

def camel_to_snake(camel_case):
    snake_case = ""
    
    for i, char in enumerate(camel_case):
        if char.isupper():
            if i != 0:
                snake_case += "_"
            snake_case += char.lower()
        else:
            snake_case += char
    
    return snake_case

user_input = input("Enter camelCase variable name: ")

result = camel_to_snake(user_input)

print(f"Snake case: {result}")