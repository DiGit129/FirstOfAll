import requests
import json

# Creamos una entrada para poner el pokemon que queremos buscar

pokemon = input("Introduce el nombre de tu pokemon:")

# Obtenemos el link de la API

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

# Con request cogemos la información

resposta = requests.get(url)

# Si hay conexión convertimos los datos a json para poder leerlos

if resposta.status_code == 200:
    dades = resposta.json()

# Usamos un bucle for para obtener la información

    tipos = []
    for tipo in dades ["types"]:
        tipos.append(tipo["type"]["name"])

    habilidades = []

    for habilidad in dades ["abilities"]:
        habilidades.append(habilidad["ability"]["name"])

    nombre = dades ["name"]
    num_pokedex = dades ["id"]
    imagen = dades ["sprites"]["front_default"]

# Imprimimos el resultado por consola

    print(f"Nombre: {nombre}")
    print(f"Número Pokedex: {num_pokedex}")
    print(f"Tipo {tipos}")
    print(f"Habilidades: {habilidades}")
    print(f"Imagen: {imagen}")

# Creamos un diccionario JSON para los datos que guardaremos después

    datosJSON = {
        "nombre": nombre,
        "numero_pokedex": num_pokedex,
        "tipos": tipos,
        "habilidades": habilidades,
        "imagen": imagen}
    
# Guardamos la información en un archivo JSON

    with open(f"{nombre}.json", "w") as archivo_json:
        json.dump(datosJSON, archivo_json, indent=2)

    print(f"Información de {nombre} ha sido guardada en {nombre}.json")

# Si no se conecta, nos mostrara un mensaje de error con la entrada incorrecta
else:
    print(f"No se ha encontrado el pokémon {pokemon}")