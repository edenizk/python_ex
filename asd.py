name = 'John'
people = [
     {
          'name': 'John',
          'description': 'a fun guy'
     },
     {
          'name': 'Anne',
          'description': 'a childhood friend'
     }
]

if name.lower() in [person['name'].lower() for person in people]:
     output_variable = hello_phrase(person)
else:
     output_variable = unknown_phrase(person)

def hello_phrase(person):
     return "Welcome back, {}! You're {}.".format(person['name'], person['description'])

def unknown_phrase(person):
     return "Sorry, {}. I don't know you!".format(person['name'])
