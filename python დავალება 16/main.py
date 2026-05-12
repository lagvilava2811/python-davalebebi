# ===================== დავალება 1 ==========================

# class BankAccount:
#     bank_name = "MyBank"
#     __total_accounts = 0

#     def __init__(self, owner, balance):
#         self._owner = owner

#         if BankAccount.validate_amount(balance):
#             self.__balance = balance
#         else:
#             self.__balance = 0
#             print("შეცდომა: ბალანსი უნდა იყოს დადებითი, დაყენდა 0-ზე")

#         BankAccount.__total_accounts += 1
#         self.__account_number = f"AN{BankAccount.__total_accounts:04d}"

#     def deposit(self, amount):
#         if BankAccount.validate_amount(amount):
#             self.__balance += amount
#             print(f"წარმატებით ჩაირიცხა {amount} ლარი. ახალი ბალანსი: {self.__balance} ლარი")
#         else:
#             print("შეცდომა: თანხა უნდა იყოს დადებითი!")

#     def withdraw(self, amount):
#         if BankAccount.validate_amount(amount):
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 print(f"წარმატებით გამოიტანეს {amount} ლარი. ახალი ბალანსი: {self.__balance} ლარი")
#             else:
#                 print(f"შეცდომა: არასაკმარისი თანხა! ბალანსი: {self.__balance} ლარი")
#         else:
#             print("შეცდომა: თანხა უნდა იყოს დადებითი!")

#     def check_balance(self):
#         return self.__balance

#     def get_account_number(self):
#         return self.__account_number

#     def change_owner(self, new_owner):
#         self._owner = new_owner
#         print(f"ანგარიშის მფლობელი შეიცვალა: {new_owner}")

#     @classmethod
#     def get_total_accounts(cls):
#         return cls.__total_accounts

#     @staticmethod
#     def validate_amount(amount):
#         return amount > 0

#     def __str__(self):
#         return f"Account: {self.__account_number} | Owner: {self._owner}"

# print("=" * 45)
# print(f"კეთილი იყოს თქვენი მობრძანება {BankAccount.bank_name}-ში!")
# print("=" * 45)

# print("\n--- ანგარიშების შექმნა ---")
# acc1 = BankAccount("გიორგი მამულაშვილი", 500)
# acc2 = BankAccount("ნინო ბერიძე", 1000)
# acc3 = BankAccount("დავით კობახიძე", -100)

# print(acc1)
# print(acc2)
# print(acc3)

# print(f"\nსულ ანგარიში: {BankAccount.get_total_accounts()}")

# print("\n--- თანხის ჩარიცხვა ---")
# acc1.deposit(200)
# acc1.deposit(-50)

# print("\n--- თანხის გამოტანა ---")
# acc2.withdraw(300)
# acc2.withdraw(5000)
# acc2.withdraw(-100)

# print("\n--- ბალანსის შემოწმება ---")
# print(f"{acc1} | ბალანსი: {acc1.check_balance()} ლარი")
# print(f"{acc2} | ბალანსი: {acc2.check_balance()} ლარი")

# print("\n--- მფობელის შეცვლა ---")
# acc3.change_owner("მარიამ გელაშვილი")
# print(acc3)

# print("\n--- ვალიდაცია ---")
# print(f"validate_amount(500): {BankAccount.validate_amount(500)}")
# print(f"validate_amount(-10): {BankAccount.validate_amount(-10)}")
# print(f"validate_amount(0):   {BankAccount.validate_amount(0)}")


# ===========================დავალება 2 ====================================

class MethodNameValidator(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value) and not key.startswith("_"):
                raise ValueError(f"კლასში '{name}' მეთოდის სახელი '{key}' არასწორია! მეთოდი უნდა იწყებოდეს '_'-ით.")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MethodNameValidator):
    def _my_method(self):
        pass

print("MyClass შეიქმნა წარმატებით")

try:
    class WrongClass(metaclass=MethodNameValidator):
        def bad_method(self):
            pass
except ValueError as e:
    print("შეცდომა:", e)