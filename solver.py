import numpy as np
from PIL import Image

negative = np.array(Image.open("negative.png"))
specimen = np.array(Image.open("specimen.png"))

sbits = []
nbits = []
for x in range(0,12):
    for y in range(0,12):
        nbit = 0
        nr = negative[x, y, 0]
        ng = negative[x, y, 1]
        nb = negative[x, y, 2]
        if nr > nb:
            nbit += 2
        if ng > nb:
            nbit += 1
        nbits.append(nbit)
        sbit = 0
        sr = specimen[x, y, 0]
        sg = specimen[x, y, 1]
        sb = specimen[x, y, 2]
        if sr > sb:
            sbit += 2
        if sg > sb:
            sbit += 1
        sbits.append(sbit)

bits = np.bitwise_xor(sbits, nbits)
print(bits)
print(nbits)
print(sbits)

codons = ""
for bit in bits:
    if bit == 0:
        codons += "U"
    elif bit == 1:
        codons += "C"
    elif bit == 2:
        codons += "A"
    elif bit == 3:
        codons += "G"

print(codons)