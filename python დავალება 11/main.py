# # =================== დავალება 1 ===================

# def analyze_file(filename):
#     file = open(filename, "r")
#     lines = file.readlines()
#     file.close()
    
#     num_lines = len(lines)
    
#     longest_line = ""
#     for line in lines:
#         line = line.strip("\n")
#         if len(line) > len(longest_line):
#             longest_line = line
    
#     total_words = 0
#     for line in lines:
#         words = line.split()
#         total_words = total_words + len(words)
    
#     return num_lines, longest_line, total_words


# result = analyze_file("test.txt")
# print("Number of lines:", result[0])
# print("Longest line:", result[1])
# print("Total words:", result[2])

# ================ დავალება 2 ===================

# def count_word_in_file(filename, word):
#     file = open(filename, "r")
#     text = file.read()
#     file.close()
    
#     words = text.split()
    
#     count = 0
#     for w in words:
#         w = w.strip(".,!?;:()[]{}'\"")
#         if w.lower() == word.lower():
#             count = count + 1
    
#     return count

# result = count_word_in_file("test.txt", "test")
# print(result)

# ================= დავალება 3 ===================

# file = open("names.txt", "a")
# counter = 1

# while True:
#     first_name = input("Enter your first name: ")
    
#     if first_name == "stop":
#         break
    
#     last_name = input("Enter your last name: ")
    
#     file.write(str(counter) + ". " + first_name + " " + last_name + "\n")
#     counter = counter + 1

# file.close()

# ================= დავალება 4 ===================

file = open("persons.txt", "r")
lines = file.readlines()
file.close()

young_file = open("young.txt", "w")
old_file = open("old.txt", "w")

young_count = 0
old_count = 0

for line in lines:
    if line.strip() == "":
        continue
    
    age_str = line.split(", ")[1]
    age = int(age_str)
    
    if age < 50:
        young_file.write(line)
        young_count = young_count + 1
    elif age > 50:
        old_file.write(line)
        old_count = old_count + 1

young_file.close()
old_file.close()

print("Young people (under 50):", young_count)
print("Old people (over 50):", old_count)
print("Done! Check young.txt and old.txt")