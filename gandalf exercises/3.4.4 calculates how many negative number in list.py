def negative_num(num_list):
    result = 0
    num_list = list(map(int, num_list))
    print(num_list)
    for x in num_list:
        if x < 0:
            result +=1

    return result

def main():
    my_num = input("please write your numbers (seperate with space):\n ").split(" ")

    print(negative_num(my_num))

main()
