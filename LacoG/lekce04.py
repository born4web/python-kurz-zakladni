# Test1
a = input("zadaj cislo A ")
b = input("zadaj cislo B ")
if a > b :
   print("A je vačšie")
elif a < b :
   print("B je vacsie")
elif a == b :
   print("Zhoda")
# Test2 - sorry nechcelo sa mi to porovnávať jednotlivo tak som využil aj čo viem z Javy

test = ["Karta", "Pero", 1, 12.6, "a", True]
print(len(test))
x = 0
string = 0
data = 0
while x <= 5:
   print(type(test[x]))
   if type(test[x]) == str:
      string += +1
   if not type(test[x]) == str:
      data += +1
   x += +1
print("Poćet stringov je", string)
print("Iné datové typy", data)

# Last Shelter Unit Types and Heroes compilation :)
heroes = {
    "Destroya" : 50,
    "Razor"    : 50,
    "Ironguard": 50,
}
units = {
    "Fighters" : 100,
    "Cars"     : 150,
    "Shooters" : 200,
}

hero = (input(heroes.keys()))

if (hero) in (heroes.keys()) :
    print(hero)
else :
    print("zle meno")

unit = (input(units.keys()))
if (unit) in (units.keys()):
    print(unit)
else :
    print("neznama jednotka")

print("Tvoj vyber" + "\n" + hero + " " + unit )


apc = heroes[hero] + units[unit]
damge = 0
# print(apc, "-1")

if hero == "Ironguard":
    if unit == "Shooters":
       damage = 60
    if unit != "Shooters":
       damage = -100

if hero == "Razor":
    if unit == "Cars":
       damage = 60
    if unit != "Cars":
       damage = -100

if hero == "Destroya":
   damage = 0

power = apc + damage
if power < 100:
    print("Stvoril si riadnu sračku")
if power >= 100 and power < 200 :
    print("Pár zombíkov zvládneš HAHAHAHA")
if power >= 200 and power < 300:
    print("Wendell Killer" )
if power >= 300 :
    print("Perfektné si Base Killer")
print("Tvoja sila je :", apc + damage)








