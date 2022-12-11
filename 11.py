#from pyodide.http import open_url
import math

with open("11.txt", encoding = 'utf-8') as f:
    lines = f.readlines()
    mcount=[]
    monkeys = []
    for line in lines:
        line = line.strip()
        print(line)
        if line.startswith("Monkey "):
            current = int(line.split("Monkey ")[1].split(":")[0])
            #print(current)
            monkeys.append({})
            mcount.append(0)

        elif line.startswith("Starting items: "):
            monkeys[current]["items"] =list(map(int,line.split("Starting items: ")[1].split(", ")))
        
        elif line.startswith("Operation: new = old "):
            monkeys[current]["operation"] = line.split("Operation: new = old ")[1].split(" ")
            if monkeys[current]["operation"][1] == "old":
                monkeys[current]["operation"][0] = "**"
            else:
                monkeys[current]["operation"][1] = int(monkeys[current]["operation"][1])
        
        elif line.startswith("Test: divisible by "):
            monkeys[current]["divby"] = int(line.split("Test: divisible by ")[1])

        elif line.startswith("If true: throw to monkey "):
            monkeys[current]["mtrue"] = int(line.split("If true: throw to monkey ")[1])
    
        elif line.startswith("If false: throw to monkey "):
            monkeys[current]["mfalse"] = int(line.split("If false: throw to monkey ")[1])
    
    for round in range(1,10001):
        m=0
        print(round, mcount)
        for monkey in monkeys:
            #print(f"Monkey {m}:")
            for i in range(0,len( monkey.get("items"))):
                item = monkey.get("items").pop(0)
                #print(item)
                worry = item
                operation = monkey.get("operation")
                #print(f"    Monkey inspects an item with a worry level of {item}.{m}:")
                divby = monkey.get("divby")
                mtrue = monkey.get("mtrue")
                mfalse = monkey.get("mfalse")
                if operation[0] == "+":
                    worry = worry + operation[1]
                    #print(f"        Worry level increases by {int(operation[1])} to {worry}.")
                
                elif operation[0] == "**":
                    worry = worry * worry
                    #print(f"        Worry level is multiplied by itself to {worry}.")
                elif operation[0] == "*":
                    worry = worry * operation[1]
                    #print(f"        Worry level is multiplied by {int(operation[1])} to {worry}.")
                
                worry = math.floor(worry/3)
                #worry = math.floor(worry)
                #print(f"        Monkey gets bored with item. Worry level is divided by 3 to {worry}.")


                
                if worry%divby == 0:
                    #print(f"        Current worry level is divisible by {divby}.")
                    monkeys[mtrue].get("items").append(worry)
                    
                    #print(f"        Item with worry level {worry} is thrown to monkey {mtrue}.")
                    
                else:
                    #print(f"        Current worry level is not divisible by {divby}.")
                    monkeys[mfalse].get("items").append(worry)
                    #print(f"        Item with worry level {worry} is thrown to monkey {mfalse}.")
                mcount[m] = mcount[m]+1
            m+=1

        #print(f"round: {round}")
        #for monkey in monkeys:
        #   print( monkey.get("items") )
    mcount.sort()
    mcount.reverse()
    print(mcount)
    print(mcount[0]*mcount[1])