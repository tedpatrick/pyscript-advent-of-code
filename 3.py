import math
from pyodide.http import open_url

data = open_url("3.txt")

# char priority lookup
priority = { "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52,}

total = 0

for line in data:
    mid = int(len(line)/2)
    a = set()
    b = set()
    count=0
    for char in line:
        if count >= mid:
            b.add(char)
        else:
            a.add(char)
        count+=1
    letter = list(a.intersection(b))[0]
    total+=priority[letter]

print( f"Part 1 total: {total}" )
total = 0
out=[]
data = open_url("3.txt")
group = []
for line in data:
    line = line.strip()
    a = set()
    for char in line:
        a.add(char)
    group.append(a)
    if len(group) == 3:
        out.append( list( group[0].intersection( group[1], group[2] ) )[0] )
        group=[]

for letter in out:
    total+=priority[letter]
print( f"Part 2 total: {total}" )
