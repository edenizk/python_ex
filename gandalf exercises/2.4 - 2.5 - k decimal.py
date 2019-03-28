try:
    n = int(input("n= "))
    k = int(input("k= "))
except ValueError:
    print("try again\n")

print ("{0}-th binary digit for {1} is: {2}".format(k,n,abs(n)%(10**k)))


print(k , "position digit = ", (abs(n) // 10 ** k) % 10)
print(k , "position digit = ", (abs(n) // 10 ** k) % 2)
print ("length of the decimal number = ", len(str(n)))
print ("length of the binary number = ", len(str(bin(abs(n))))-2, )
