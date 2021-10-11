"""
LEKCE 3 - datovy typ dictionary - Cast 1.

Dalsim velmi pouzivanym datovym typem je typ dictionary - ano chova se to trochu jak slovnik.

Je to soubor prvku ktere na rozdil od list nemaji index ciselny a nelezi za sebou v danem poradi, ale jednotlive prvky
maji jakysi nazyva se to klic pod kterym prvek najdete ve slovniku. Jako kdyz hledate anglicky vyraz na ceske klicove
slovo ve slovniku.

Tato promena ma zvlastni typ zapisu prvku a ty jsou uzavreny do slozenmych zavorek

    muj_slovjnik = {
        'klic1': 'prvek1',
        'klic2': 'prvek2',
        ...
    }

    Klic musi byt neco statickeho nejcasteji se setkate s retezcem (lze pouzit kterekoliv z uvozovek, ale doporucuje se
    zvyknout si na jedny a ty pouzivat a nezamenovat je, ale klicem muze byt i cislo cele nebo i desetine...

    Za klicek nasleduje dvojtecka a za ni vlastni prvek pak carka a pripadne dalsi prvek
    prvek

    Prvkem muze byt jako u listu cokoliv vcetne promenych nebo i dalsich vnorenych slovniku.

1. vytvoreni slovniku prirazenim promene

    slovnik = {
        'jmeno': 'Michal',
        'prijmeni': 'Gamer',
        'vek': 16,
        'plat': 158,
        1: 'ahoj',
        2: ,
    }

2. jak zjistim seznam klicu
    slovnik.keys()

3. jak dostanu seznam hodnot
    slovnik.values()

4. jak dostanu seznam kombinaci klic: hodnota
    slovnik.items()

    Zatim nereste co je vysledkem techto funkci jsou to specielni datove typy, ale chovaji se velmi podobne jako vam
    znamy datovy tip list a da se k nemu tak chovat a tak k tomu pristujpujte. Kdyby jste chteli mit jistotu ze je to
    list ale neni to pro nase ucely ted potreba pouzijete na vysledek funkci list(slovnik.keys()). Ale jak rikam ted
    nemusite resit...

5. Jak pridam prvek do slovniku? Specifickym zapisem prirazeni:
    slovnik[novy_klic] = prvek

    - pokud kliec neexistuje prida se do slovniku novy prvek
    - pozor pokud klic existuje prepise se novou hodnotou

6. Slovnik lze rozsirit o cely slovnik funkci update ktera ma parametr zase slovnik
    slovnikA.update(slovnikB)

    - opet plati ze pokud pridavany slovnik obsahuje prvky stejnych klicu jsou tyto prepsany novymi hodnotami

"""

slovnik1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

osoba = {
    'jmeno': 'Petr',
    'prijmeni': 'Vlcek',
    'vek': 49,
}

print(slovnik1)
print(osoba)

# pristup k prvku
jmeno = osoba['jmeno']
print(f"JMENO: {osoba['jmeno']}, PRIJMENI: {osoba['prijmeni']}, VEK: {osoba['vek']}")

# pridat neco do slovniku
slovnik1['d'] = 4
print(slovnik1)

osoba['vyska'] = 182
print(osoba)

# slouceni slovniku dohromady
osoba.update(slovnik1)
print(osoba)

# klice, hodnoty, prvky
print(slovnik1.keys())
print(slovnik1.values())
print(slovnik1.items())

