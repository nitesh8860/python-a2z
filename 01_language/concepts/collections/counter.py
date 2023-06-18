from collections import Counter

print(Counter("superfluous"))


counter = Counter("superfluous")
print(counter["u"])
print(list(counter.elements()))
print(counter.most_common(2))

counter_two = Counter("super")
print(counter.subtract(counter_two))


print(counter)

# ➜ python-a2z (main) ✗ python 01_language/concepts/collections/counter.py
# Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})
# 3
# ['s', 's', 'u', 'u', 'u', 'p', 'e', 'r', 'f', 'l', 'o']
# [('u', 3), ('s', 2)]
# None
# Counter({'u': 2, 's': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 0, 'e': 0, 'r': 0})