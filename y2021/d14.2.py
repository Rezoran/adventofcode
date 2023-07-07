import math
prod = """KHSNHFKVVSVPSCVHBHNP

FV -> H
SB -> P
NV -> S
BS -> K
KB -> V
HB -> H
NB -> N
VB -> P
CN -> C
CF -> N
OF -> P
FO -> K
OC -> F
BN -> V
PO -> O
OS -> B
KH -> N
BB -> C
PV -> K
ON -> K
NF -> H
BV -> K
SN -> N
PB -> S
PK -> F
PF -> S
BP -> K
SP -> K
NN -> K
FP -> N
NK -> N
SF -> P
HS -> C
OH -> C
FS -> H
VH -> N
CO -> P
VP -> H
FF -> N
KP -> B
BH -> B
PP -> F
SS -> P
CV -> S
HO -> P
PN -> K
SO -> O
NO -> O
NH -> V
HH -> F
KK -> C
VO -> B
KS -> B
SV -> O
OP -> S
VK -> H
KF -> O
CP -> H
SH -> H
NC -> S
KC -> O
CK -> H
CH -> B
KO -> O
OV -> P
VF -> V
HN -> P
FH -> P
BC -> V
HV -> N
BO -> V
PH -> P
NP -> F
FN -> F
FK -> P
SC -> C
KN -> S
NS -> S
OK -> S
HK -> O
PC -> O
BK -> O
OO -> P
BF -> N
SK -> V
VS -> B
HP -> H
VC -> V
KV -> P
FC -> H
HC -> O
HF -> S
CB -> H
CC -> B
PS -> C
OB -> B
CS -> S
VV -> S
VN -> H
FB -> N"""

dev = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

data = prod
steps = 40

polymer, connectionstr = data.split("\n\n")
conns = {}
rules = {}
for elem in connectionstr.splitlines():
    key, value = elem.split(" -> ")
    conns[key] = value
    rules[key] = 0
#print(rules)
for i in range(len(polymer)-1):
    rules[polymer[i]+polymer[i+1]] +=1
#print(rules)
for step in range(steps):
    tmprules = rules.copy()
    for rule in rules:
        if rules[rule] != 0:
            #print("adding {} {} times".format((rule[0]+conns[rule]), rules[rule]))
            #print("adding {} {} times".format((conns[rule]+rule[1]), rules[rule]))
            tmprules[(rule[0]+conns[rule])] += rules[rule]
            tmprules[(conns[rule]+rule[1])] += rules[rule]
            tmprules[rule] -= rules[rule]
            #print(tmprules)
    rules = tmprules.copy()
print("rules: {}".format(rules))

results = {}
for rule in rules:
    if rule[0] not in results:
        results[rule[0]] = rules[rule]
    else:
        results[rule[0]] += rules[rule]
    if rule[1] not in results:
        results[rule[1]] = rules[rule]
    else:
        results[rule[1]] += rules[rule]
print(results)
for i in results:
    results[i] = math.ceil(results[i] /2)
print(results)
max = 0
min = 0
for elem in results:
    if min == 0:
        min = results[elem]
    if results[elem] > max:
        max = results[elem]
    if min > results[elem]:
        min = results[elem]
print("solution: ", (max - min))