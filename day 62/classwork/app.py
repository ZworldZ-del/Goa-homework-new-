person = {
    "name" : "guy",
    "Crimes":"Zero",
    "Last-name" : "Walking",
    "Nickname" : "Walker Guy",
    "List" : ["Person" , "is" , "a", "good" , "guy"]
}
new_dict = [
    {"name": "a"},
    {"name": "g"},
    {"name": "b"},
    {"name": "e"},
    {"name": "r"}
]



for key in person:
    print(person[key])

print(person["List"])

print(new_dict)


nums = []

for i in range(1, 101):
    nums.append(i)

result = []

for z in nums:
    if z % 10 == 0:
        result.append(z)

print(result)
