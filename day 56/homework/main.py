hero = {
    "name": "Archer",
    "level": 5,
    "items": ["Sword", "Shield"]
}

hero["items"].append("Bow")
hero["level"] += 1

print("გმირის მონაცემები:")
print(hero)
print("-" * 30)



user_profile = {
    "name": "Giorgi",
    "surname": "Beridze",
    "age": 16,
    "hobby": "Gaming"
}

user_profile["name"] = "Nika"
del user_profile["age"]

print("მომხმარებლის მონაცემები (მხოლოდ values):")
for value in user_profile.values():
    print(value)
print("-" * 30)


cart = {
    "Keyboard": 120,
    "Mouse": 60,
    "Headphones": 150
}

total = 0
for price in cart.values():
    total += price

print("კალათის ჯამური ფასი:", total)
print("-" * 30)



countries = {
    "Georgia": "Tbilisi",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid"
}

country = input("შეიყვანე ქვეყნის სახელი: ")

if country in countries:
    print("დედაქალაქია:", countries[country])
else:
    print("ინფორმაცია ვერ მოიძებნა")

print("-" * 30)


students = {
    "Ana": [9, 8, 10],
    "Luka": [7, 9, 8]
}

students["Nino"] = [10, 10, 9]

print("სტუდენტების საშუალო ნიშნები:")
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, "- საშუალო ნიშანი:", average)
