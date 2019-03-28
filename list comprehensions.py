square = [x**2 if x%2==0 else x+3 for x in range (9)]
print(square)



#capitalized_cities = []
#for city in cities:
    #capitalized_cities.append(city.title())
capitalized_cities = [city.title() for city in cities]
