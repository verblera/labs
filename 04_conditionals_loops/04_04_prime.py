'''
Print out every prime number between 1 and 100.

'''
for x in range(1,101):
    if (x % 2 != 0) or (x == 2):
        if (x % 3 !=0) or (x == 3):
            if (x % 5 != 0) or (x == 5):
                if (x % 7 != 0) or (x == 7):
                    print(x)