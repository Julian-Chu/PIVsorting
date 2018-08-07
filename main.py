import glob
import os
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
files.sort(key=os.path.getmtime)

print('Files found: ' + str(files))
result = []
for file in files:
    elements = getIndexedElementFromFile(file, 3)
    total = sum(float(e) for e in elements)
    result.append(total)

    print(file + ":" + str(total))


newTxt = open('result.txt', "w+")
for e in result:
    newTxt.write(str(e)+'\n')
newTxt.close()

input("Press Enter to continue...")
