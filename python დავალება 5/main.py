# ============ 1 ====================

# numbers = [11, 8, 24, 27, 9, 33, 18]

# total = 0
# count = 0

# for num in numbers:
#     total = total + num
#     count = count + 1

# average = total / count

# print("სია:", numbers)
# print("რიცხვების ჯამი:", total)
# print("რიცხვების საშუალო:", average)

# =========== 2 ====================

# original_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
# unique_list = []

# for item in original_list:
#     already_exists = False
#     for unique_item in unique_list:
#         if item == unique_item:
#             already_exists = True
#             break
#     if not already_exists:
#         unique_list.append(item)

# print("ორიგინალი სია:", original_list)
# print("უნიკალური ელემენტების სია:", unique_list)

# =========== 3 ====================

# import random

# random_numbers = []
# for i in range(20):
#     random_numbers.append(random.randint(-50, 50))

# even_numbers = [num for num in random_numbers if num % 2 == 0]

# print("პირველი სია (20 შემთხვევითი რიცხვი -50-დან 50-მდე):")
# print(random_numbers)
# print("\nმეორე სია (მხოლოდ ლუწი რიცხვები):")
# print(even_numbers)

# =========== 4 ====================

long_names = []
short_names = []

while True:
    user_input = input("შეიყვანეთ სახელი (stop/exit/quit - გასასვლელად): ")
    
    if user_input.lower() == "stop" or user_input.lower() == "exit" or user_input.lower() == "quit":
        print("პროგრამა დასრულდა!")
        break
  
    cleaned_name = user_input.strip()
    
    if len(cleaned_name) > 0:
        formatted_name = cleaned_name.capitalize()
        
        if len(formatted_name) > 3:
            long_names.append(formatted_name)
        else:
            short_names.append(formatted_name)

print("long_names:", long_names)
print("short_names:", short_names)




























