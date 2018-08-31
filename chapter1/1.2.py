# Unpacking elements from iterables of arbitrary length

"""
Problem 
You need to unpack N elements from an iterable, but the iterable may 
be longer than N elements, causing a “too many values to unpack” exception.

Solution

Python "star expressions" can be used to address this problem
"""


def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print("Print name:")
print(name)
print("Print email:")
print(email)
# phone_numbers will always print a list, regardless of how many, even none
print("Print phone_numbers:")
print(phone_numbers)

print("Starred variables can also be the first one in a list")
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("Should print first 7 elements:")
print(trailing)
print("Should print last element, 3")
print(current)

# Extended iterable unpacking is tailor-made for unpacking iterables of unknown
# or arbitrary length

print("Can be useful when combined with certain kinds of string processesing")  
line = 'nobody:*:-2:-2:UnprivilegedUser:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

print("Sometimes you might want to unpack values and throw them away. You can't\
	 specify a bare * when unpacking but you can use a throwaway variable name \
	 like _ or ign (ignored)")
record = ('ACME', 50, 123.45, (12,18,2012))
name, *_, (*_, year) = record
print(name)
print(year)

# Split lists into head and tail components
print("List of items 1,10,,7,4,5,9")
items = [1, 10, 7, 4, 5, 9]
print("Split into head and tail")
head, *tail = items
print("Head:")
print(head)
print("Tail(s)")
print(tail)

# Splitting in order to carry out some kind of clever recursive algorithm
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head

print("Sum of items")
print(sum(items))





