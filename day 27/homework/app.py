parents = ["Deda", "Mama"]
parents.append("Me")
print(parents)


numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is Odd")


words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "hat", "ice", "juice"]
for word in words[1::2]:
    print(word)


word = "GOA"
for i, char in enumerate(word, start=1):
    print(f"{char}-{i}")


lst = [1, 2, 3, 4, 5]
print(lst[::-1])
