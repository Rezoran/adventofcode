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


def extract_numbers(found: list):
    numbers = []
    for elem in found:
        num = data[elem[0]][elem[1]]
        for y in range(elem[1]+1, yMax):
            if data[elem[0]][y].isdigit():
                num += data[elem[0]][y]
            else:
                break
        for y in range(elem[1]-1,-1,-1):
            if data[elem[0]][y].isdigit():
                num = data[elem[0]][y] + num
            else:
                break
        if num not in numbers:
            numbers.append(num)
    print("found numbers: ", numbers)
    if len(numbers) == 2:
        return (int(numbers[0]) * int(numbers[1]))
    return 0

try:
    result = 0
    for x in range(xMax):
        for y in range(yMax):
            cur = data[x][y]
            if not cur == "*":
                continue
            print("gear found: ",cur)
            foundnumbers = []
            # begin and end 
            begin = y if y == 0 else (y-1)
            end = y if (y >= (yMax-1)) else y+1
            # current line (left and right)
            print("checking current line, begin {} end {}".format(begin, end))
            for i in range(begin,end+1):
                if data[x][i].isdigit():
                    print("valid number ({}) at x: {} y: {}".format(data[x][i], x, i))
                    foundnumbers.append([x,i])
                    #here the same number cant be found twice
            # above
            if x > 0:
                print("checking line above")
                for i in range(begin,end+1):
                    if data[x-1][i].isdigit():
                        print("valid number ({}) at x: {} y: {}".format(data[x-1][i], x-1, i))
                        foundnumbers.append([x-1,i])
            # below
            if (x < (xMax-1)):
                print("checking line below")
                for i in range(begin,end+1):
                    if data[x+1][i].isdigit():
                        print("valid number ({}) at x: {} y: {}".format(data[x+1][i], x+1, i))
                        foundnumbers.append([x+1,i])
            result += extract_numbers(foundnumbers)
    print(result)
except Exception as e:
    print(e)