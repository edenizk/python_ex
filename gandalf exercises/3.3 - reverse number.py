def reverse(dec):
    return str(dec)[::-1]


def main():

    num=int(input("num= "))

    print("{} reversed = {}".format(num,reverse(num)))


main()
