"""Kirjoita peli, jossa tietokone arpoo
kokonaisluvun väliltä 1..10. Kone arvuuttelee
lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri
arvaus, Liian pieni arvaus tai Oikein. \
Huomaa, että tietokone
ei saa vaihtaa lukuaan arvauskertojen välissä."""

import random
luku = input ("Anna kokonaisluku 1-10: ")
luku1 = luku2 = yritykset = 0
while (luku1!=1 or luku2!=10):
    luku1 = random.randint(1,10)
    luku2 = random.randint(1,10)
    yritykset = yritykset + 1
print(f"Tarvittiin {yritykset:d} yritystä. ")
print("Oikea luku, toiminnot lopetettu. ")