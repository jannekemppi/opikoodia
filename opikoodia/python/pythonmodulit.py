# Python modulien käsittelyä

# moduli otetaan käyttöön import komennolla

import os

# system antaa komennon "dir"
os.system('dir')

# kuka on loggaantunut koneelle
print(os.getlogin())

# mikä prosessi on käytössä?
print( os.getppid())

statinfo = os.stat('testitesti.txt')
print(statinfo)


import shutil
shutil.copyfile('testitesti.txt', 'hubbabubba.txt')

# Glob module
import glob
print(glob.glob('*.txt'))

import sys
print(sys.argv)

# tämä lopettaa python ohjelman
# sys.exit()

import re
lista = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(lista)

import math
print(sum([1,2,3,4]))

# Miksi float ei ole tarkka?
# tietokoneet käyttää kokonaislukuja, jotka ilmaistaan binäärisesti
# kokonaislukujen lasku on aina tarkka

print(1/3)
