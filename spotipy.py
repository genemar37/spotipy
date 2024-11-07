# Se importa el módulo random para crear una playlist sugerida de forma aleatoria, módulo os y time para limpiar pantalla y contador
import random
import os
import time

nombres = ['Dua Lipa', 'Nicky Minaj', 'Justin Bieber', 'Ed Sheeran']

lista = [
{
    'nombre': 'Dua Lipa',
    'oyentes': 67221199,
    'popular': [
        'levitating',
        "we're good",
        'un dia',
        "don't start now",
        'one kiss',
    ],
    'albums': [
        'future nostalgia',
        'dua lipa deluxe'
    ],
    'discografica': 'warner - vertigo',
    'web': 'dualipa.com',
    'nacionalidad': 'britanica',
    'wiki': 'https://es.wikipedia.org/wiki/Dua_Lipa',
},
{
    'nombre': 'Nicky Minaj',
    'oyentes': 40033700,
    'popular': [
        'tusa',
        'super bass',
        'seeing green',
        'bang bang',
        'whole lotta money',
    ],
    'albums': [
        'beam me up scotty',
        'qeen',
        'the pinkprint',
        'pink friday'
    ],
    'discografica': 'Universal Motown -Young Money -Cash Money -Republic Records',
    'web': 'www.nickiminajofficial.com',
    'nacionalidad': 'trinitense',
    'wiki': 'https://es.wikipedia.org/wiki/Nicki_Minaj',
},
{
    'nombre': 'Justin Bieber',
    'oyentes': 71938798,
    'popular': [
        'peaches',
        'stay',
        'hold on',
        'stuck with U',
        '10,000 hours',
    ],
    'albums': [
        'Justice',
        'Changes',
        'Purpose',
        'Journals'
    ],
    'discografica': 'island records',
    'web': 'www.justinbiebermusic.com',
    'nacionalidad': 'inglés canadiense',
    'wiki': 'https://es.wikipedia.org/wiki/Justin_Bieber',
},
{       # Se agregó la información de Ed Sheeran en el script
        'nombre': 'Ed Sheeran',
        'oyentes': 68206922,
        'popular': [
            'perfect',
            'shape of you',
            'photograph',
            'shivers',
            'thinking out loud',
        ],
        'albums': [
            '+',
            'x',
            '÷',
            '='
        ],
        'discografica': 'Atlantic Records',
        'web': 'https://www.edsheeran.com/',
        'nacionalidad': 'británico',
        'wiki': 'https://es.wikipedia.org/wiki/Ed_Sheeran',
    }
]


# Función para mostrar el menú
def mostrar_menu():
    print("\n🎶🎶🎶 Bienvenido/a a los perfiles de los artistas 🎶🎶🎶")
    for nombre in nombres:
        print('*', nombre)
    print("\nSeleccione una opción:")
    print("1. Mostrar información de un artista")
    print("2. Agregar canciones populares a un artista")
    print("3. Generar playlist de canciones sugeridas")
    print("4. Salir")


# Función para mostrar info del artista almacenada en los diccionarios de la lista "lista", se obtiene accediendo a los valores de las llaves correspondientes
def mostrar_info(artista):
    print("\nNombre:", artista['nombre'])
    print("Oyentes:", artista['oyentes'])
    print("Canciones populares:", artista['popular'])
    print("Albums:", artista['albums'])
    print("Discográfica:", artista['discografica'])
    print("Página Web:", artista['web'])
    print("Nacionalidad:", artista['nacionalidad'])
    print("Wiki:", artista['wiki'])


# Función para agregar nuevas canciones populares al artista mediante entrada del usuario, se usa función split()
def agregar_nueva_popular(artista):
    canciones_a_agregar = input("Ingrese las nuevas canciones populares que desea agregar separadas por comas: ").split(',')
    if canciones_a_agregar:
        # Se obtiene la longitud de la llave "popular"
        longitud_anterior = len(artista['popular'])
        # Se añaden las nuevas canciones a la llave "popular" usando función .extend 
        artista['popular'].extend(canciones_a_agregar)
        # Imprime solo las nuevas canciones populares porque tomamos en cuenta la longitud anterior de la llaves "popular" 
        print("\nNuevas canciones populares agregadas de", artista['nombre'] + ":", artista['popular'][longitud_anterior:])
        

# Función para crear playlist de canciones sugeridas aleatorias
def playlist_canciones_sugeridas():
    # Se obtiene la suma de la longitud de la llaves "popular" por cada artista en la lista "lista" y se divide
    total_populares = sum(len(artista['popular']) for artista in lista) 
    mitad_populares = total_populares // 2
     
    # Se crea una lista vacía
    lista_sugerida = []
    # El bucle se detiene cuando la lista sugerida tiene aproximadamente la mitad de las canciones populares
    while len(lista_sugerida) < mitad_populares:
        # Se usa función .choice para que seleccione las canciones de forma aleatoria 
        artista_aleatorio = random.choice(lista)
        cancion_aleatoria = random.choice(artista_aleatorio['popular'])
        
        # Se evalua y agrega con función .append las canciones aleatorias
        if cancion_aleatoria not in lista_sugerida: 
            lista_sugerida.append(cancion_aleatoria) 
    print("\n🎶🎶🎶Playlist sugerida🎶🎶🎶")
    # Itera sobre cada canción en "lista_sugerida", enumerándolas desde 1
    for indice, cancion in enumerate(lista_sugerida, start=1):
        print(f"{indice}. {cancion}")      


# Función para agregar información sobre Ed Sheeran donde se consulta al usuario si desea agregarla
def agregar_info_ed():
    eleccion_usuario_ed = input("¿Desea agregar la información de Ed Sheeran? Presione S para sí o N para no: ").upper()
    if eleccion_usuario_ed == "S":
        for artista in lista:
            if artista['nombre'] == 'Ed Sheeran':
                mostrar_info(artista)
                break

    elif eleccion_usuario_ed == "N":
        print("\nNo se agregó la información de Ed Sheeran")

    else:
        print("Opción no válida")


# Función para limpiar la pantalla
def limpiar_pantalla():
    time.sleep(3)
    os.system("clear")


# Ejecución del programa
while True:

    mostrar_menu()
    eleccion_usuario_menu = input("\nIngrese el número de la opción que desea: ")

    if eleccion_usuario_menu == "1":
        artista_seleccionado = input("Ingrese el nombre del artista: ").title()
        if artista_seleccionado == 'Ed Sheeran':
            agregar_info_ed()
            limpiar_pantalla()

        else:
            for artista in lista:
                if artista['nombre'] == artista_seleccionado:
                    mostrar_info(artista)
                    limpiar_pantalla()
                    break

            else:
                print("Artista no encontrado.")

    elif eleccion_usuario_menu == "2":
        artista_seleccionado = input("Ingrese el nombre del artista al que desea agregar canciones: ").title()
        for artista in lista:
            if artista['nombre'] == artista_seleccionado:
                agregar_nueva_popular(artista)
                limpiar_pantalla()
                break
        else:
            print("Artista no encontrado.")

    elif eleccion_usuario_menu == "3":
        playlist_canciones_sugeridas()
        limpiar_pantalla()

    elif eleccion_usuario_menu == "4":
        print("\nHa seleccionado salir del sistema. Gracias por usar nuestro programa")
        break

    else:
        print("\nOpción no válida. Por favor, ingrese un número válido.")