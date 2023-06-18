from collections import OrderedDict

d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
new_d = OrderedDict(sorted(d.items()))
new_d

for key in new_d:
    key, new_d[key]
for key in reversed(new_d):
    print(key, new_d[key])