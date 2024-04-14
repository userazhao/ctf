import numpy as np
from PIL import Image

cdict = {
    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "I": ["AUU", "AUC", "AUA"],
    "M": ["AUG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "Y": ["UAU", "UAC"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
    "Stop": ["UAA", "UAG", "UGA"]
}

msg = "THEALLCAPSPASSPHRASEISGENETICCIPHER"

codons = "AUG"
for c in msg:
    codons += np.random.choice(cdict[c])
codons += np.random.choice(cdict["Stop"])

def randCodon():
    return np.random.choice(list("UCAG")) + np.random.choice(list("UCAG")) + np.random.choice(list("UCAG"))

def specialCodon(codon):
    return codon in cdict["M"] or codon in cdict["Stop"]

rn = np.random.randint(12)
for x in range(0,rn):
    codon = randCodon()
    while specialCodon(codon):
        codon = randCodon()
    codons = codon + codons
for x in range(0, 11-rn):
    codon = randCodon()
    while specialCodon(codon):
        codon = randCodon()
    codons += codon

print(codons)

pbits = []
for b in codons:
    bit = 0
    if b == "U":
        pbits.append(0)
    elif b == "C":
        pbits.append(1)
    elif b == "A":
        pbits.append(2)
    elif b == "G":
        pbits.append(3)

negative = np.array(Image.open("../website/assets/negative.png"))

nbits = []
for x in range(0,12):
    for y in range(0,12):
        r = negative[x, y, 0]
        g = negative[x, y, 1]
        b = negative[x, y, 2]
        bit = 0
        if r > b:
            bit += 2
        if g > b:
            bit += 1
        nbits.append(bit)

sbits = np.bitwise_xor(pbits, nbits).reshape((12,12))

print(pbits)
print(nbits)
print(sbits)

specimen = np.zeros((12,12,3), dtype=np.uint8)
for x in range(0,12):
    for y in range(0,12):
        b = np.random.randint(1,255)
        specimen[x,y,2] = b
        if sbits[x,y] > 1:
            specimen[x,y,0] = np.random.randint(b+1,256)
        else:
            specimen[x,y,0] = np.random.randint(b)
        if sbits[x,y] % 2:
            specimen[x,y,1] = np.random.randint(b+1,256)
        else:
            specimen[x,y,1] = np.random.randint(b)

specimen = Image.fromarray(specimen)
specimen.save("../website/assets/specimen.png")