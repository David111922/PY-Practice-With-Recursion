# Write code for algorithm 5 below. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.
# Here's a function to calculate the value of a raised to the power of b:
def power(a, b):
    return a ** b

# Example usage
print(power(2, 4))  # Output: 16

# . Palindrome Check Function
# Here's a function to check whether a string is a palindrome:

# python
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))     # Output: True
print(is_palindrome("hello"))     # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
-