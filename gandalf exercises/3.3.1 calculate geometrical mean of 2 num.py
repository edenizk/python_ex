def geomean(my_num):
    result = 1

    for x in my_num:
        result *= int(x)

    return result**(1/len(my_num))

def main():
    my_num = input("please write your numbers (seperate with space):\n ").split(" ")
    print(geomean(my_num))

main()
