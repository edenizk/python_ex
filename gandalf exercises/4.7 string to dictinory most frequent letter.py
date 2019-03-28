import collections

def distribution(x):

    counted = {}
    for i,v in enumerate(x):
        if v in counted:
            counted[v] += 1
        else:
            counted[v] = 1

    return counted

def main():

    L = list(input("string = "))
    print(collections.Counter(L).most_common(1)[0])

    print("distribution= ", distribution(L))


main()
