def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        result = Fibonacci(n-1) + Fibonacci(n-2)
        return result
    
i = 2
list= []
while Fibonacci(i) < 4000000:
    result = Fibonacci(i)
    if result%2 == 0:
        list.append(result)
    i +=3
print(sum(list))