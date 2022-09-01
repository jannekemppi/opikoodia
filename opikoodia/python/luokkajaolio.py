# Luokka ja olio
# ==============

# olio-ohjelmointi = object oriented programming (tai OOP)
# luokka = class
# olio = object

# Luokalla on aina ominaisuuksia ja toimintoja
# ominaisuudet ovat luokassa määritettyjä muuttujia
# toiminnat ovat funktioita, joilla luokan jäsenet tekevät jotain

# luokan avulla rakennetaan olioita.
# luokka on siis malli ja olio on mallin mukaan luotu yksittäinen asia.
# Olio on aina erillinen toisesta oliosta.
# Olion ominaisuudet voivat saada uusia arvoja sen elinaikana.
# oliot elävät omaa elämää muista olioista riippumatta.

# Luokissa määritetään myös toimintoja (funktioita).
# Näin kukin erillinen olio tekee mitä sen pitää tehdä.
# toiminta on muista olioista riippumatonta.
# toimnnoilla olion sisäisiä tietoja käytetään halutun toiminnan saavuttamiseksi.
# Toiminnat keskittyvät siihen mitä olion pitäisi pystyä tekemään.
# Muita toimintoja ei tarvitse eikä pidä tukea.

from doctest import REPORT_UDIFF


class Henkilo:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def sanonimi(self):
        print(f"Nimeni on {self.nimi}!")

# tässä näkyy että kukin olio on luomisensa jälkeen itsenäinen toisista!
henkilo1 = Henkilo("Aku Ankka", 313)
henkilo2 = Henkilo("Iines Ankka", 123)
print(henkilo1.nimi)
print(henkilo2.nimi)
henkilo2.nimi = "Roope Ankka"
print(henkilo1.nimi)
print(henkilo2.nimi)
henkilo1.sanonimi()
henkilo2.sanonimi()


# Olio-ohjelmoinnin A ja O on suunnittelu
# Periaatteessa kaikki luokat on suunniteltava etukäteen

# Asiakas luokka
# Sen on pystyttävä:
# Etsiä kirjoja
# Lainata ja palauttaa kirjoja
# Maksaan sakot
# --> Jokainen näistä asioista on funktio eli toiminnallisuus

# --> tämän jälkeen voidaan miettiä ominaisuuksia, jotka tukevat toimintoja
# Esim Kirja luokka
# Tekijä
# sivujenmäärä
# julkaisuvuosi
# Nimi
# ISBN/ISSN numero

# luokka määritetään sanalla class
class Eläin:
    # luokalla on aina konstruktori eli kuinka se rakennetaan
    # oliota luodessa konstruktori ajetaan luodulle oliolle
    def __init__(self) -> None:
        # Tähän laitetaan kaikki alustamiseen liittyvät asiat
        # eli ominaisuudet esitellään ja annetaan alkuarvot
        self.nimi = ""

elukka1 = Eläin()
elukka1.nimi = "Sylvi"
print(elukka1.nimi)
elukka2 = Eläin()
print(elukka2.nimi)

class Kissa:
    def __init__(self, rotu, nimi, sukupuoli, ikä) -> None:
        self.rotu = rotu
        self.nimi = nimi
        self.sukupuoli = sukupuoli
        self.ikä = ikä

    # toimintoja tehdessä self määrittää, että voidaan käyttää omia ominaisuuksia
    def kävelee(self):
        print(f"{self.nimi} kävelee")
    # toiminnoilla voi olla myös parametrejä
    def kehrää(self, kuvaus):
        print(f"Kissa kehrää {kuvaus}...")

kissa1 = Kissa("","Jenny","F",13)
# kutsussa sanaa self ei tarvita
kissa1.kävelee()
kissa1.kehrää("iloisesti")

# Tehtävä 1 - luo kaksi kissaa lisää
# anna niille ominaisuuksia, muuta niitä ja kutsu funktioita
kissa2 = Kissa("Katti","Kali","M",16)
kissa3 = Kissa("Katti","Galileo","M",16)
kissa3.ikä = 14
kissa3.kehrää("")

# Perintä

# Luokka ei välttämättä pysty venymään kaikkeen
# toimintojen kasautuminen lisää monimutkaistumista
# erikoistapauksien ja reunalla olevien tapauksien käsittely
# 
# --> tällöin käytetään perintää
# --> Perintää käytetään erikoistapauksien hoitamiseen!
#
# --> äitiluokka pysyy yksinkertaisena
# --> lapsiluokka hoitaa erikoistapauksen

# lapsiluokka luodaan <lapsiluokan nimi> (<äitiluokan nimi>)
# Siamilainen luokka perii Kissa luokan
class Siamilainen (Kissa):
    def __init__(self, rotu, nimi, sukupuoli, ikä, laatu) -> None:
        # lapsiluokkaa luodessa, se kutsuu aluksi äitiluokan konstruktoria
        # super() viittaa äitiluokkaan
        super().__init__(rotu, nimi, sukupuoli, ikä)
        # tämän jälkeen konstruktori toimii aivan samalla tavalla
        self.rotu = "Siamilainen"
        self.laatu = laatu

    # tämä on uusi toiminto, jota EI ole äitiluokassa
    def kilpailee(self):
        print(f"{self.nimi} kilpailee ja laatu on {self.laatu}!")

    # perivä luokka voi myös muuttaa toiminnallisuutta äidistä
    def kehrää(self, kuvaus):
        # tämä kutsuu äitiluokan kehrää(kuvaus) funktiota
        super().kehrää(kuvaus)  
        # toisaalta voimme myös tehdä omaa toiminnallisuutta!
        print(f"{self.nimi} kehrää {kuvaus}...")


siamilainen1 = Siamilainen("","Leonardo","M", 1, "erinomainen")
# perivä luokka perii äidin ominaisuudet ja toiminnat
siamilainen1.kävelee()
# perivällä luokalla voi olla uusia toimintoja, 
# joita käytetään kuten toimintoja yleensäkin
siamilainen1.kilpailee()
siamilainen1.kehrää("kauniisti")

# perintää voi ketjuttaa loputtomasti.
# lapsen alla voi olla toinen lapsi...
class Supersiamilainen (Siamilainen):
    def __init__(self, rotu, nimi, sukupuoli, ikä, laatu) -> None:
        super().__init__(rotu, nimi, sukupuoli, ikä, laatu)

# Polymorfismi liittyy perintään.
# Se tarkoittaa toiminnallisuuden periytymisen vaikutuksia.
# Perusajatus on, että lapsiluokilla on yhteisiä toimintoja 
# Esimerkiksi kaikilla graafisilla elementeillä se on piirtäminen!
print("----")
kissalista = []
kissalista.append(kissa1)
kissalista.append(kissa2)
kissalista.append(kissa3)
kissalista.append(siamilainen1)

for kissa in kissalista:
    kissa.kehrää("kauniisti")

