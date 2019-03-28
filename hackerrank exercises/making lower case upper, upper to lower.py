s = "Deniz"
a = ""
for i in s:
    if i.islower():
        a+=i.capitalize()
        continue
    elif i.istitle():
        a += i.lower()
    else:
            a += i
print(a)
