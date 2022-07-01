#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def main(elderNumber: int) -> int:
    sum = 0
    for i in range(1, elderNumber):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum



# Test output with problem description if they match
print(f"The answer is: {main(10)}")
# Test the function with the given input
print(f"The answer is: {main(1000)}")
