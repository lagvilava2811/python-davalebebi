# ==================== 1 =========================

# sentence = input("შეიყვანეთ წინადადება: ")
# first_word = input("შეიყვანეთ სიტყვა რომლის ჩანაცვლებაც გსურთ: ")
# second_word = input("შეიყვანეთ ახალი სიტყვა: ")

# new_sentence = sentence.replace(first_word, second_word, 1)

# print("ახალი წინადადება:", new_sentence)


# ===================== 2 =========================

# sentence = input("შეიყვანეთ წინადადება: ")

# words = sentence.split()

# longest_word = ""
# longest_length = 0

# for word in words:
#     word_length = len(word)
    
#     if word_length > longest_length:
#         longest_length = word_length
#         longest_word = word

# print("ყველაზე გრძელი სიტყვაა:", longest_word)

# ===================== 3 =========================

word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")

word1 = word1.lower()
word2 = word2.lower()

if len(word1) != len(word2):
    print("ეს სიტყვები არ არის ანაგრამები")
else:
    temp_word2 = word2
    
    for letter in word1:
        index = temp_word2.find(letter)
        
        if index != -1:
            temp_word2 = temp_word2[:index] + temp_word2[index + 1:]
    
    if temp_word2 == "":
        print("ეს სიტყვები არის ანაგრამები")
    else:
        print("ეს სიტყვები არ არის ანაგრამები")
