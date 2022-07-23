import random

genf = open("gendata.txt", "w")
for i in range(0,1000):
    value = random.random()
    genf.write(str(value)+"\n")

genf.close
