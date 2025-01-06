# What is *args (Non-Keyword Arguments) ? explain with function's example.
def function(*args):
    for i in args:
        print(i)


function("123456", "2", "24")
def table(*n):
    for j in n:
        for i in range(1,11):
            print(f"{j}*{i}={j*i}")
table(42,5)