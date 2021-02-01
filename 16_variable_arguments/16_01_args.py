"""
Write a script with a function that demonstrates the use of *args.

"""
import random
def schedule(*args):
    with open('schedule.txt', 'w') as promises:
        promises.write('I promise to work out following days...')
        words = ['for sure', 'honestly', 'definitely', 'no doubt', 'seriously']
        for day in args:
            promises.write(f'\n{day}, {random.choice(words)}')

schedule('09.02', '11.02', '14.02', '17.02', '21.02', '01.03', '02.03')