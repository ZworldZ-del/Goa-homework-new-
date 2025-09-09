print("=== 2) რიცხვები 1-დან 100-მდე ===")
i = 1
while i <= 100:   
    print(i, end=" ")
    i += 1
print("ended")
 

print("=== 3) 5 ელემენტიანი list და მე-3, მე-5 მნიშვნელობები ===")
numbers = [10, 20, 30, 40, 50]
print("list:", numbers)
print("მე-3 ელემენტი:", numbers[2])  # goon 2
print("მე-5 ელემენტი:", numbers[4])  # goon 4
print()


print("=== 4) შეტყობინება ===")
print("ვინც საკლასო ვერ გააკეთეთ — გააკეთეთ სახლში და ვინც ვერ გაიგო, შეატყობინეთ ლიდერს <3")
print()


print("=== 5) 7 ელემენტიანი list და 20-ზე მეტი მნიშვნელობები ===")
number = [5, 18, 25, 33, 12, 7, 45]
print("list:", number)
print("20-ზე მეტი ელემენტები:")
dino = 0
while dino < len(number):
    if number[dino] > 20:
        print(number[dino], end=" ")
    dino += 1
print("\n")

# Recsource მაგალითი
print("=== Recsource მაგალითი ===")
    #   1         2        3       4        5
fruits = ["Apple", "Samsung", "Xiaomi", "lomi", "Ak-47", "RPG-7"]


item3 = fruits[2]
print("მესამე ელემენტი (dino 2):", item3)


number = int(input("მიუთითე ინდექსი (0-დან 5-მდე): "))
if 2 <= number < len(fruits):
    print("შენ აირჩიე:", fruits[number])
else:
    print("incorrect!")
