def aritmetic_mean(my_num):
    result = 0

    for x in my_num:
        result += int(x)

    return result/len(my_num)

def main():
    my_num = input("please write your numbers (seperate with space):\n ").split(" ")
    print(aritmetic_mean(my_num))

main()
