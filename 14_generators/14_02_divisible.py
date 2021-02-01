"""
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

"""

gen = (x for x in range(10000))
for i in gen:
    if i % 1111 == 0:
        print(i)
