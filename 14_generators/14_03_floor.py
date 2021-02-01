"""
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

"""
gen = (x for x in range(10000))
for i in gen:
    if i % 1111 == 0:
        print(i // 1111)