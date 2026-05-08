# ================== დავალება ===============================

class Student:
    status = True  
    pay = 1000

    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
        self.status = True  

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_discount(self):
        if self.age < 18:
            self.pay = self.pay * 0.8
        return self.pay

    def calculate_average(self):
        total = 0
        for grade in self.grades:
            total = total + grade
        return total / len(self.grades)

    def get_status(self):
        avg = self.calculate_average()

        if avg > 90:
            return "Excellent"
        if avg >= 70:
            return "Good"
        if avg >= 50:
            return "Average"

        self.status = False
        return "Poor"


s1 = Student("Vako", "Lagvilava", 35, [95, 88, 92, 78, 85])
s2 = Student("Nino", "Abazadze", 16, [45, 38, 52, 41, 47])
s3 = Student("Mariam", "Abashidze", 17, [55, 58, 52, 60, 54])

print(s1.get_full_name(), s1.get_status(), s1.get_discount())
print(s2.get_full_name(), s2.get_status(), s2.get_discount())
print(s3.get_full_name(), s3.get_status(), s3.get_discount())

print("\nAll students status:")
print("s1.status:", s1.status)
print("s2.status:", s2.status)
print("s3.status:", s3.status)