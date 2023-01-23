"""Kirjoita while-toistorakennetta käyttävä
ohjelma, joka tulostaa kolmella
jaolliset luvut väliltä 1..1000."""

eka = 0
while eka <=1000:
    if eka % 3==0:
        print(f"{eka} on kolmella jaollinen" )
        eka = eka + 1
    else:
        eka = eka + 1




