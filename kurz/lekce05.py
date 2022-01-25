"""
LEKCE 5 - cykly

Pojdme se podivat na cykly. Tyto techniky se pouzivaji pok8ud je potreba nejakou cast kodu/programu vykonavat opakovane
treba i do nekonecna. Existuji dva zakladni typy cyklu

    1. for x in seznam:     - zde rikam ze budu provadet nasledujici kod pro kazdy prvek ze seznamu
                            - protoze je seznam vzdy omezeny je tedy omezeny i pocet cyklu

    2. while podminka=True: - kod v cyklu se provadi dokud plati uvedena podminka
                            - zde tedy mohou vznikat i nekonecne smycky napr. "while True:" zde to pobezi do nekonecna



Cyklus "while"
--------------
    - jedna se o jednodussi cyklus na pochopeni i pouziti ale nese sebou prave schopnost vytvaret nekonecne smycky v programu
    - jsou chvile, nebo specificke pripady, kdy se to tak skutecne dela
    - zakladni zapis cyklu je:

            while podminka:
                ...
                kus programu
                ...

    - podminkou muze byt cokoliv co lze vyhodnotit jako pravda nepravda dokonce pravda je vyhodnocena i kdyz budu
      testovat nejakou nenulovou promenou

            a = 10
            while a:
                print("A")


    - ale beznejsi byvaji testovane podminky jako zname z pouziti "if" jako napr.

            i = 10
            while i > 0:
                print(i)
                i = i - 1

    - a to je defakto k tomuto typu cyklu vse


Cyklus "for"
------------
    - zde provadim cyklus tedy kus kodu v ramci cyklu pro kazdy prvek z nejakeho seznamu
    - seznamem je cokoliv co jako seznam jiz zname tedy list [], tuple () a take dict {}
      (zde se automaticky bere pokud nereknu jinak seznam klicu tedy {}.keys() ale take to muze byt
      {}.values() ci {}.items() podle toho co potrebuji
    - takovym seznamem muze byt i retezec kde jednotlive prvky seznamu jsou jednotlive znaky
    - pozor na operace kdy bych v ramci cyklu menil pocet prvku v seznamu nad kterym provadim cyklus to lze treba u listu
      popomci funkce [].insert [].append nebo [].pop, zde pak lehce vzniknou neocekavane vysledky

      Zapis cyklu:

            for prvek in seznam:            seznam - musi obecne existovat predem
                ...                         prvek  - promena ktera vznikne pro potrebu cyklu a vzdy obsahuje
                delam neco                           aktualni krok cyklu tedy prvek ze seznamu co je na rade
                ...


      Priklady:

      1.    a = [1,2,3,4,5]
            for x in a:
                print(x)

      2.    a = [1,2,3,4,5]
            mocniny = []
            for cislo in a:
                mocniny.insert(cislo * cislo)
            print(mocniny)

      3.    jmeno = "Petr Vlcek"
            for pismeno in jmeno:
                print(pismeno)


Specielni pripady mohou se hodit
--------------------------------
    1. funkce range(start, stop, step) - vytvari seznam cisel pocinaje start, MIMO stop s krokem step
       pokud zadate jen range(10) je to jako by jste zadali range(0, 10, 1) tedy od 0 - 9 s krokem 1
       Funkci range lze pouzit pro vytvareni seznamu pro cyklus:

            for x in range(10):
                print(x)


    2. break - klicove slovo ktere ukonci v danem okamziku provadeni cyklu jako celku

            number = 0

            for number in range(10):
                if number == 5:
                    break    # break here

                print('Number is ' + str(number))

            print('Out of loop')


    3. continue - klicove slovo ktere ukonci provadeni daneho kroku cyklu

            number = 0

            for number in range(10):
                if number == 5:
                    continue    # continue here

                print('Number is ' + str(number))

            print('Out of loop')


    4. pass - pokud potrebujete treba testovat kus kodu s cyklem a zatim se teto casti treba podmince nechcete venovat
              pouzijete toto slovo a tim defakto vytvorite pro python platny blok kodu (treba v podmince) ktery ale
              defakto nic nedela

            number = 0

            for number in range(10):
                if number == 5:
                    pass    # pass here

                print('Number is ' + str(number))

            print('Out of loop')

Cviceni:
--------
1. Vytisknete svoje jmeno po pismenech na obrazovku
2. Ze seznamu cisel vytvorte seznam mocnin a ten na konci vytisknete
3. Varianta ukolu 2. seznam a to dvojnasobku kazdeho prvku v seznamu opet na konci tisk
4. Pomoci while udelejte jednoduchy automat ktery vytiskne "zadane cislo je: xy" a misto xy bude cislo zadane z
   klavesnice. Pouzijte k tomu funkci input treba: cislo = input("zadej cislo: ").
   Pokud bude zadane cislo 0 automat skonci a podekuje za data :)
5. Pomoci cyklu for udelejte programek, ktery vase zadane jmeno vypise ne po pismenech na radku ale najednou a to
   pozpatku (zde jiz skladame veci co jsme se naucili v minulych lekcich)
6. Pohrajte si jen s funkci range, otestujte ruzne moznosti zadani parametru a overte si ze rozumite jak funkce funguje
7. otestujte si moznost ukoncit cyklus pomoci break a continue treba s pouzitim prikladu stejneho kodu viz vyse jen s
   pouzitim vzdy jineho prikazu a pozorujte rozdily v chovani kodu at porozumite co se deje
8. Zkuste sami nejaky cyklus, ktery pouzije break ci continue nebo i oboje a bude se chovat tak jak vy chcete


"""