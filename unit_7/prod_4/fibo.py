def fibo_odd(n: int) -> list:
    if n <= 1:
        return [0]
    fibo = [0, 1]
    for _ in range(2, 3 * n):
        fibo.append(fibo[-1] + fibo[-2])
    return [x for x in fibo if x % 2 == 0]


fibo = fibo_odd(50)
print(len(fibo))
print(fibo)
