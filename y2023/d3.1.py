from d3data import input_test, input_prod

input = input_prod

data = []
for line in input.splitlines():
    row = []
    for digit in line:
        row.append(digit)
    data.append(row)
xMax = len(data)
yMax = len(data[0])
print("x: ", len(data))
print("y: ", len(data[0]))

try:
    result = 0
    for x in range(xMax):
        curnum = ""
        for y in range(yMax):
            cur = data[x][y]
            if cur.isdigit():
                curnum += data[x][y]
            else:
                if curnum == "":
                    continue
            if (y < (yMax-1)) and data[x][y+1].isdigit():
                continue
            print("number found: ",curnum)
            numValid = False
            # begin and end 
            begin = (y-(len(curnum)-1)) if ((y-(len(curnum)-1)) <= 0) else (y-(len(curnum)-1)-1)
            end = y if (y >= (yMax-1)) else y+1
            # current line (left and right)
            print("checking current line, begin {} end {}".format(begin, end))
            for i in range(begin,end+1):
                if not data[x][i].isdigit() and data[x][i] != ".":
                    print("valid element ({}) at x: {} y: {}".format(data[x][i], x, i))
                    numValid = True
                    break
            # above
            if x > 0 and not numValid:
                print("checking line above")
                for i in range(begin,end+1):
                    if not data[x-1][i].isdigit() and data[x-1][i] != ".":
                        print("valid element ({}) at x: {} y: {}".format(data[x-1][i], x-1, i))
                        numValid = True
                        break
            # below
            if (x < (xMax-1)) and not numValid:
                print("checking line below")
                for i in range(begin,end+1):
                    if not data[x+1][i].isdigit() and data[x+1][i] != ".":
                        print("valid element ({}) at x: {} y: {}".format(data[x+1][i], x+1, i))
                        numValid = True
                        break
            if numValid:
                result += int(curnum)
            else:
                print("number invalid")
            curnum = ""
    print(result)
except Exception as e:
    print(e)