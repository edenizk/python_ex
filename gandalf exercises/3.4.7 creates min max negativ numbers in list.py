
    
def negative_num(num_list):
    result = 0
    num_list = list(map(int, num_list))
    print(num_list)
    for x in num_list:
        if x < 0:
            result +=1

    return result

def min_max_negativ(my_list):
    my_list.sort()
    new_list = []
    new_list.append(my_list[0])
    new_list.append(my_list[-1])
    new_list.append(negative_num(my_list))
    return new_list
def main():
    print(min_max_negativ([2,3,5,1,4,-2,-5]))

main()
