from d2data import input_test, input_prod

input = input_prod
sum = 0
for line in input.splitlines():
    min_val = {
        "red":0,
        "green":0,
        "blue":0
    }
    #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game, res = line.split(":")
    for round in res.split(";"):
        for color in round.split(","):
            _, digit, name = color.split(" ")
            digit = int(digit)
            if digit > min_val[name]:
                min_val[name] = digit
    sum += min_val["blue"]*min_val["green"]*min_val["red"]
print(sum)