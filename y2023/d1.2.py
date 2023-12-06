from d1data import input
digits = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}
def hasdigit(line: str, index: int):
    passed = False
    digit = 0
    for i in range(6,2,-1):
        try:
            #print("checking {} with var {} and {} -- {}".format(line[index:(index+i)], index, i, line))
            digit = digits[line[index:(index+i)]]
            passed = True
            break
        except Exception as e:
            continue
    return passed, digit

sum = 0
for line in input.splitlines():
    print("line: {}".format(line))
    firstnum = ""
    lastnum = ""
    for x in range(len(line)):
        #print("new for index: {}".format(x))
        if line[x].isdigit():
            print("isdigit: {} val {}".format(x, line[x]))
            if firstnum == "":
                firstnum = line[x]
            lastnum = line[x]
        else:
            test, digit = hasdigit(line,x)
            if test is True:
                print("isdigit: {} val {}".format(x, digit))
                if firstnum == "":
                    firstnum = digit
                lastnum = digit
    if (firstnum+lastnum) != "":
        sum += int(firstnum+lastnum)
print(sum)