"""
LEKCE 2 - datovy typ list - Cast 1.


Jednim z nejpouzivanejsich datovych typu je typ list neboli seznam. Seznam je rada nepojmenovanych prvku a jejich pozice
v seznamu jednoznacne identifikuje konkretni prvek na rozdil od typu dictionary ktery probirame v dalsi lekci.

1. Definuje se tak, ze se promene priradi seznam prvku v hranatych zavorkach a jednotlive prvky jsou oddeleny carkou

seznam_cisel = [1, 2, 5, 52, 98, 123, 8, 55, 984, 0]

2. typ se zjisti u promene pomoci funkce list(jmeno_promene)

3. k prvkum seznamu se pristupuje pomoci tzv. indexu coz je ciselne poradi prvku v seznamu. Index pouziji jako cislo v
hranatych zavorkach za jmene promene. Pozor jen je potreba si zvyknout ze poradi nezacina jednickou jak by se mohlo zdat
ale nulou. Poradi/index se pocita od prvku zleva doprava. Prvni prvek seznamu je tedy nejvic vlevo a posledni
nejvic vpravo.

prvek1 = seznam_cisel[0]
prvek2 = seznam_cisel[1]

4. muzete pouzit pro oznaceni indexu i zaporna cisla a tim jdete jakoby seznamem v protismeru

seznam_cisel[-1] ukazuje na prvni prvek zprava tedy na posledni prvek seznamu a tak dale

vyzkousejte si treba co se stane kdyz pouzijete neexistujici index na kteroukoliv stranu

5. list lze pomoci indexu filtrovat v existujicim rozmezi indexu. v nasem prikladu je to 0-9. A to bud pouzijete konkretni
dvojici cisel indexu nebo nektere z tech cisel vynechate. Zase lze pouzivat i zaporna cisla ale musi to davat smysl.
Take cvicenim zjistite ze horni index se ignoruje, resp je to od prvniho indexu vcetne az po posledni prvku v seznamu.


seznam_cisel[0:3]

Dokonce funguje i to ze horni index nemusi byt platny
seznam_cisel[0:3]


Zjistete proc treba tady jeden smysl dava a druhy ne? I kdyz to neni chyba...Treba si to i namalujte na papir :)
seznam_cisel[-1:5]
seznam_cisel[-10:5]

Dalsi priklady vyberu ze seznamu
seznam_cisel[-2:]
seznam_cisel[:5]
seznam_cisel[2:-2]
seznam_cisel[-10:5]

6. Jak muzete rozsitit existujici seznam

    - pridate prvek na jeho konec    jmeno_seznamu.append(prvek)

    - vlozite prvek na misto indexu    jmeno_seznamu.insert(index, prvek)

    - pridate k nemu dalsi seznam pomoci operatoru scitani tedy: +     novy_seznam = seznam_cisel + [7, 8, 9]

7. Jak vyradit prvek ze seznamu
    - pomoci funkce pop nad seznamem kde parametrem je index prvku jmeno_seznamu.pop(index)
    - pokud pouzijete funkci pop bez parametru odebere vzdy posledni prvek ze seznamu
    - funkce pop take vraci jako vysledek hodnotu prave toho prvku ktery davate pryc ze seznamu
            prvek = jmeno_seznamu.pop(index_prvku)

8. Seznam muze obsahovat libovolne prvky soucasne vcetne jinych promenych, nebo celych seznamu. Takze se da pouzit jako
   jakysi reknem sklad na ruzne veci a jen vy vite co na kterem miste seznamu je ulozeno ve vasem programu
        ruzne_veci = [1, 'ahoj', [0.1, 0.5, 1.5], seznam_cisel, True]

SE SEZNAMY V TETO LEKCI SE ZASE DOBRE A RYCHLE PRACUJE ZKOUSI SE  UCI SE PRIMO V PYTHON RADKU ALE KLIDNE TO DELEJTE ZDE

"""

# realny kod z lekce - MUZE OBSAHHOVAT CHYBY ! (odstranit chybu muzete tak ze pridate # na zacatek prislusneho radku
# tedy udelate z nej komentar

seznam_cisel = [1, 2, 5, 52, 98, 123, 8, 55, 984, 0]

print(type(seznam_cisel))


# Jak nacist prvek ze senamu? Pomoci jeho indexu
prvek1 = seznam_cisel[0]
prvek2 = seznam_cisel[1]
print(prvek1)
print(prvek2)

# Odkaz na prvek indexem ruzne priklady
print(seznam_cisel[0])
print(seznam_cisel[-1])
print(seznam_cisel[5])
print(seznam_cisel[-100])
print(seznam_cisel[21])

# Vyber ze seznamu - vysledkem je zase seznam ale vyhovujici kriteriim - zadanym rozsahum indexu
print(seznam_cisel[-1:5])
print(seznam_cisel[-10:5])
print(seznam_cisel[-2:])
print(seznam_cisel[:5])
print(seznam_cisel[2:-2])
print(seznam_cisel[-10:5])

# rozsireni seznamu
seznam_cisel.append(999)
print(seznam_cisel)

seznam_cisel.insert(1, 888)
print(seznam_cisel)

print(seznam_cisel + [7, 8, 9])

# ruzne prvky v seznamu

jmeno = "Petr"
prijmeni = "Vlcek"
vek = 49
plat = 158.5
miry = [80, 120, 140]

udaje_osoby = [jmeno, prijmeni, vek, plat, miry, False]   # True/False jsou tzv logicke hodnoty tady treba mohou mit smysl ze je zamestnanec aktivni nebo jiz propusteny :)


