# ================ დავალება 1 ====================

# import csv

# def add_users(n):
#     with open("users.csv", "w", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=["ID", "first_name", "last_name", "age"])
#         writer.writeheader()
        
#         for i in range(1, n + 1):
#             print(f"\n--- Person {i} ---")
#             first = input("First name: ")
#             last = input("Last name: ")
            
#             while True:
#                 try:
#                     age = int(input("Age: "))
#                     break
#                 except ValueError:
#                     print("Please enter a valid integer for age!")
            
#             writer.writerow({"ID": i, "first_name": first, "last_name": last, "age": age})
    
#     print(f"\nSuccessfully saved {n} persons to users.csv")

# n = int(input("How many persons do you want to enter? "))
# add_users(n)



# ================ დავალება 2 =================

import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    
    passed = []
    failed = []
    
    for row in reader:
        grade = int(row["Grade"])
        if grade > 50:
            passed.append(row)
        elif grade < 50:
            failed.append(row)

with open("passed_students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(passed)

with open("failed_students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(failed)

print(f"Passed: {len(passed)} students")
print(f"Failed: {len(failed)} students")
print("Done!")


