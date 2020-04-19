import random

def prodTestFile(num):
    file = open("randTestFile" + str(num) + ".txt", "w")
    n = 5000
    m = 50000
    file.write(str(n) + '\n' + str(m) + '\n')
    for i in range(m):
        file.write(str(random.randint(0, n - 1)) + " " + str(random.randint(0, n - 1)) + " " + str(random.randint(10, 1000)) + "\n")


prodTestFile(1)