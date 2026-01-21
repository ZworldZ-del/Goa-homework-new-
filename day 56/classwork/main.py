_story = {
    "Story-maker":"nikolozi",
    "weapon":"AK47",
    "characther":"Zgnerdemona",
    "Rashveba":"tvaletidan amodis",
    "rogor-klavs-adamians":"azgnerebs.",
    "rato-Sheveba-amas":["HE_IS", "A VILLAN."]
}

story = {
    "Story-maker":"nikolozi",
    "weapon":"DESERT EGALE DIGLI",
    "characther":"THE HERO",
    "Rashveba":"klavs zgnerdemonebs",
    "rogor-exmareba-adamians":"wmindavs adamianebs zgneridan",
    "RA MOWONS MAGASHI":["HE IS A HERO"]
}

car = {
    "name":"nikolozis manqana",
    "age":"newest",
    "brand":"bmw m6 f06",
    "engine":"twin turbo 4.4"


}
car["love"] = "wsp my guy"
story["love"] = "what is love"
_story["love"] = "Baby Don't You LEave me"

for i in car:
    print(i)

for i in story:
    print(i)

for i in _story:
    print(i)
for value in car:
    print(value)

for value in story:
    print(value)

for value in _story:
    print(value)


item1 = _story["characther"]
item2 = _story["Rashveba"]
item3 = _story["rogor-klavs-adamians"]
item4 = _story["Story-maker"]
item5 = _story["weapon"]
item6 = _story["rato-Sheveba-amas"]

item7 = story["characther"]
item8 = story["Rashveba"]
item9 = story["RA MOWONS MAGASHI"]
item10 = story["Story-maker"]
item11 = story["weapon"]
item12 = story["RA MOWONS MAGASHI"]

story_name = story["name"]
for i in story:
        print(story[i])

print(item1)
print(item2)
print(item3)
print(item4)
print(item5)
print(item6)

print(item7)
print(item8)
print(item9)
print(item10)
print(item11)
print(item12)

print(car[value])
print(story[value])
print(_story[value])

print(car[i])
print(story[i])
print(_story[i])