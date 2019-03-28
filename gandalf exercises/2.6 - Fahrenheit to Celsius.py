choose = input("choose F/C: ")
temp = int(input("choose temperature for {}: ".format(choose)))
if choose == "F" or choose=="f" :
    
    print("for {0} F, C is {1}".format(temp,((temp-32)*5)/9))

elif choose == "C" or choose == "c":
    print("for {0} C, F is {1}".format(temp,((temp*9)/5)+32))

else:
    print("Wrong Input")
