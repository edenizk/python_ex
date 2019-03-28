def main():
    random_things = [1, 3.4, 'a string', True]
    print (random_things[-1],"\n")

    month = ["January", "February", "March", "April",
                        "May", "June", "July", "August",
                            "September", "October", "November", "December"]
    hello = "Hello there"
    q3 = month[6:9]
    first_half = month[:6]
    second_half = month[6:]
    
    print("- 6-9 months = {0} \n-first half = {1} \n-second half = {2} \n- 6-9 string and list = {3}{4} \n-len string and list = {5}{6} "
          .format(q3, first_half, second_half, len(hello), len(month), hello[6:9], month[6:9]))

    print("is there '-her' inside hello there =  " ,'her' in hello)

    print("how many 'd' letter inside month names = ".count('s'))
    
    print("May is not a month = ", 'May' not in month)


    #mutating

    my_list = [1, 2, 3, 4, 5]
    my_list[0] = 'one'
    print(my_list)
main()
