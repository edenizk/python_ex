while True:

    try:
        x = int(input('Enter a number: '))
        break
    except KeyboardInterrupt:
        print("BYE BYE")
        break
    except:
        print('That\'s not a valid number!')

    finally:
        print('\nAttempted Input\n')
