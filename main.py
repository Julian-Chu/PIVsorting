import glob
import os


def getIndexedElementFromFile(filename, indexOfElement=4):
    file = open(filename)
    linesOfFile = file.readlines()
    file.close()
    targets = []
    for line in linesOfFile:
        target = line.split()[indexOfElement]
        targets.append(target)
    return targets


def getAvgExcludeZero(nums):
    target = [float(num) for num in nums if num != '0']
    print(target)
    if len(target) == 0:
        avg = 0
    else:
        avg = sum(target) / len(target)
    return avg


def getVarExcludeZero(nums):
    target = [float(num) for num in nums if num != '0']
    print(target)
    if len(target) == 0:
        var = 0
    else:
        avg = sum(target) / len(target)
        var = sum((x-avg)**2 for x in target) / len(target)
    return var


files = glob.glob("*_PIV3_disp.txt")
files.sort(key=os.path.getmtime)

print('Files found: ' + str(files))
result = []
for file in files:
    elements = getIndexedElementFromFile(file, 4)
    total = sum(float(e) for e in elements)
    avg = getAvgExcludeZero(elements)
    var = getVarExcludeZero(elements)

    result.append([total, avg, var])

    print(file + ":" + str(total) + " " + str(avg) +
          " " + str(var) + " ")


with open('result.txt', "w+") as newTxt:
    newTxt.write("sum avg variance \n")
    for e in result:
        newTxt.write(str(e[0])+' '+str(e[1]) + ' ' + str(e[2])+'\n')

input("Press Enter to continue...")
