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

print( elves[len(elves)-1]) # print last elfs calories carries

print(elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3])