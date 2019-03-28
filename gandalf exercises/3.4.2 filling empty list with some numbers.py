def one_to_ten(max_num):
    my_list = []
    for i in range(1, max_num+1):
        my_list.append(i)
    return my_list

def two_two_two(max_num):
    my_list = []
    for i in range(0, max_num+1, 2):
        my_list.append(i)
    return my_list

def power_of(max_num):
    my_list = []
    for i in range(1, max_num+1):
        my_list.append(i**2)
    return my_list

def zeros(max_num):
    my_list = []
    for i in range(0, max_num):
        my_list.append(0)
    return my_list

def one_zeros(max_num):
    my_list = []
    for i in range(0, max_num):
        my_list.append(i%2)
    return my_list

def one_zeros(max_num):
    my_list = []
    new_num = max_num // 2
    for i in range(0, new_num):
        my_list.append(i)
    return my_list*2

def main():
    
    a = one_to_ten(10)
    b = two_two_two(20)
    c = power_of(10)
    d = zeros(10)
    e = one_zeros(10)
    f = one_zeros(10)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)


main()
