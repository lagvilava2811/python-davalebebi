# ============== დავალება 1 ==============
persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:
    first_name = input("Enter first name (or 'stop' to exit): ")
    
    if first_name == "stop":
        print("Program stopped")
        break
    
    matching_persons = []
    for person in persons:
        if person[0] == first_name:
            matching_persons.append(person)
    
    if not matching_persons: 
        print("Name not found")
        continue
     
    last_name = input("Enter last name: ")
    
    found = False
    for person in matching_persons:
        if person[1] == last_name:
            print(f"Age: {person[2]}")
            found = True
            break
    
    if not found:
        print("Last name not found for this name")

# ============== დავალება 2 ==============

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")

# set1 = set(word1)
# set2 = set(word2)

# common = set1 & set2  

# different = set1 ^ set2  

# union = set1 | set2  

# print(f"\nFirst word: {word1}")
# print(f"Second word: {word2}")
# print(f"\nსაერთო სიმბოლოები (common): {common}")
# print(f"განსხვავებული სიმბოლოები (different): {different}")
# print(f"გაერთიანებული სიმბოლოები (union): {union}")