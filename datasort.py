data = open("gendata.txt","r")
sorted = open("sorted.txt", "w")

awe = []
for line in data:
    awe.append(float(line))
    awe.sort()

for i in awe:
    sorted.write(str(i)+"\n")

sorted.close()
data.close()
