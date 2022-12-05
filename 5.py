from pyodide.http import open_url

A=[
    list(),
    list("BGSC"),
    list("TMWHJNVG"),
    list("MQS"),
    list("BSLTWNM"),
    list("JZFTVGWP"),
    list("CTBGQHS"),
    list("TJPBW"),
    list("GDCZFTQM"),
    list("NSHBPF")
]

data = open_url("5.txt")
for line in data:
    c = list(map(int,line.strip().split('move ')[1].replace(" from ", " to ").split(" to ")))
    for n in range(0,c[0]):
        A[c[2]].append(A[c[1]].pop())
out=""
for d in range(1,10):
    out+=A[d].pop()

print(f"Part 1 total: {out}")

A=[
    list(),
    list("BGSC"),
    list("TMWHJNVG"),
    list("MQS"),
    list("BSLTWNM"),
    list("JZFTVGWP"),
    list("CTBGQHS"),
    list("TJPBW"),
    list("GDCZFTQM"),
    list("NSHBPF")
]

data = open_url("5.txt")
for line in data:
    c = list(map(int,line.strip().split('move ')[1].replace(" from ", " to ").split(" to ")))
    m=[]
    for n in range(0,c[0]):
        m.append(A[c[1]].pop())
    m.reverse()
    A[c[2]] += m
out=""
for d in range(1,10):
    out+=A[d].pop()

print(f"Part 2 total: {out}")

