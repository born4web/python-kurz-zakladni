hero_list = ["Death Rider", "Coutdown", "Huntress", "Scorpion", "Lust", "Hummingbird", "Glutton", "Sarlet", "Dawn"]
print(*hero_list)
print(hero_list[2], hero_list[3])

#Zoradenie do skupín

vehicles = hero_list[0], hero_list[1], hero_list[2]  # TODO: jen poznamkka vytvaris zde zvlastni typ seznamu 'tuple' jedna se o fixni seznam. Chova se jako normalni ale kulatymi zavorkami a neda se menit pomoci append, pop, apod.
shooters = hero_list[3], hero_list[4], hero_list[5]
fighters = hero_list[6], hero_list[7], hero_list[8]
print(f"Auta:{vehicles}")
print(f"Strelci:{shooters}")
print(f"Bojovníci:{fighters}")

print(len(vehicles))
print(len(hero_list))

# Zoradenie pomocou záporných čísel
vehicles2 = hero_list[-9], hero_list[-8], hero_list[-7]
print(f"Auta:{vehicles2}")

# Pridať do zoznamu
print("Novy zonam")
hero_list.insert(0, "Vanguard")
hero_list.insert(1, "Ferseer")

hero_list.pop(2)
hero_list.pop(3)

print(*hero_list)
vehicles3 = hero_list[0], hero_list[1],hero_list[2],   # TODO: neni to chyba ale vsimni si ze to neni syntakticky cisty kod (vlnovka u carky) takto pycharm upozornuje na neuplne cisty kod ma tam byt za carkou mezera
print(f"Nova formacia" , vehicles3)   # TODO: tady zase mezera navic :)
