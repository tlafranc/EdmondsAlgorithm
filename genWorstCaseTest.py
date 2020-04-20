def prodTestFile():
    n = 3000
    file = open("worstCase" + str(n) + ".txt", "w")
    
    m = (n - 3) * 2 + 3
    file.write(str(n) + ' ' + str(m) + '\n')
    file.write(str(1) + " " + str(2) + " " + str(1) + '\n')

    cost = 2
    for curVertex in range(2, n - 1):
        file.write(str(curVertex) + " " + str(curVertex - 1) + " " + str(cost) + "\n")
        cost += 1
        file.write(str(curVertex) + " " + str(curVertex + 1) + " " + str(cost) + "\n")
        cost += 1

    file.write(str(n - 1) + " " + str(n - 2) + " " + str(cost) + '\n')
    cost += 1
    file.write(str(0) + " " + str(n - 1) + " " + str(cost) + '\n')


prodTestFile()