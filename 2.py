from pyodide.http import open_url

data = open_url("2.txt")

LOSS = 0
TIE = 3
WIN = 6
ROCK = 1
PAPER = 2
SIZZORS = 3

# A X = Rock = 1
# B Y = Paper = 2
# C Z = Sizzors = 3

total = 0

for line in data:
    if line == "A X\n":
        total = total + TIE + ROCK

    elif line == "A Y\n":
        total = total + WIN + PAPER

    elif line == "A Z\n":
        total = total + LOSS + SIZZORS

    elif line == "B X\n":
        total = total + LOSS + ROCK

    elif line == "B Y\n":
        total = total + TIE + PAPER

    elif line == "B Z\n":
        total = total + WIN + SIZZORS

    elif line == "C X\n":
        total = total + WIN + ROCK

    elif line == "C Y\n":
        total = total + LOSS + PAPER

    elif line == "C Z\n":
        total = total + TIE + SIZZORS

    else:
        raise Exception("Invalid input")

print(f"Part 1 total: {total}")

# X = LOSS
# Y = TIE
# Z = WIN
# A = Rock = 1
# B = Paper = 2
# C = Sizzors = 3

data = open_url("2.txt")

total = 0

for line in data:
    if line == "A X\n":
        total = total + LOSS + SIZZORS

    elif line == "A Y\n":
        total = total + TIE + ROCK

    elif line == "A Z\n":
        total = total + WIN + PAPER

    elif line == "B X\n":
        total = total + LOSS + ROCK

    elif line == "B Y\n":
        total = total + TIE + PAPER

    elif line == "B Z\n":
        total = total + WIN + SIZZORS

    elif line == "C X\n":
        total = total + LOSS + PAPER

    elif line == "C Y\n":
        total = total + TIE + SIZZORS

    elif line == "C Z\n":
        total = total + WIN + ROCK

    else:
        raise Exception("Invalid input")

print(f"Part 2 total: {total}")
