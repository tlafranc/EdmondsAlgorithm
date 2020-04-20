import random

def prodTestFile():
    file = open("sparseGraph.txt", "w")
    n = 25000
    connectedSet = [0]
    disconnectedSet = set(range(1, n))
    file.write(str(n) + ' ' + str(n - 1) + '\n')
    while len(disconnectedSet) != 0:
        u = random.choice(connectedSet)
        v = random.choice(tuple(disconnectedSet))
        connectedSet.append(v)
        disconnectedSet.remove(v)
        file.write(str(u) + " " + str(v) + " " + str(random.randint(10, 1000)) + "\n")


prodTestFile()