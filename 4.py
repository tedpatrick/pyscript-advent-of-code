from pyodide.http import open_url

data = open_url("4.txt")
total = 0
for line in data:
    line = line.strip()
    pair = line.split(",")
    a = pair[0].split("-")
    b = pair[1].split("-")
    if int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]):
        total += 1
    elif int(b[0]) <= int(a[0]) and int(b[1]) >= int(a[1]):
        total += 1

print(f"Part 1 total: {total}")

data = open_url("4.txt")
total = 0
for line in data:
    line = line.strip()
    pair = line.split(",")
    a = pair[0].split("-")
    b = pair[1].split("-")
    a_set = set(range(int(a[0]), int(a[1]) + 1))
    b_set = set(range(int(b[0]), int(b[1]) + 1))
    c_list = list(a_set.intersection(b_set))
    if len(c_list) > 0:
        total += 1

print(f"Part 2 total: {total}")
