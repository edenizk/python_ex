def main():
# question 1
    names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
    usernames = []



    # write your for loop here

    for name in names:
        usernames.append(name.lower().replace(" ", "_"))

    print(usernames)

#question 2

    usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

    # write your for loop here
    for i in range(len(usernames)):
        usernames[i] = (usernames[i].lower().replace(" ", "_"))



    print(usernames)
    
#question 3
    tokens = ['<greeting>', 'Hello World!', '</greeting>']
    count = 0

    # write your for loop here
    for token in tokens:
        if '<' in token:
            count += 1
        

    print(count)


#question 4
    items = ['first string', 'second string']
    html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                         # the characters that are after it in html_str are on the next line

    # write your code here
    for item in items:
        html_str += "<li>" + item + "</li>\n"
    html_str += "</ul>\n"
    print(html_str)
    
main()
