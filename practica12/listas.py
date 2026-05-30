nombres=["Rodrigo","Juan","Pedro","Santiago","Jorge","Raymundo"]
print(nombres)
#f-strings
for i, nombres in enumerate(nombres):
    #print("se inscribe", i "en la lista", i, nombre)
    print(f"se inscribió {nombres}en la lista con el indice[i]")

    print("Bienvenido a la fiesta", nombres[:3])
    print("lo siento",nombres[:3])
