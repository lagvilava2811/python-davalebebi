import math

print("=== პირველი დავალება ===")
print("მართკუთხა სამკუთხედის გამოთვლა")


a = int(input("შეიყვანეთ a კათეტი: "))
b = int(input("შეიყვანეთ b კათეტი: "))

c = math.sqrt(a*a + b*b) 
s = (a * b) / 2           

print("ჰიპოთენუზა =", c)
print("ფართობი =", s)

print("\n=== მეორე დავალება ===")
print("წამების გადაყვანა")

sec = int(input("შეიყვანეთ წამები: "))

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60

print(sec, "წამი =", hours, "სთ", minutes, "წთ", seconds, "წმ")