import config
from pathlib import Path

def main ():
    print("Esto es un mensaje de chequeo. Igualmente te damos la bienvenida")
    ruta_data = Path("data") 
    ruta_json = ruta_data / "transactions.json"
    if ruta_data.is_dir():
        print ("El directorio data existe.")
    else:
        print("El directotio no existe :( No te preocupes vamos a crearlo ahora :)")
        ruta_data.mkdir()

    if ruta_json.is_file():
        print ("El archivo transactions.json existe.")
    else:
        print("El archivo no existe :( No te preocupes vamos a crearlo ahora :)")
        with open(ruta_json, "w") as archivo:
            archivo.write("")
    print(config.CATEGORIAS)


if __name__ == "__main__":
    main()