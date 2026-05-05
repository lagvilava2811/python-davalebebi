# ============== დავალება 1 ==============
# def sum_user_numbers(times=5):
#     total = 0
    
#     for i in range(times):
#         num = int(input("Enter number: "))
#         total = total + num
    
#     return total


# result = sum_user_numbers()
# print(result)

# ============== დავალება 2 ==============
# def separate_odd_even(*args):
#     odd_numbers = []
#     even_numbers = []
    
#     for num in args:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
    
#     return odd_numbers, even_numbers


# odd, even = separate_odd_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print("კენტი:", odd)
# print("ლუწი:", even)

# ============== დავალება 3 ==============
# def word_count(sentence):
  
#     sentence = sentence.lower()
    
#     sentence = sentence.replace(".", " ")
#     sentence = sentence.replace(",", " ")
#     sentence = sentence.replace("!", " ")
#     sentence = sentence.replace("?", " ")
#     sentence = sentence.replace(";", " ")
#     sentence = sentence.replace(":", " ")
    
#     words = sentence.split()
    
#     word_dict = {}
    
#     for word in words:
#         if word in word_dict:
#             word_dict[word] = word_dict[word] + 1
#         else:
#             word_dict[word] = 1
    
#     return word_dict

# result = word_count("This is a test. This test is fun.")
# print(result)

# # ================== დავალება 4 ==================
# def word_count(sentence):
#     sentence = sentence.lower()
    
#     punctuation = [".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}"]
    
#     for p in punctuation:
#         sentence = sentence.replace(p, " ")
    
#     words = sentence.split()
    
#     word_dict = {}
    
#     for word in words:
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
    
#     return word_dict

# result = word_count("This is a test. This test is fun!")
# print(result)

