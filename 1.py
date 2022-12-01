from pyodide.http import open_url

data = open_url("1.txt")

elves = []

elf = 0
for line in data:
    if line == "\n":
        elves.append(elf)
        elf = 0
    else:
        elf = int(line.strip()) + elf
elves.sort()
elves_len = len(elves)

# last elfs calories carried
print( f"Top elf calories: {elves[elves_len-1]}" )

# sum of last 3 elves
print( f"Top 3 elfs calories: {elves[elves_len-1] + elves[elves_len-2] + elves[elves_len-3]}")