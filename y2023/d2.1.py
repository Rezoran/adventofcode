from d2data import input_test, input_prod

max_red = 12
max_green = 13
max_blue = 14

max_val = {
    "red":max_red,
    "green":max_green,
    "blue":max_blue
}

input = input_prod
sum = 0
for line in input.splitlines():
    #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    gamenum, res = line.split(":")
    _, gamenum = gamenum.split(" ")
    possible = True
    for round in res.split(";"):
        for color in round.split(","):
            _, digit, name = color.split(" ")
            digit = int(digit)
            if digit > max_val[name]:
                possible = False
    if possible is True:
        sum += int(gamenum)
print(sum)