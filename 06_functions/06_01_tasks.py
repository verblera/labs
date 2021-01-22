'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean


def four_or_seven(num):
    if num % 4 == 0:
        return True
    elif num % 7 == 0:
        return True
    else:
        return False


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def four_and_seven(numb):
    if numb % 4 == 0:
        if numb % 7 == 0:
            return True
        else:
            return False
    else:
        return False
# take in a number from the user between 1 and 1,000,000,000


def user_input():
    string = input('Please, type in a number between 1 and 1,000,000,000: ')
    return string
# call your functions, passing in the user input as the arguments, and set their output equal to new variables 


def calling():
    x = int(user_input())
    first_boolean = four_or_seven(x)
    second_boolean = four_and_seven(x)
    return first_boolean, second_boolean
# print your new variables to display the results

answer = calling()
print(f'The typed number is divisible \n by 4 or 7: {answer[0]} \n by both 4 and 7: {answer[1]}')
