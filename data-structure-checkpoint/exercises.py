# Q1
result = 1
for x in [2, 3, 6]:
    result *= x
print(result)  # 36

# Q2
print(sorted([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)], key=lambda t: t[-1]))

# Q3
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
merged = dict(d1)
for k, v in d2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)

# Q4
n = int(input("n: ") or 8)
squares = {}
for i in range(1, n + 1):
    squares[i] = i * i
print(squares)

# Q5
items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(items, key=lambda t: float(t[1]), reverse=True))

# Q6
s = {0, 1, 2, 3, 4}
for x in s:
    print(x)
s.add(5)
s.remove(0)
s.discard(99)  # no error if missing
print(s)

assert result == 36
assert merged == {'a': 400, 'b': 400, 'd': 400, 'c': 300}
