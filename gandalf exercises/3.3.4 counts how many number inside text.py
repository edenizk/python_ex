def file_len():
    with open('linecounter.txt') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#def file_write(input_text):
  #  with open('linecounter.txt', 'w') as f:
      #  f.write(input_text)

def main():

    #text = input("write your text:\n")
    #file_write(text)

    print(file_len())
          
main()
