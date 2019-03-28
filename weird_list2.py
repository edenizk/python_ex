def main():

    num = [12,32,4,3,123]
    names = ["ergin", "deniz", "kosecioglu", "deniz"]
    print("max element = ",max(num))
    print("min elemen = ", min(num))
    print("small to big =", sorted(num))
    print("big to small = ", sorted(num, reverse=True))
    print("-".join(names))# - seperates each element
    num.append(35)
    print("last update = ", num)
    print("'{0}' removed".format(names.pop(0)))
    
main()
