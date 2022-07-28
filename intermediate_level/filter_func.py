def square_of_numb(numb):
    return numb**2


def is_even(numb):
    return numb%2==0


my_list = [1, 5, 3, 2, 4, 6, 7, 0, 10]

print("even numers: ", list(filter(is_even, my_list)))

print('Square of even numbs inside of my_list: \n', \
    list(map(square_of_numb, filter(is_even, my_list))))