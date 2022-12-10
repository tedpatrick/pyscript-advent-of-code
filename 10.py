from pyodide.http import open_url


def ps(s):
    print("".join(s[0:40]))
    print("".join(s[40:80]))
    print("".join(s[80:120]))
    print("".join(s[120:160]))
    print("".join(s[160:200]))
    print("".join(s[200:240]))


with open_url("10.txt") as f:
    lines = f.readlines()
    commands = []
    for line in lines:
        line = line.strip()
        if line.startswith("noop"):
            commands.append([0])
            # print("> noop")
        elif line.startswith("addx"):
            v = int(line.split("addx ")[1])
            # print(f"> addx {v}")
            commands.append([1, None])
            commands.append([1, v])

    # CPU
    x = 1
    cycle = 1
    phase = 1
    strength = 0
    for command in commands:
        if cycle == 20:
            print(f"{cycle} signal: {x*cycle}")
            strength += x * cycle
            phase = 0
        if cycle > 20 and phase == 40 and cycle < 221:
            print(f"{cycle} signal: {x*cycle}")
            strength += x * cycle
            phase = 0
        # print(f"{cycle} x: {x}")
        if command[0] == 0:
            1  # print(f"{cycle} noop")
        elif command[0] == 1:
            # print(f"{cycle} addx {command[1]}")
            if command[1] != None:
                x = x + command[1]
        cycle += 1
        phase += 1
    print(f"{cycle} x: {x}")
    print(f"{cycle} x: {strength}")

    print("==============================")

    # SCREEN
    s = []
    for i in range(0, 240):
        s.append("0")

    # CPU
    x = 1
    cycle = 1
    row = 0
    for command in commands:
        # print(f"{cycle} x: {x}")
        if command[0] == 0:
            1  # print(f"{cycle} noop")
        elif command[0] == 1:
            # print(f"{cycle} addx {command[1]}")
            if command[1] != None:
                x = x + command[1]

        if (
            cycle == (row * 40) + (x - 1)
            or cycle == (row * 40) + x
            or cycle == (row * 40) + (x + 1)
        ):
            s[cycle] = "#"
        cycle += 1
        if cycle % 40 == 0:
            row += 1
    print(f"{cycle} x: {x}")
    ps(s)
