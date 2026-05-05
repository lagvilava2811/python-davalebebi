# =============== საკლასო დავალება ===================

import csv
from faker import Faker
import random

fake = Faker()

persons = []

for i in range(1, 51):
    person = {
        "ID": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": random.randint(20, 80)
    }
    persons.append(person)

headers = persons[0].keys()

with open("persons.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(persons)

print("50 persons written to persons.csv")