"""
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

"""
try:
    with open('integers.txt', 'r') as text:
        content_list = text.read().split()
        i = 0
        for item in content_list:
            try:
                item = int(item)
            except ValueError:
                pass
            else:
                number_1 = int(input('Type in a number: '))
                print(number_1 * int(content_list[i]))
                break
            finally:
                i += 1
except FileNotFoundError:
    print('check the file name')
except ValueError:
    print('cannot do calculation with these values')

