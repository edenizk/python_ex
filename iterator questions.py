#question 1 Quiz: Implement my_enumerate

def my_enumerate(iterable, start=0):
    count = start
    for i in iterable:
        yield count, i
        count +=1
#question 2 Quiz: Chunker
        
def chunker(iterable, size):
  
    for i in range(0, len(iterable), size):
            yield iterable[i:i + size]

def main():
    
    #question 1 Quiz: Implement my_enumerate
    lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

    for i, lesson in my_enumerate(lessons, 1):
        print("Lesson {}: {}".format(i, lesson))

    #question 2 Quiz: Chunker
    for chunk in chunker(range(25), 4):
        print(list(chunk))
main()
