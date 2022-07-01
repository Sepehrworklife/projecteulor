# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


# Returns True if n is prime, False otherwise
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Returns the nth prime number
def nth_prime(n):
    i = 1
    while True:
        i += 1
        if is_prime(i):
            n -= 1
            if n == 0:
                return i


# Check if answer is correct
print(f"The 10001st prime number is {nth_prime(10001)}")
