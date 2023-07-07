from __future__ import annotations

input = """QR-da
QR-end
QR-al
start-op
zh-iw
zh-start
da-PF
op-bj
iw-QR
end-HR
bj-PF
da-LY
op-PF
bj-iw
end-da
bj-zh
HR-iw
zh-op
zh-PF
HR-bj
start-PF
HR-da
QR-bj"""

# expected 10
exdata = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

#expected 19
exdata2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

#expected 226
exdata3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""



class cave:
    def __init__(self, char: str) -> None:
        self.letter = char
        self.adjacent = []
        self.upper = True if char.upper() == char else False
    def addAdjacent(self, input: cave):
        self.adjacent.append(input)
    def isUpper(self) -> bool:
        return self.upper

def recursionWorker(cavedict, startingpoint, path):
    global waycounter
    #print("worker: {}, path: {}".format(startingpoint, path))
    if startingpoint == "end":
        path += "end"
        print("Found: ", path)
        waycounter += 1
        return 
    for elem in cavedict[startingpoint].adjacent:
        if elem.letter != "start":
            if (elem.upper != True and elem.letter not in path) or (elem.upper == True):
                recursionWorker(cavedict, elem.letter, path+cavedict[startingpoint].letter+"-")


caves = {}
for line in input.splitlines():
    a, b = line.split("-")
    if a not in caves:
        caves[a] = cave(a)
    if b not in caves:
        caves[b] = cave(b)
    caves[a].addAdjacent(caves[b])
    caves[b].addAdjacent(caves[a])

for elem in caves:
    print("cave {}, adjacent: {}".format(caves[elem].letter, list(x.letter for x in caves[elem].adjacent)))

# find ways now
waycounter = 0
try:
    recursionWorker(caves, "start", "")
except Exception as e:
    print(e)
#for x in range(40):
#    workingcaves = caves.copy()
print("found ways: ", waycounter)