import glob
# PIV　data sorting


def getIndexedElementFromFile(filename, indexOfElement=4):
    file = open(filename)
    linesOfFile = file.readlines()
    file.close()
    targets = []
    for line in linesOfFile:
        target = line.split()[indexOfElement]
        targets.append(target)
    return targets


files = glob.glob("*_PIV3_disp.txt")
result = []
for file in files:
    elements = getIndexedElementFromFile(file, 3)
    result.append(sum(int(e) for e in elements))

    print(result)


newTxt = open('result.txt', "w+")
for e in result:
    newTxt.write(str(e)+'\n')
newTxt.close()
