# Injury Severity Score
# =====================

"""
There are nine AIS chapters corresponding to nine body regions:

0    Head
1    Face
2    Neck
3    Thorax
4    Abdomen
5    Spine
6    Upper Extremity
7    Lower Extremity
8    External and other.
"""

bodyregions = [0]*9


# vamman vakavuus
"""
1    Minor
2    Moderate
3    Serious
4    Severe
5    Critical
6    Maximal (currently untreatable).
"""

bodyregions[0] = 3 # Serious damage päähän
bodyregions[1] = 1 # minor damage kasvoihin
bodyregions[2] = 2 # moderate damage
bodyregions[3] = 2 # moderate damage

print(bodyregions)

"""
To calculate an ISS, take the highest AIS severity code in 
each of the three most severely injured ISS body regions, 
square each AIS code and add the three squared numbers for 
an ISS (ISS = A2 + B2 + C2 where A, B, C are the AIS scores 
of the three most injured ISS body regions). The ISS scores 
ranges from 1 to 75 (i.e. AIS scores of 5 for each category). 
If any of the three scores is a 6, the score is automatically 
set at 75. Since a score of 6 ("unsurvivable") indicates the 
futility of further medical care in preserving life, this may 
mean a cessation of further care in triage for a patient with 
a score of 6 in any category.[3]
"""

# etsitään 3 suurinta arvoa bodyregions listasta
arvoA = 0
arvoB = 0
arvoC = 0

apulista = sorted(bodyregions)
apulista.reverse()
arvoA = apulista[0]
arvoB = apulista[1]
arvoC = apulista[2]


# tämän jälkeen lasketaan kunkin arvon neliöt yhteen
# tämä summa on ISS score, joka halutaan
issscore = arvoA**2 + arvoB**2 + arvoC**2
# jos korkein arvo on 6, niin score on aina 75
if apulista[0] == 6:
    issscore = 75

print(issscore)
vahinko = [0,1,2,3,4,5]
for a in vahinko:
    for b in vahinko:
        for c in vahinko:
            bodyregions = [a,b,c,0,0,0,0,0,0]
            arvoA = 0
            arvoB = 0
            arvoC = 0
            apulista = sorted(bodyregions)
            apulista.reverse()
            arvoA = apulista[0]
            arvoB = apulista[1]
            arvoC = apulista[2]
            issscore = arvoA**2 + arvoB**2 + arvoC**2
            print(f"{bodyregions} numero on {issscore}")
