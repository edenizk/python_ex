import random
def counter(my_list):
    tmp = 0
    result = 0
    result_num = 0
    number = 0
    for i in my_list:
       # print("tmp b",tmp)

        if i == tmp:
            result +=1
           # print(i," i= ",tmp )

        else:
           # print("result", result," result num ",result_num)
            if result > result_num:
                result_num = result 
                number = tmp
                #print("tmp",tmp," result num ",result_num)
            else:
                result = 1
                tmp = i
            
    print("{} most fruquent {} time".format(number, result_num ))
                
def random_list(n, k):
    result = []
    for y in range(n):
        rand = random.randrange(1,k)
        result.append(rand)
    return result
    
def main():


    counter([3, 4, 6, 2, 2, 1, 4, 4, 5, 1, 1, 1, 6])
    counter(random_list(1000000,7))
main()
