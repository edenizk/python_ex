def zipdic(sentence,a,b,c,d,e):
    print(sentence['what'][a%2],sentence['who'][b%3],
              sentence['how'][c%2],sentence['do'][d%2],
                  sentence['where'][e%3])




def main():
    
    sentence=dict(zip(['what','who','how','do','where'],[
                      ['What what','Stray'],
                      ['Doctor','Cat','Dog'],
                      ['ludly','happily'],
                      ['cry','laugh'],
                      ['in the street','in the home','under the dome']]))
    
    a = int(input("a= "))

    b = int(input("b= "))

    c = int(input("c= "))

    d = int(input("d= "))

    e = int(input("e= "))



    zipdic(sentence,a,b,c,d,e)

main()
