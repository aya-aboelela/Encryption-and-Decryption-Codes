import math
import numpy as np


ptextinput = input("Enter Ptext : ")
key = input("Enter Key : ")


ptext = ""
for i in ptextinput:
    if i == " ":
        continue
    ptext += i

numRowAndCoulm = math.floor(math.sqrt(len(key)))

matrixKey = []

for i in range(numRowAndCoulm):
    rowKey = []
    for j in range(numRowAndCoulm):
        rowKey.append(ord(key[(i * numRowAndCoulm) + j]) - ord("a"))
    matrixKey.append(rowKey)

while len(ptext) % numRowAndCoulm != 0:
    ptext += "x"

print(ptext)

matrixPtext = []

rownumber = math.ceil(len(ptext) / numRowAndCoulm)


for i in range(numRowAndCoulm):
    rowptext = []
    for j in range(rownumber):
        rowptext.append(ord(ptext[(j * numRowAndCoulm) + i]) - ord("a"))
    matrixPtext.append(rowptext)


chipherText = np.dot(matrixKey, matrixPtext)
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = ""
for i in range(len(chipherText[0])):
    for j in range(len(chipherText)):
        index = chipherText[j][i]
        a = alpha[(index % 26)]
        ans += a

print(ans)
