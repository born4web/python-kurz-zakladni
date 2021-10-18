jmeno = "Laco"
prijmeni = "Gramer"
vek = 38
vyska = 177
plat = 820 / 167
print(f"Priezvisko : {prijmeni}, Meno: {jmeno}, Vek: {vek}, Vyska: {vyska} cm, Almužna: {plat} EUR/hod")
print("")


# priklad prirazeni promene
a = "ahoj"
b = 1
c = 3.2
# Pokus o zoradenie pod seba :)
print(f"Hodnota : {a},{b},{c}")
print(type(a),(b),(c))              # TODO: ty zavorky jsou zbytecne u b a c i pycharm te na to vlnovkama upozornuje

# tisk s formatovanim retezce
print("")
print(f"Promena: {b,a,c}")          # TODO: Neni to chyba ale nebyva obvykle takto vypisovat naraz vice promenych, kazda by spravne mela byt v samostatnych zavorkach, obvykle by mezi nimi byt nejaky dalsi cast retezce/textu
print("Promena: {0}, Premenna: {1}".format(c,b))

