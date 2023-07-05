input = """8577245547
1654333653
5365633785
1333243226
4272385165
5688328432
3175634254
6775142227
6152721415
2678227325"""
exdata = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

def printCoordsPretty(coord):
    for x in coord:
        for y in x:
            if y.power < 10:
                print(" {} ".format(y), end = '')
            else:
                print("{} ".format(y), end = '')
        print("")
    print("")
class octopus:
    def __init__(self) -> None:
        self.power = 0
        self.adjacent = []
    def __str__(self):
        return str(self.power)
    def setInitPower(self, val):
        self.power = val
    def addOctopus(self, octopus):
        self.adjacent.append(octopus)
    def increasePower(self):
        global flashes
        if self.power <= 9: # could be if other octopi flashed
            self.power += 1
            if self.power > 9:
                flashes += 1
                for octopus in self.adjacent:
                    octopus.increasePower()
    def resetPower(self):
        if self.power > 9:
            self.power = 0
#hint: maybe all need to be increased by 1 first and than process this and flash others...

flashes = 0
octopiarray = [[None] * 10 for x in range(10)]
for x in range(len(octopiarray)):
    for y in range(len(octopiarray[0])):
        octopiarray[x][y] = octopus()

for x in range(len(octopiarray)):
    for y in range(len(octopiarray[0])):
        if x > 0: #x -1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x-1][y])
        if y > 0: #y -1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x][y-1])
        if x > 0 and y > 0: #x-1|y-1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x-1][y-1])
        if x < len(octopiarray)-1: #x+1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x+1][y])
        if y < len(octopiarray[0])-1: #y+1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x][y+1])
        if x < len(octopiarray)-1 and y < len(octopiarray[0])-1: #x+1|y+1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x+1][y+1])
        if x > 0 and y < len(octopiarray)-1: #x-1|y+1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x-1][y+1])
        if y > 0 and x < len(octopiarray)-1: #x+1|y-1 is adjacent
            octopiarray[x][y].addOctopus(octopiarray[x+1][y-1])
printCoordsPretty(octopiarray)
"""for x in range(10):
    octopiarray[0][0].setInitPower(9)
    printCoordsPretty(octopiarray)
    octopiarray[0][0].increasePower()
    printCoordsPretty(octopiarray)
print(flashes)
"""
x = 0
y = 0
for line in input.splitlines():
    y = 0
    for num in line:
        octopiarray[x][y].setInitPower(int(num))
        y += 1
    x += 1
printCoordsPretty(octopiarray)
print("init done")

steps = 100
for step in range(steps):
    for line in octopiarray:
        for elem in line:
            elem.increasePower()
    for line in octopiarray:
        for elem in line:
            elem.resetPower()
    print("step ", step)
    printCoordsPretty(octopiarray)
print("flashes: ", flashes)