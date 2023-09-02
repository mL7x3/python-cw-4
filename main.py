def my_name():
    print("my name is mubarak")
my_name()

def my_meal(food, drink):
    print(f"i like to eat {food} and while drinking {drink}")
food = str(input("what your best food : "))
drink = str(input("what your best drink :" ))
my_meal(food, drink)


def cube(number):
    return number ** 3
cube(1)
def by_there(number1):
    if number1 % 3 == 0:
        cube(number1)
        return cube(number1)
    else:
        return False 
print(by_there(3))

