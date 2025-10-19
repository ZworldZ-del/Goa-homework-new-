def check_even_or_odd():
    number = int(input("შეიყვანე რიცხვი: "))
    if number % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")


def check_positive_or_negative():
    number = int(input("შეიყვანე რიცხვი: "))
    if number > 0:
        print("რიცხვი დადებითია")
    elif number < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულია")


def compare_numbers():
    a = int(input("შეიყვანე პირველი რიცხვი: "))
    b = int(input("შეიყვანე მეორე რიცხვი: "))
    if a > b:
        print(f"{a} უფრო დიდია ვიდრე {b}")
    elif a < b:
        print(f"{b} უფრო დიდია ვიდრე {a}")
    else:
        print("ორივე რიცხვი ტოლია")


def grade_student():
    score = int(input("შეიყვანე სტუდენტის ქულა (0-100): "))
    if 90 <= score <= 100:
        print("შენი ნიშანია: A")
    elif 80 <= score <= 89:
        print("შენი ნიშანია: B")
    elif 70 <= score <= 79:
        print("შენი ნიშანია: C")
    elif 60 <= score <= 69:
        print("შენი ნიშანია: D")
    elif 0 <= score <= 59:
        print("შენი ნიშანია: F")
    else:
        print("არასწორი ქულა! უნდა იყოს 0-დან 100-მდე.")


def check_temperature():
    temp = float(input("შეიყვანე ტემპერატურა ცელსიუსში: "))
    if temp < 0:
        print("Today is very cold! Wear warm clothes")
    elif 0 <= temp <= 30:
        print("Today is a really nice weather")
    else:
        print("Today is very hot! Drink plenty of water")


check_even_or_odd()
check_positive_or_negative()
compare_numbers()
grade_student()
check_temperature()
