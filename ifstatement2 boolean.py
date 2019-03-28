def main():
    unsubscribed = False
    location = "USA"
    if (not unsubscribed) and (location == "USA" or location == "CAN"):
        print("send email")
        
    is_cold = True
    # Good example
    if is_cold:
    print("The weather is cold!")
    # Good example
    if not is_cold:
    print("The weather is cold!")

    errors = 3
    if errors:#this expression will run cuz different than 0 is true
        print("You have {} errors to fix!".format(errors))
    else:
        print("No errors to fix!")

    points = 174  # use this input when submitting your answer

    # set prize to default value of None
    prize = None

    # use the value of points to assign prize to the correct prize name
    if points <= 50:
        prize = "wooden rabbit"
    elif 151 <= points <= 180:
        prize = "wafer-thin mint"
    elif points >= 181:
        prize = "penguin"

    # use the truth value of prize to assign result to the correct message
    if prize:
        result = "Congratulations! You won a {}!".format(prize)
    else:
        result = "Oh dear, no prize this time."

    print(result)
    
    
main()
