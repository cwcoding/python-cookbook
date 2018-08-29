# Simple Exercises
# Data Structures and Algorithms

# 1.1

"""
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. 
"""

p = (4, 5)
x, y = p
print(x)
print(y)

# unpacking a list
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, prices, date = data
print(name)
print(shares)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)

# Unpacking works with any object that happens to be iterable, not just tuples or lists
s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)

# When unpacking, you may sometimes want to discard certain values.
# No special syntax for this, but you can use a throwaway variable name for it
_, shares, price, _ = data
print(shares)
print(price)