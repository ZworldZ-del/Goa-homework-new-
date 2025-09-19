a = "lomi ki ara lekvi kide!"
print(len(a))
new_a = ""
for i in range( len(a) ) :
    new_a = [a]
print(new_a)
# ______________________________________

a = "lom ki ara lekvi kide!"
print(len(a))
new_a = ""
for i in range(len(a)):
     if a[i] != " ":
        new_a += a[i]
print(new_a)
