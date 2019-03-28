import random

def guess(min_num,max_num):

     return random.randrange(min_num,max_num)

def uncorrect(userin):
    while True:
        userin = input("yes or no ? ")
        if userin in "yes" or userin in "YES" or userin in "Y" or userin in "y" :
            return userin
        elif userin in "no" or userin in "NO" or userin in "N" or userin in "n":
            return userin
        else:
            print("try again")
    

def main():
    min_num = int(input("choose min and max\n min: "))
    max_num = int(input("max: "))
    
    while min_num < max_num:
        guessed = guess(min_num, (max_num + 1))
        print( "{} is your guess".format( guessed ) )
        userin = input("yes or no ? ")
        if userin in "yes" or userin in "YES" or userin in "Y" or userin in "y" :
            print("I knew I can find it, I'm so smart :D")
            break
        elif userin in "no" or userin in "NO" or userin in "N" or userin in "n":
            userin = input("should I go higher or lower?[H/L]\n ")
           
            if "high" in userin or "h" in userin or "HIGH" in userin or "H" in userin:
                print("high then its! ")
                min_num = guessed + 1
            else:
                print("ok I'll lower my guess ")
                max_num = guessed + 1
        
              

main()
