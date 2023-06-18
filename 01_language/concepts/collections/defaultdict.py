from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)


# list
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)


# lambda
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'

print (animal['Nick'])

print (animal)


# ➜ python-a2z (main) ✗ python 01_language/concepts/collections/defaultdict.py
# defaultdict(<class 'int'>, {'The': 1, 'red': 1, 'for': 2, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'food': 1})
# defaultdict(<class 'list'>, {1234: [100.23, 75.0, 35.67], 345: [10.45, 222.66], 678: [300.25]})
# Monkey
# defaultdict(<function <lambda> at 0x104cd20c0>, {'Sam': 'Tiger', 'Nick': 'Monkey'})