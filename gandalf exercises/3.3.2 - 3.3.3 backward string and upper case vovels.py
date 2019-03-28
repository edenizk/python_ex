def backward(text):
    return text[::-1]

def capital_vovel(text):
    capital = ''
    for texts in text:
        if texts in ('a', 'e', 'i', 'o', 'u'):
           capital += texts.capitalize()
        else:
            capital += texts

    return capital
def main():

    text = list(input("write your text:\n"))
    print(backward(''.join(text)), capital_vovel(text))
main()
