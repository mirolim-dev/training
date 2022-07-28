# advantage of map function
# short lines of code

# lets compare it

from hashlib import new


my_list = [1, 3, 5, 2, 6, 4, 8, 10, 9, 7]

new_list = []
def func(numb):
    return numb**numb

for i in my_list:
    new_list.append(func(i))
print(new_list)
    
    
# now i'm gonna use from map function
print(list(map(func, my_list)))


# now i'm gonna solve this with list comperhantions
print([func(x) for x in my_list])


# solve this problem dor only even numbs of my_list
print([func(x) for x in my_list if x%2==0])