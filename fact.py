def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

numbers_to_compute = [5, 7, 3, 10]

factorial_results = [factorial(num) for num in numbers_to_compute]

print(','.join(map(str, factorial_results)))
