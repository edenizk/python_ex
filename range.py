def main():
    #range(start, stop, step)

    print("0-4 = ", list(range(4))) #4-1 last elemet
    print("2-6 = ", list(range(2, 6)))#6-1 last element
    print("1-10, 2 step = ", list(range(1, 10, 2)))#10-1 last element

    countries = ['u.s.a', 'turkey', 'poland']
    for index in range(len(countries)):
        countries[index] = countries[index].title()
        
    print("-".join(countries))

    for i in range(3):
        print("Hello")

    print(list(range(0,-5)))
main()
