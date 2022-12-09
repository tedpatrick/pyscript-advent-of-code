from pyodide.http import open_url

trail = set()
with open_url("9.txt") as f:
    lines = f.readlines()
    h = [0, 0]
    t = [0, 0]
    trail.add(f"{t[0]},{t[1]}")
    for line in lines:
        v = line.split(" ")
        com = v[0]
        dist = int(v[1])
        for s in range(0, dist):
            if com == "R":
                h[0] += 1
                if h[0] > t[0] and h[0] - t[0] > 1:
                    t[0] += 1
                    if h[1] != t[1]:  # diag
                        t[1] = h[1]
            elif com == "L":
                h[0] -= 1
                if h[0] < t[0] and t[0] - h[0] > 1:
                    t[0] -= 1
                    if h[1] != t[1]:  # diag
                        t[1] = h[1]
            elif com == "U":
                h[1] += 1
                if h[1] > t[1] and h[1] - t[1] > 1:
                    t[1] += 1
                    if h[0] != t[0]:  # diag
                        t[0] = h[0]
            elif com == "D":
                h[1] -= 1
                if h[1] < t[1] and t[1] - h[1] > 1:
                    t[1] -= 1
                    if h[0] != t[0]:  # diag
                        t[0] = h[0]
            trail.add(f"{t[0]},{t[1]}")

print(len(list(trail)))


def move_right(h):
    h[0][0] = h[0][0] + 1
    i = 0
    for item in h:
        if i < 10:
            if h[i][0] > h[i + 1][0] and (h[i][0] - h[i + 1][0]) > 1:
                h[i + 1][0] = h[i + 1][0] + 1
                if h[i][1] != h[i + 1][1]:  # diag
                    h[i + 1][1] = h[i][1]
        i += 1


def move_left(h):
    h[0][0] = h[0][0] - 1
    i = 0
    for item in h:
        if i < 10:
            if h[i][0] < h[i + 1][0] and (h[i + 1][0] - h[i][0]) > 1:
                h[i + 1][0] = h[i + 1][0] - 1
                if h[i][1] != h[i + 1][1]:  # diag
                    h[i + 1][1] = h[i][1]
        i += 1


def move_up(h):
    h[0][1] = h[0][1] + 1
    i = 0
    for item in h:
        if i < 10:
            if h[i][1] > h[i + 1][1] and (h[i][1] - h[i + 1][1]) > 1:
                h[i + 1][1] = h[i + 1][1] + 1
                if h[i][0] != h[i + 1][0]:  # diag
                    h[i + 1][0] = h[i][0]
        i += 1


def move_down(h):
    h[0][1] = h[0][1] - 1
    i = 0
    for item in h:
        if i < 10:
            if h[i][1] < h[i + 1][1] and (h[i + 1][1] - h[i][1]) > 1:
                h[i + 1][1] = h[i + 1][1] - 1
                if h[i][0] != h[i + 1][0]:  # diag
                    h[i + 1][0] = h[i][0]
        i += 1


trail = set()
with open_url("9.txt") as f:
    lines = f.readlines()
    h = []
    for i in range(0, 11):
        h.append([10000, 10000])
    trail.add(f"{h[10][0]},{h[10][1]}")
    for line in lines:
        v = line.split(" ")
        com = v[0]
        dist = int(v[1])
        for s in range(0, dist):
            if com == "R":
                move_right(h)
            elif com == "L":
                move_left(h)
            elif com == "U":
                move_up(h)
            elif com == "D":
                move_down(h)
            trail.add(f"{h[10][0]},{h[10][1]}")

print(len(list(trail)))
