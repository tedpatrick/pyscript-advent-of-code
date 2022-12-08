from pyodide.http import open_url
import json

path = []
filesize = 0
dirs = {}
with open_url("7.txt") as f:
    lines = f.readlines()
    for line in lines:
        # command
        if line[0] == "$":
            if line[0:7] == "$ cd ..":
                path.pop()
            elif line[0:5] == "$ cd ":
                d = line[5:].strip()
                path.append(d)
                dirs["_".join(path)] = 0
            elif line[0:4] == "$ ls":
                filesize = 0
        # output
        else:
            if line[0:4] == "dir ":
                continue
            else:
                parts = line.split(" ")
                name = parts[1].strip()
                filesize += int(parts[0])
                dirs["_".join(path)] = filesize

tdir = {}
for d in dirs:
    tdir[d] = dirs[d]
    for e in dirs:
        if d == e:
            continue
        elif e.startswith(d):
            tdir[d] += dirs[e]


total = 0
for d in tdir:
    if tdir[d] < 100000:
        total += tdir[d]

print(f"Part 1 total: {total}")


free = 70000000 - tdir["/"]
need = 30000000 - free
# print(need,free)

candidates = []
for d in tdir:
    if tdir[d] > need:
        candidates.append(tdir[d])
candidates.sort()
print(f"Part 2 total: {candidates[0]}")
