from pyodide.http import open_url

with open_url("6.txt") as f:
    line = f.read()
    for i in range(0, len(line)):
        if len(list(set(line[i : i + 4]))) == 4:
            print(i + 4)
            break

with open_url("6.txt") as f:
    line = f.read()
    for i in range(0, len(line)):
        if len(list(set(line[i : i + 14]))) == 14:
            print(i + 14)
            break
