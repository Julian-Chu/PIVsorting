import glob
# PIV　data sorting

print('Hello world')
files = glob.glob("*.txt")
print(files)


filename = files[0]
print(filename)
with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())
        print(len(line))


def getIndexedElementFromFile(filename, indexOfElement=4):
    file = open(filename)
    linesOfFile = file.readlines()
    targets = []
    for line in linesOfFile:
        target = line.split()[indexOfElement]
        print(target)
        targets.append(target)
    return targets


result = getIndexedElementFromFile(files[0], 3)
print(result)
print(sum(int(e) for e in result))

newTxt = open('new.txt', "w+")
