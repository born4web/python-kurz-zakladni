"""
lEKCE 1 - promene a jejich typy, uvod do tisku na obrazovku

Promenne v python se nemusi na rozdil od jinych jazyku nijak deklarovat. Jejich nazvy pozor rozlisuji mala a velka pismena.
Takze Jmeno jmeno JMENO jsou tri ruzne promene...
Staci jen promenou zavest jejim jmenem a priradit data a podle typu dat ze zvoli i typ promenne. Od te chvile lze obecne
promenou pouzivat menit obsah apod. Python nezna pojem kontanta, takze kazdou promenou muzete zmenit. Konstanty pokud
je potrebujete se obvykle pisi jinak v ramci programu at je to zrejme pokud mozno na prvni pohled. Treba jmena
konstant maji vsechna velka pismena, nebo neco podobneho. Je dobre zvolit si nebo okopirovat styl psani nazvu promenych
funkci a dalsich objektu a drzet se toho a moc to nemenit at je kod co nejvic citelny...

napr.   a = 1       typ int - cele cislo
        a = 3.14    typ float - cislo s pohyblivou desetinnou carkou
        a = "ahoj"  typ str - retezec / text (mohu pouzivat stejnou dvojici uvozovek bud " ", nebo ' '
        a = 1 + 1j  typ complex - kompelxni cislo (nebudeme hned tak pouzivat jestli vubec)
        a = True    typ bool - logicka 0/1 False/True

Jak zjistim jeji typ?
        type(nazev_promene) napr. type(a) viz vyse

Mohu zmenit type promene?
        Ano pouziji nazev datoveho typu (viz. vyse) a oznacim promenou co chci zmenit jeji typ a vysledek
        priradim do nove promene... napr.

            a = 1           - priradim novou promenou vznikne typ cele cislo (int)
            b = float(a)    - zmenim typ celeho cisla na plovouci carku (float)

            text = "123"    - text reprezentujici cislo
            int(text)       - prevede text na cele cislo

Tisk na obrazovku - uplne zaklady
        - pro tisk na obrazovku slouzi funkce print(co_chci_tisknout)
        - cokoliv zadate jako parametr fukce tedy vlozite do zavorek se vyhodnoti (vypocte pokud je potreba)
          prevede na text a zobrazi na obrazovce
          Priklady:     print(a)
                        print(a+b)
                        print("ahoj chlapi")

        - tisknout lze takzvane formatovane a to dvema zpusoby zapisu jak se obsah promene zapise do tisknuteho
          textu na dane misto. Nejlepe ukazeme na prikaldu zadejme si nejake promene
                jmeno = "Petr"
                prijmeni = "Vlcek"
                vek = 49
                vyska = 182
                plat = 15.53 EUR/hod

                Chceme vytisknout radek textu aby vysledek vypadaltakto:
                    >> PRIJMENI: Vlcek, JMENO: Petr, VEK: 49, VYSKA: 182 cm, PLAT: 15.53 EUR/hod"


                Existuje nekolik zpusobu jak to udelat muy se zatim naucime dva casto pouzivane
                starsi 1) a relativne nove pridany do pythonu 2)

            1. pomoci funkce format pripojene na konec retezce, kdy jednotlive veci co chceme vlozit do textu davame
               jako parametry funkce format a jejich misto a poradi v textu oznacime {} poradovym cislem od 0,1,2...



            2. pomoci specielniho zapisu retezce ktery zacina pismenem 'f' a v retezci na misto kde chceme neco zobrazit
               napiseme primo promenou do slozenych zavorek

                print(f"PRIJMENI: {prijmeni}, JMENO: {jmeno}, VEK: {vek}, VYSKA: {vyska} cm, PLAT: {plat} EUR/hod")


ZADANI UKOLU:
    1. vlezte do adresare virtualenv\kurzpy1 a spuste si: python. Vyzkousejte si python prikazovy radek.
       Proste si jen zkouset psat prikazy. Tedy jednoducha prirazeni promenych. Zkuste je scitat a prirazovat novym
       promenym napr. x = a + b. Otestujte si datove typy jednotlivych promennych at vite co se stane kdyz sectete treba
       int a float co takto scitat treba texty? Nemusite zde psat print pokud chcete zobrazit obsah promene proste ji jen
       napisete a odeslete jako prikaz...
    2. Zkusit menit typy promenych, scitat treba texty reprezentujici cisla jako texty a co se stane kdyz je
       prevedete na coisla? Jde scitat treba promenou cislo a text reprezentujici cislo?
    3. Zkuste zakladni funkce tisku na obrazovku pomoci funkce print od nejjednodussich variant vcetne pouziti
       formatovacich funkci pro retezce az treba po komplexnejsi viz muj priklad nahore. Mente treba poradi promenych at vidite
       jak to funguje...
"""

# priklad prirazeni promene
a = "ahoj"
b = 1
c = 3.2

# vytisknu prmenou na obrazovku
print(a)

# vytisknu typ promene a
print(type(a))

# tisk s formatovanim retezce
print(f"Promena: {b}")
print("Promena: {0}".format(c))
