def binary(dec):
    base = ""
    while dec > 0:
        base += str(dec % 2)
        dec = dec // 2
       
    return base[::-1]

def base8(dec):
    base = ""
    while dec > 0:
        base += str(dec % 8)
        dec = dec // 8
       
    return base[::-1]

def base16(dec):
    base = ""
    while dec > 0:
        base += str(dec % 16)
        dec = dec // 16
       
    return base[::-1]


def main():
    
    choose = input("1-binary \n2-base8 \n3-base16 \nchoose: ")
    num = int(input("input a number: "))
    if choose in "1" or choose in "binary":
        print("binary number for {} is = {}".format(num,binary(num)))
    elif choose in "2" or choose in "base8":
        print("base 8 number for {} is = {}".format(num,base8(num)))
    elif choose in "3" or choose in "base16":
        print("base 16 number for {} is = {}".format(num,base16(num)))
    

main()
