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
steps = 10

polymer, connectionstr = data.split("\n\n")
conns = {}
for elem in connectionstr.splitlines():
    key, value = elem.split(" -> ")
    conns[key] = value
print("Template:    ", polymer)

for step in range(steps):
    newpolymer = ""
    for i in range(len(polymer)-1):
        #print("key: ", i, i+2, polymer[i:i+2])
        key = polymer[i:i+2]
        #print("adding: ", polymer[i], conns[key], polymer[i+1])
        newpolymer += polymer[i]+conns[key]
    newpolymer += polymer[len(polymer)-1]
    polymer = newpolymer
    #print("After Step {}: {}".format(step+1, polymer))
print("len: ", len(polymer))

results = {}
for monomer in polymer:
    if monomer not in results:
        results[monomer] = 1
    else:
        results[monomer] += 1
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