# Improved with memoization
# You can declar cache outside function with no values
# Must use base case number < 2
def fibonacci_memo(number, cache = {0: 0, 1: 1}):
    # check if number is in cache if true return it
    if number in cache:
        return cache[number]
    
    # Add computed value to cache dictionary
    cache[number] = fibonacci_memo(number - 1, cache) + fibonacci_memo(number - 2, cache)    
    return cache[number]

    
def fibonacci(number):
    # 0, 1 (base) , 1, 2, 3, 5, 8
    
    if number < 2:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)
    
def print_desc_numbers(n):
    if n == 0:
        return
    
    print(n)
    print_desc_numbers(n - 1)   # return address
    print(n)
    
    
def print_asc_numbers(n):
    if n == 0:
        return
    
    print_desc_numbers(n - 1)
    print(n)

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

def sum_of_digits(n):
    if n < 10:
        return n
    
    return (n % 10) + sum_of_digits(n // 10)

def prod_of_digits(n):
    if n < 10:
        return n
    
    return (n % 10 ) * prod_of_digits(n // 10)


def reverse_digits(number, result=0):
    if number == 0:
        return
    
    last_digit = number % 10
    result = result * 10 + last_digit
    reverse_digits(number // 10)
    
    return result
    

if __name__ == "__main__":
    print(reverse_digits(123))
    