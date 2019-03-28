def main():

    maria_string = "Maria loves {} and {}"
    print(maria_string.format("math","statistics"))

    animal = "dog"
    action = "bite"
    print("Does your {} {}?".format(animal, action))

    print("Mohammed has {} balloons".format(27))
    
    first_word = 'Hello'
    second_word = 'There'
    
    print(first_word + second_word)

    #HelloThere

    print(first_word + ' ' + second_word)

    #hello there
    print(first_word * 5)

    #HelloHelloHelloHelloHello
    
    print(len(first_word))
    #5
main()
