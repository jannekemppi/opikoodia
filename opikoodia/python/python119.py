# Python 119
# ==========

matriisi = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

# tulostaa matriisin toisen elementin, kolmannen elementin eli 6
print(matriisi[1][2])

# 119-1: Tee ohjelma, jossa luodaan Sudokun numeroiden jakautuminen.
sudoku = []
for elementti in range(9):
    sudoku.append([0,0,0,0,0,0,0,0,0])

# print(sudoku)


# tuodaan random kirjasto käyttöön
import random
random.seed()

# funktio sudokun näyttämiselle
def sudokunayta():
    global sudoku
    for elementti in sudoku:
        print(elementti)

def luopikkulaatikko(xpos,ypos):
    # Luo numero väliltä 1-9 ja sijoita se tyhjään ruutuun
    luotu = False
    while not luotu:
        # luo numero välillä 1-9
        numero = random.randint(1,9)

        # etsi seuraava tyhjä (0) positio
        # 9x9 ruudukossa
        xpositio = -1
        ypositio = -1
        positionfound = False
        for x in range(xpos,xpos+3):
            for y in range(ypos,ypos+3):
                if sudoku[y][x] == 0:
                    xpositio = x
                    ypositio = y
                    positionfound = True
                if positionfound:
                    break        
            if positionfound:
                break        
        # löytyikö yhtään tyhjää paikkaa?
        # me emme generoi enää, jos kaikki paikat on täynnä
        if not positionfound:
            luotu = True

        # sudoku asettaa seuraavat reunaehdot sijoitukselle
        # 1) Numerot ovat väliltä 1-9
        # 2) Kullakin rivillä voi olla yksi numero
        if sudoku[ypositio].count(numero) > 0:
            continue
        # 3) Kullakin sarakkeella voi olla yksi numero
        sarakekunnossa = True
        for elementti2 in sudoku:
            if elementti2[xpositio] == numero:
                sarakekunnossa = False
            if not sarakekunnossa:
                break
        if not sarakekunnossa:
            continue
        # 4) sudoku jakautuu 3x3 laatikoihin, joissa
        # kussakin ei saa olla samaa numeroa
        xalku = (xpositio//3)*3
        xloppu = xalku + 3
        yalku = (ypositio//3)*3
        yloppu = yalku + 3

        # 4.a) laatikon rivin tarkastelu
        laatikkokunnossa = True
        for ylaskuri in range(yalku,yloppu):
            if sudoku[ylaskuri][xalku:xloppu].count(numero) > 0:
                laatikkokunnossa = False
        if not laatikkokunnossa:
            continue

        # sijoita positioon arvo
        sudoku[ypositio][xpositio] = numero

for row in range(0, 9, 3):
    for col in range(0, 9, 3):
        print("----------")
        luopikkulaatikko(row,col)
        sudokunayta()

sudokunayta()


# Luo numero väliltä 1-9 ja sijoita se tyhjään ruutuun
luotu = False
while not luotu:
    # luo numero välillä 1-9
    numero = random.randint(1,9)

    # etsi seuraava tyhjä (0) positio
    # 9x9 ruudukossa
    xpositio = -1
    ypositio = -1
    positionfound = False
    for x in range(0,9):
        for y in range(0,9):
            if sudoku[y][x] == 0:
                xpositio = x
                ypositio = y
                positionfound = True
            if positionfound:
                break        
        if positionfound:
            break        
    # löytyikö yhtään tyhjää paikkaa?
    # me emme generoi enää, jos kaikki paikat on täynnä
    if not positionfound:
        luotu = True

    # sudoku asettaa seuraavat reunaehdot sijoitukselle
    # 1) Numerot ovat väliltä 1-9
    # 2) Kullakin rivillä voi olla yksi numero
    if sudoku[ypositio].count(numero) > 0:
        continue
    # 3) Kullakin sarakkeella voi olla yksi numero
    sarakekunnossa = True
    for elementti2 in sudoku:
        if elementti2[xpositio] == numero:
            sarakekunnossa = False
        if not sarakekunnossa:
            break
    if not sarakekunnossa:
        continue
    # 4) sudoku jakautuu 3x3 laatikoihin, joissa
    # kussakin ei saa olla samaa numeroa
    xalku = (xpositio//3)*3
    xloppu = xalku + 3
    yalku = (ypositio//3)*3
    yloppu = yalku + 3

    # 4.a) laatikon rivin tarkastelu
    laatikkokunnossa = True
    for ylaskuri in range(yalku,yloppu):
        if sudoku[ylaskuri][xalku:xloppu].count(numero) > 0:
            laatikkokunnossa = False
    if not laatikkokunnossa:
        continue

    # sijoita positioon arvo
    sudoku[ypositio][xpositio] = numero
    sudokunayta()
    print("----")

sudokunayta()

# print(sudoku)
