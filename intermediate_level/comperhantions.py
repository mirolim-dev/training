# list comperhantions


numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []

# for x in numbs:
#     my_list.append(x)
# print(my_list)


# print([x for x in numbs])

# # I'm gonna print list of the 'x**x' in numbs --------------

# for x in numbs:
#     my_list.append(x**x)
# print(my_list)

# print([x**x for x in numbs])

# # with map and lambda functions
# print(list(map(lambda x: x**x, numbs)))

# filter even numbs ------------------------

# normal codes
# for x in numbs:
#     if x %2 == 0:
#         my_list.append(x)
# print(my_list)

# by list comperhantion
# my_list = [x for x in numbs if x%2 == 0]
# print(my_list)

# by filter + lambda function
# my_list = list(filter(lambda x: x%2 == 0, numbs))
# print(my_list)
# -----------------------------------------------------
# symbols = 'abcd'
# nums = [1, 2, 3, 4]

# my_list = []
# for x in symbols:
#     for n in nums:
#         my_list.append((x, n))
# print(my_list)

# by list comperhantions
# my_list = [(x, num) for x in symbols for num in nums]
# print(my_list)

# dict and set comperhantions---------------------------------
chars = 'abcdefghij'
# my_dict = {}
# for char, numb in zip(chars, numbs):
#     my_dict[char] = numb
# print(my_dict)

my_dict = {char: numb for char, numb in zip(chars, numbs)}
