import random

def prodTestFile(num):
    file = open("randTestFile" + str(num) + ".txt", "w")
    n = 2000
    m = 100000
    file.write(str(n) + ' ' + str(m) + '\n')
    for i in range(m):
        file.write(str(random.randint(0, n - 1)) + " " + str(random.randint(0, n - 1)) + " " + str(random.randint(10, 1000)) + "\n")


prodTestFile(3)