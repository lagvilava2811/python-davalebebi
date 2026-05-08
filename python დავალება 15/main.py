# ====================== დავალება 15 =======================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        if salary < 0:
            self.salary = 0
        else:
            self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    def work(self):
        print("Employee is working")

    def raise_salary(self, amount):
        if amount > 0:
            self.salary = self.salary + amount
            print(f"{self.name}'s salary increased by {amount}. New salary: {self.salary}")
        else:
            print("Amount must be positive")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print("Writing code...")

    def work(self):
        print("Developer is coding")


class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self):
        print("Creating design...")

    def work(self):
        print("Designer is designing")


# =================== ტესტი ===================

dev = Developer("Vako Lagvilava", 3000, "Python")
print("--- Developer ---")
dev.show_info()
dev.work()
dev.code()
dev.raise_salary(500)

print()

des = Designer("Dani Lagvilava", 2500, "Figma")
print("--- Designer ---")
des.show_info()
des.work()
des.create_design()
des.raise_salary(300)