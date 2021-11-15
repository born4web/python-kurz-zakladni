"""
LEKCE 4 - podminky a operatory pro testovani stavi

Pojdme se podivat na pouziti podminek. Podminka je neco co umoznuje na danem miste vetvit program nebo proste jen ridit
jeho chovani na zaklade nejakych udalosti nebo stavu.

Pozor je to prvni prikaz se kterym se setkavame, ktery vytvari blok programu ktery je jakoby do nej vnoren tedy vykona se jen
pokud je splnena podminka. Po zapsani prikazu testojuciho podminku je potreba tzv odsadit text tabulatorem nebo nekilika mezerami
pyCharm to kontroluje a je obecne potencionalni chybou to napsat ruzne na ruznych mistech nebo zamenovat tabulatory a mezery
pri odsazovani python textu. Ne ze by nutne musel zhavarovat kod ale klidne by mohl a blbe se to hleda mimo nastroje jako pyCharm...

Tak a ted konkretne k podminkam
-------------------------------

Stavy testujeme bud dotazem na stav pravda/nepravda (budeme od teto chvile pouzivat jiz jen True/False z pythonu)
a to na nejakou treba promenou nebo vysledek ktery vraci treba funkce nebo webovy formular.

Obecne k testovani pouzijeme prikaz - if

    if stav_neceho_nebo_podminka:
        print("podminka je platna")      # vykona se jen pokud je podminka platna
    else:
        print("podminka je naplatna")    # vykona se jen pokud je podminka neplatna

    if stav_neceho_nebo_podminka:
        print("podminka je platna")      # vykona se pokud je podminka platna
    print("podminka je naplatna")        # vykona se vzdy jen at vidite rozdil


    V zasade tesujeme jestli "stav_neceho_nebo_podminka" se da vyhodnotit jako True/False

    True:   1,2,3,..."retezec", [1,2,3], {1: "ahoj", 2: "nashledanou"}, True, ... cokoliv co je nenulove, nebo neprazdne
    False:  0, "", '', [], (), {}, None - specielni obecny idetifikator pro nic (muzu diky nemu rozlisit jestli je neco rovno 0 nebo None)


Testovaci operatory, ktere vraci True/False

    if a == b:      nasledujici kod se provede pokud jsou si promene rovny  testovat muzu i konstantu if a == "ahoj":
    if a != b:      pokud jsou si promene nerovny
    if a > b:       a vetsi nez b
    if a < b:       a mensi nez b
    if a <= b:      a mensi nebo rovno b
    if a >= b:      a vetsi nebo rovno b

    not             funkce pro testovani opacneho vysledku podminky
                    if a:  - testuji zda promena neco obsahuje a pokud ano vykonam kus programu v podmince
                    if not(a): - kod bykonam treba pokud je promena prazdna a ja treba to chci v programu detekovat jako chybu

    in              testuji zda prvek je v seznamu prvku - obecne rekneme list nebo tuple ale i pozdeji dalsi datove typy
                    ktere se daji povazovat za seznamy (podrobnosti ted nejsou podstatne)
                    if "a" in "ahoj":

                    pokud y = [1,2,3] pak mohu testovat

                    if x in [1,2,3]:
                    if x in y:


Slozitejsi podminky s vice moznostmi testovani a zde rozhoduje poradi jejich zapisu tedy prvni kladne vyhodnocena podminka
se provede ostatni jsou ignorovany - klicove slovo "elif" a nasleduje zase podminka pro vyhodnoceni. Jinymi slobvy rikate
pythonu zkus prvni podminku kdyz neplati zkus druhou a kolikatou chcete...kdyz vsechny testy selzou muzete a nemusite pridat
else: a ten kus kodu se vykona jen kdyz vsechny podminkz selzou

    a = 200
    b = 33
    if b > a:
      print("b je vetsi nez a")
    elif a == b:
      print("a i  b jsou si rovny")
    else:
      print("a je vetsi nez b")


Da se kombinovat i nekolik testu v jednom kroku a spojovat je logickymi operatory and - soucasne a or - nebo

    a = 200
    b = 33
    c = 500
    if a > b and c > a:
      print("Obe podminky jsou splnene vykonej  kus kodu")

    a = 200
    b = 33
    c = 500
    if a > b or a > c:
      print("Alesppon jedna podminka plati vykonej program")


Podminky se daji libovolne vnorovat do sebe. Zde prave pozor na to at dodrzite bloky textu a tim rikate pythonu
co k cemu patri

    x = 41

    if x > 10:
      print("Vice nez 10,")
      if x > 20:
        print("a take vice nez 20!")
      else:
        print("ale ne vice nez 20.")


Nekdy treba kdyz existuje blok kodu ktery musite naplnit ale defakto ho nepotrebujete, nebo treba vite ze budete testovat
pozdeji nejakou podminku na tomto miste programu ale vratite se k tomu pozdeji lze pouzit klicove slovo "pass"

    a = 33
    b = 200

    if b > a:
      pass


Nekdy potrebujete zjistit zda je promena urciteho typu treba jestli je to cele cislo nebo treba retezec...
pouzijete na to funksi type(promena) nebo modernejsi a v pythonu cistejsi je isinstance(promena, datovy_typ)

    a = "textik"   -  datovy typ string neboli str

    if type(a) == type("aaa"):
    if type(a) == str:
    if isinstance(a, str):


Cviceni:
1. otestujte si srovnavani cisel celych i desetinych
2. otestujte si velikost retezce - pouzijte k tomu funkci len(retezec)
3. otestujte si klicove slovo "in" v podmince pro list a dictionary
4. otestujte si zda je pismeno v retezci
5. udelejte program ktery otestuje ruzne datove typy promene kterou budete postupne menit a vypise vysledek ve tvaru:
   Promena: hodnota_z_promene je datoveho typu: datovy_typ
6. Zkuste si nekolik vnorenych podminek
7. zkuste si spojit veci dohromady s tim co umite. Treba vytvorte:
    apc - jako datovy dict
    naplnte hrdiny - keys
    pridejte vojaky - values
    otestujte jestli jsou awaken ;-)
    pokud ma apc v prvni rade mene nez X vojaku vypiste Booom jste mrtvi
8. zkratka pohtrajte si s necim co znate a fantazii se meze nekladou

"""
