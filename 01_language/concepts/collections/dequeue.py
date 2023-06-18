# As a general rule, if we need fast appends or fast pops, use a deque. If we need fast random access, use a list.

from collections import deque
import string

d = deque(string.ascii_lowercase)
for letter in d:
    letter

d.append("bork")
print(d)


d.appendleft("test")
print(d)


d.rotate(1)
print(d)