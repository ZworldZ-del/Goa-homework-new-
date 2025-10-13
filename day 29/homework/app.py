# 1)
lion = [4 , 5 , 5 , 4 , 5]
lion_count = lion.count(5)
lion_index = lion.index(4)

print(lion_count)
print(lion_index)

# ---------------------------------

lion = ["dino" , "lino" , "baino" , "lion" , "dino"]
lion_count = lion.count("daino")
lion_index = lion.index("lino")

print(lion_count)
print(lion_index)

# ---------------------------------

def lion():
    return "მე ვარ ლომი ნიკოლოზი" 
lion()

print(lion())

# ---------------------------------

def lion4():
    numbers = []
    for i in range(22):  
        if i % 2 != 0:  
            numbers.append(i)  
    print(numbers)  
print(lion4())

# ---------------------------------------------

def lion5():
    სწორი_პასვორდი= "lomivarlomi!"
    password = input("შეიყვანე პაროლი")
    while password != სწორი_პასვორდი:
        print("პაროლი არასწორია")
        password = input("შეიყვანე პაროლი")
    print("სწორია!")

# ---------------------------------------------

fruits = ["apple", "banana", "apple", "orange", "apple", "grape"]
print("ვაშლი გვხვდება:", fruits.count("apple"), "ჯერ")

# ---------------------------------------------

def multiply(a, b):
    return a * b

print(multiply(5, 3))

# ---------------------------------------------

animals = ["Lion", "Tiger", "Frog", "Panda", "Deer", "Elephant", "Fox"]
print(animals[1])
print(animals[2])
print(animals[-5])
print(animals[-6])


