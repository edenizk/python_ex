def main():

    elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
    print("print the value mapped to 'helium'",elements["helium"])  # print the value mapped to "helium"
    elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
    print("elements = ",elements)

    print("is there carbon = ", "carbon" in elements)
    print("get dilithum = ",elements.get("dilithium"))
    print("get hydrogen = ",elements.get('hydrogen'))
    print("there is no dilithium ? ", elements.get("dilithium") is None)

    n = elements.get("dilithium")
    print("there is no dilithium ? ", n is None)
    print("there is no dilithium ? ", n is not None)
    print("type of elements = ", type(elements))

    animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
    print(sorted(animals))
    elements2 = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
    print("hydrogen weight = ",elements2['hydrogen']['weight'])
    
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print(a == b)
    print(a is b)
    print(a == c)
    print(a is c)

main()
