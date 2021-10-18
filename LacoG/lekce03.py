týždeň = {
    "Pondelok" : 1,
    "Utorok" :2,
    "Streda" :3,
    "Štvrtok" :4,
    "Piatok" :5
    }
mesiace = {
    "Jan" : 1,
    "Feb" : 2,
    "Mar" : 3

}

print(týždeň.keys())
print(týždeň.values())
print(týždeň.items())

# Vyber Den
print(týždeň["Pondelok"])

# Pridaj dni
týždeň["Sobota"] = 6
týždeň["Nedela"] = 7
print(týždeň.items())
#Kalendár :)
mesiac = {
    "Týždeň1" : týždeň,
    "Týždeň2" : týždeň,
    "Týždeň3" : týždeň,
    "Týždeň4" : týždeň,
}

#print(mesiac["Týždeň1"])
#print(mesiac.keys())
#print(mesiac.values())
#print(mesiac.items())
print(mesiace)
print(mesiac)
print(týždeň)
# Update
mesiace.update(mesiac)
print(mesiace)