import random
def game():
    i=0
    n=int(input('n='))
    
    rand=random.randrange(1,n)
    while True:
        a=int(input('guess the num: '))
        if a==rand:
            print('number was:',rand ,'\nYou guess correctly in ',i,'times')
            break;
        elif a>rand:
            print('guess again it was too high')
            i+=1
        elif a<rand:
            print('too low guess again')
            i+=1
def main():

    game()

main()
