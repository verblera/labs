'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def age_count(years):
    # takes years, calls a function to return minutes and returns seconds
    seconds = age_count_2(years)*60
    return seconds


def age_count_2(yars):
    # takes years and returns minutes
    minutes = yars * 365 * 24
    return minutes


def init(name):
    age = int(input(f'What\'s your age, {name}? '))
    print(f'So, you lived for {age} years, or {age_count(age)} seconds')
    yes_or_no = input('Pretty old, huh? yes/no?')
    i = 0
    while yes_or_no.lower() != 'yes':
        print(f'Don\'t agree? Let me remind you, you\'re {age_count(age)} seconds old')
        yes_or_no = input('Pretty old, huh? yes/no?')
        i += 1
        if i > 4:
            print('Hard to persuade you, huh')
            break
    if yes_or_no.lower() == 'yes':
        print(f'Bye, {name}, my old friend')


user_name = input('Hello! What\'s your name?')
init(user_name)
