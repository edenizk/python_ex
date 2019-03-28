#question 1 Quiz: Extract First Names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

#question 2 Quiz: Multiples of Three
multiples_3 = [3*i for i in range(1,21)] # write your list comprehension here
print(multiples_3)


#question 3 Quiz: Filter Names by Scores
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, value in scores.items() if value>65 ] # write your list comprehension here
print(passed)
