# Write code for algorithm 4 below.Write a function that calculates the value of 'a' to the power of 'b'.

# For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.

#  Iterative Approach
# This method uses a loop to multiply a by itself b times.
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Example usage
print(power(2, 4))  # Output: 16
def power(a, b):
    # Base case
    if b == 0:
        return 1
    # Recursive case
    return a * power(a, b - 1)

# Example usage
print(power(2, 4))  # Output: 16
