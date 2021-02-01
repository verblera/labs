"""
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

"""

gen = (x*3 for x in range(1, 8))
print(gen)
for i in gen:
    print(i)