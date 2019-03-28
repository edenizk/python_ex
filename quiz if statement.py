def main():
    points = 174  # use this input to make your submission

    # write your if statement here
    result = "Congratulations! You won a "
    if points >=1 and 50 >= points :
        result += "[wooden rabbit]"

    elif points >= 51 and 150 >= points :
        result = "Oh dear, no prize this time."

    elif points >=151 and 180>= points:
        result += "[wafer-thin mint]"
            
    elif points >=181 and 200>= points:
        result += "[penguin]"
    print(result)

    answer = 35#provide answer
    guess = 30#provide guess
    if answer > guess: #provide conditional
        result = "Oops!  Your guess was too low."
    elif guess < answer:#provide conditional
        result = "Oops!  Your guess was too high."
    elif guess==answer: #provide conditional
        result = "Nice!  Your guess matched the answer!"

    print(result)

    # Depending on where an individual is from we need to tax them 
    # appropriately.  The states of CA, MN, and 
    # NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
    # Use this information to take the amount of a purchase and 
    # the corresponding state to assure that they are taxed by the right
    # amount.
    # '''
    state = "CA"#Either CA, MN, or NY
    purchase_amount = 13#amount of purchase

    if state is "CA":#provide conditional for checking state is CA
        tax_amount = .075
        total_cost = purchase_amount*(1+tax_amount)
        result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

    elif state is "MN":#provide conditional for checking state is MN
        tax_amount = .095
        total_cost = purchase_amount*(1+tax_amount)
        result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

    elif state is "NY":#provide conditional for checking state is NY
        tax_amount = .089
        total_cost = purchase_amount*(1+tax_amount)
        result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

    print(result)
main()
