import random

def prodTestFile(num):
    file = open("t" + str(num) + ".txt", "w")
    file.write("1\n")
    n = 10000
    m = 250000
    file.write(str(n) + '\n' + str(m) + '\n')
    for i in range(m):
        file.write(str(random.randint(0, n - 1)) + " " + str(random.randint(0, n - 1)) + " " + str(random.randint(10, 1000)) + "\n")


prodTestFile(14)