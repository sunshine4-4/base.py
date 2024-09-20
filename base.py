# 0 1 1 2 3 5
def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


print(fib(4))


# with open('fib_num.txt', 'w') as file:
#     file.write(str(fib(5)))
#     file.close()
