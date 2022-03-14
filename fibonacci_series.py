# Fn = Fn-1 + Fn-2
def fibonacci(n):
    if n < 0:
        print("incorrect")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

list2 = []
for i in range(0,10):
    list2.append(fibonacci(i))

print(f"analis fibonacci = {list2}")
result = fibonacci(9)