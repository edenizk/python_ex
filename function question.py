#question 1 Quiz: Population Density Function

# write your function here
def population_density(population, land_area):
    return population/land_area

    #question 2 Quiz: readable_timedelta
def readable_timedelta(days):
    print("{} week(s) and {} day(s).".format(int(days/7),days%7))
def main():
    #question 1 Quiz: Population Density Function
    # test cases for your function
    test1 = population_density(10, 1)
    expected_result1 = 10
    print("expected result: {}, actual result: {}".format(expected_result1, test1))

    test2 = population_density(864816, 121.4)
    expected_result2 = 7123.6902801
    print("expected result: {}, actual result: {}".format(expected_result2, test2))


    #question 2 Quiz: readable_timedelta
    
    readable_timedelta(10)

main()
