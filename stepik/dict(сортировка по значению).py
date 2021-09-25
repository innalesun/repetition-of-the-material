d = {'n': 250, 'b': 100, 'a': 500, 'c': 400, 'm': 50}

key_sorted = sorted(d.keys(), key=(lambda x: d[x]))
print(key_sorted)

d_sorted_value = {i: d[i] for i in key_sorted}
print(d_sorted_value)

