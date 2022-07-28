# lambda function

def plus(num1, num2):
    return num1+num2

func2 = lambda x, y: x+y
# lambda is an easy(short) way to create simple functions
print(f"def funk: {plus(2, 3)}\nlambda func: {func2(2,3)}")


# using map, filter, lambda functions together
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: x**2, filter(lambda x: x%2==0, my_list))))