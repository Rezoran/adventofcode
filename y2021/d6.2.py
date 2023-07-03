input = "1,4,1,1,1,1,1,1,1,4,3,1,1,3,5,1,5,3,2,1,1,2,3,1,1,5,3,1,5,1,1,2,1,2,1,1,3,1,5,1,1,1,3,1,1,1,1,1,1,4,5,3,1,1,1,1,1,1,2,1,1,1,1,4,4,4,1,1,1,1,5,1,2,4,1,1,4,1,2,1,1,1,2,1,5,1,1,1,3,4,1,1,1,3,2,1,1,1,4,1,1,1,5,1,1,4,1,1,2,1,4,1,1,1,3,1,1,1,1,1,3,1,3,1,1,2,1,4,1,1,1,1,3,1,1,1,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,5,1,1,1,2,2,1,1,3,5,1,1,1,1,3,1,3,3,1,1,1,1,3,5,2,1,1,1,1,5,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,5,1,4,3,3,1,3,4,1,1,1,1,1,1,1,1,1,1,4,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,1,4,4,1,1,1,1,1,1,1,5,1,1,2,5,1,1,4,1,3,1,1"

#class lanternfish:
#    def __init__(self, num: int) -> None:
#        self.days = num
"""
lanternfishes = []
for num in input.split(","):
    lanternfishes.append((int(num)))
print("len: ",len(lanternfishes))
#print(lanternfishes)

days = 256
for day in range(days):
    newdayarray = []
    for fish in range(len(lanternfishes)):
        if lanternfishes[fish] == 0:
            newdayarray.append((8))
            lanternfishes[fish] = 6
        else: 
            lanternfishes[fish] -= 1
    lanternfishes += newdayarray
    print("day {}: total fishes: {}, new fishes: {}".format(day, len(lanternfishes), len(newdayarray)))
"""
cntarray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for num in input.split(","):
    cntarray[int(num)] += 1
print("len: ",sum(cntarray))
print(cntarray)

days = 256
for day in range(days):
    newdayfishes = 0
    #print(cntarray)
    for index in range(len(cntarray)):
        if index == 0:
            newdayfishes = cntarray[0] # index is obv 0
        else:
            cntarray[index-1] = cntarray[index]
            cntarray[index] = 0
    
    cntarray[6] += newdayfishes
    cntarray[8] += newdayfishes
    #print(cntarray)
    print("day {}: total fishes: {}, new fishes: {}".format(day, sum(cntarray), newdayfishes))
