
""" Importar la libreria de interfaz gráfica """
import pymongo  # Libreria de Conexión Python-MongoDB
from bson.objectid import ObjectId
from tkinter import *  # Todas las librerias
from tkinter import ttk  # tabla de tkinter
from tkinter import messagebox  # Mensajes y/o Alertas

""" Conexión al servidor de mongo """
MONGO_HOST = "localhost"  # Declaración del Servidor de la DB
MONGO_PUERTO = "27017"  # Declaración del Puerto del Servidor
MONGO_TIEMPO_FUERA = 1000  # Declaración del Tiempo de Respuesta

# Declaración de la Dirección URL de la Base de datos
MONGO_URL = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

""" Base de Datos """
MONGO_DB = "proyecto_P1"  # Declaración del Nombre de la BD

""" Coleccion """
MONGO_C = "registro_Alquiler"  # Declaración de la Colección de la DB

""" Control de Errores y Función"""
cliente = pymongo.MongoClient(
    MONGO_URL, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)  # Control de Conexión a la BD
base = cliente[MONGO_DB]  # Obtención de la BD
coleccion = base[MONGO_C]  # Obtención de la Colección
ID_CLIENTE = ""

messagebox.showinfo(message="No ingrese espacios en blancos en el formulario, en su lugar use el guión bajo _  en su lugar",
                    title="Importante al escribir información")

messagebox.showinfo(message="Nombre1_Nombre2", title="Ejemplo de escritura")


def mostrarDatos(nombre="", apellido="", direccion="", cedula="", inicio="", fin="", precio="", marca="", modelo="", color="", placa=""):
    objetoBuscar = {}  # Diccionario Vacío
    if len(nombre) != 0:
        objetoBuscar["Nombre"] = nombre
    if len(apellido) != 0:
        objetoBuscar["Apellido"] = apellido
    if len(direccion) != 0:
        objetoBuscar["Dirección"] = direccion
    if len(cedula) != 0:
        objetoBuscar["Cédula"] = cedula
    if len(inicio) != 0:
        objetoBuscar["FechaInicioRenta"] = inicio
    if len(fin) != 0:
        objetoBuscar["FechaFinRenta"] = fin
    if len(precio) != 0:
        objetoBuscar["PrecioRentaDía"] = precio
    if len(marca) != 0:
        objetoBuscar["MarcaAuto"] = marca
    if len(modelo) != 0:
        objetoBuscar["ModeloAuto"] = modelo
    if len(color) != 0:
        objetoBuscar["MarcaAuto"] = color
    if len(placa) != 0:
        objetoBuscar["PlacaAuto"] = placa
    try:
        registros = tabla.get_children()    # Obtencion de los datos de la tabla
        for registro in registros:
            tabla.delete(registro)
        """ Lectura de los documentos """
        for documento in coleccion.find(objetoBuscar):  # Lectura de cada uno de los Documentos
            # Muestra los datos en la tabla
            tabla.insert('', 0, text=documento["_id"], values=documento["Nombre"]+" "+documento["Apellido"]+" "+documento["Dirección"]+" "+documento["Cédula"]+" "+documento["FechainicioRenta"] +
                         " "+documento["FechaFinRenta"]+" "+documento["PrecioRentaDía"]+" "+documento["MarcaAuto"]+" "+documento["ModeloAuto"]+" "+documento["ColorAuto"]+" "+documento["PlacaAuto"])
            cliente.close()  # Cierre de la sesión
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:  # Demora en tiempo de conexión
        print("Tiempo excedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:  # Fallo de la conexión
        print("Falló la conexión "+errorConexion)


def insertarDatos():
    """ Validación si no se ingresa datos """
    if len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(direccion.get()) != 0 and len(cedula.get()) != 0 and len(inicio.get()) != 0 and len(fin.get()) != 0 and len(precio.get()) != 0 and len(marca.get()) != 0 and len(modelo.get()) != 0 and len(color.get()) != 0 and len(placa.get()) != 0:
        try:
            """ Obtención de los datos del formulario """
            documento = {"Nombre": nombre.get(), "Apellido": apellido.get(), "Dirección": direccion.get(), "Cédula": cedula.get(), "FechainicioRenta": inicio.get(
            ), "FechaFinRenta": fin.get(), "PrecioRentaDía": precio.get(), "MarcaAuto": marca.get(), "ModeloAuto": modelo.get(), "ColorAuto": color.get(), "PlacaAuto": placa.get()}
            coleccion.insert(documento)

            """ Borrado de teclado """
            nombre.delete(0, END)
            apellido.delete(0, END)
            direccion.delete(0, END)
            cedula.delete(0, END)
            inicio.delete(0, END)
            fin.delete(0, END)
            precio.delete(0, END)
            marca.delete(0, END)
            modelo.delete(0, END)
            color.delete(0, END)
            placa.delete(0, END)
            nombre.focus()
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacíos")
    mostrarDatos()


def actualizarDatos():
    global ID_CLIENTE
    if len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(direccion.get()) != 0 and len(cedula.get()) != 0 and len(inicio.get()) != 0 and len(fin.get()) != 0 and len(precio.get()) != 0 and len(marca.get()) != 0 and len(modelo.get()) != 0 and len(color.get()) != 0 and len(placa.get()) != 0:
        try:
            idBuscar = {"_id": ObjectId(ID_CLIENTE)}
            nuevosValores = {"Nombre": nombre.get(), "Apellido": apellido.get(), "Dirección": direccion.get(), "Cédula": cedula.get(), "FechainicioRenta": inicio.get(
            ), "FechaFinRenta": fin.get(), "PrecioRentaDía": precio.get(), "MarcaAuto": marca.get(), "ModeloAuto": modelo.get(), "ColorAuto": color.get(), "PlacaAuto": placa.get()}
            coleccion.update(idBuscar, nuevosValores)
            nombre.delete(0, END)
            apellido.delete(0, END)
            direccion.delete(0, END)
            cedula.delete(0, END)
            inicio.delete(0, END)
            fin.delete(0, END)
            precio.delete(0, END)
            marca.delete(0, END)
            modelo.delete(0, END)
            color.delete(0, END)
            placa.delete(0, END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror("Los campos no pueden estar vacíos")
    mostrarDatos()
    crear["state"] = "normal"
    actualizar["state"] = "disabled"
    eliminar["state"] = "disabled"


def eliminarDatos():
    global ID_CLIENTE
    try:
        idBuscar = {"_id": ObjectId(ID_CLIENTE)}
        coleccion.delete_one(idBuscar)
        nombre.delete(0, END)
        apellido.delete(0, END)
        direccion.delete(0, END)
        cedula.delete(0, END)
        inicio.delete(0, END)
        fin.delete(0, END)
        precio.delete(0, END)
        marca.delete(0, END)
        modelo.delete(0, END)
        color.delete(0, END)
        placa.delete(0, END)
    except pymongo.errors.ConnectionFailure as error:
        print(error)
    crear["state"] = "normal"
    actualizar["state"] = "disabled"
    eliminar["state"] = "disabled"
    mostrarDatos()


def buscarDatos():
    mostrarDatos(nombre.get(), apellido.get(), direccion.get(), cedula.get(), inicio.get(
    ), fin.get(), precio.get(), marca.get(), modelo.get(), color.get(), placa.get())
    """ Borrado de Datos por teclado """
    nombre.delete(0, END)
    apellido.delete(0, END)
    direccion.delete(0, END)
    cedula.delete(0, END)
    inicio.delete(0, END)
    fin.delete(0, END)
    precio.delete(0, END)
    marca.delete(0, END)
    modelo.delete(0, END)
    color.delete(0, END)
    placa.delete(0, END)
    nombre.focus()


def dobleClickTabla(event):
    global ID_CLIENTE
    ID_CLIENTE = str(tabla.item(tabla.selection())["text"])
    documento = coleccion.find({"_id": ObjectId(ID_CLIENTE)})[0]
    nombre.delete(0, END)
    nombre.insert(0, documento["Nombre"])
    apellido.delete(0, END)
    apellido.insert(0, documento["Apellido"])
    direccion.delete(0, END)
    direccion.insert(0, documento["Dirección"])
    cedula.delete(0, END)
    cedula.insert(0, documento["Cédula"])
    inicio.delete(0, END)
    inicio.insert(0, documento["FechainicioRenta"])
    fin.delete(0, END)
    fin.insert(0, documento["FechaFinRenta"])
    precio.delete(0, END)
    precio.insert(0, documento["PrecioRentaDía"])
    marca.delete(0, END)
    marca.insert(0, documento["MarcaAuto"])
    modelo.delete(0, END)
    modelo.insert(0, documento["ModeloAuto"])
    color.delete(0, END)
    color.insert(0, documento["ColorAuto"])
    placa.delete(0, END)
    placa.insert(0, documento["PlacaAuto"])
    crear["state"] = "disabled"
    actualizar["state"] = "normal"
    eliminar["state"] = "normal"


""" Desarrollo """
ventana = Tk()  # Declaración de la Ventana Principal
ventana.title("Proyecto de MongoDB: Renta de Carros")  # Título de la ventana
ventana.geometry('900x475')  # Tamaño de la Ventana
ventana.resizable(1, 1)  # Control de expansion

""" Tabla de Visualización de Datos """
# Declaración de la tabla para los datos
# Creación de las columnas de la tabla
tabla = ttk.Treeview(ventana, columns=[f"#{n}" for n in range(1, 12)])
# Declaración de la fila y ocupación de las columnas de la tabla
tabla.grid(row=1, column=0, columnspan=12)
tabla.heading("#0", text="Id_Cliente", anchor="center")  # Cabecera
tabla.heading("#1", text="Nombre", anchor="w")  # Cabecera
tabla.heading("#2", text="Apellido", anchor="w")    # Cabecera
tabla.heading("#3", text="Dirección", anchor="w")   # Cabecera
tabla.heading("#4", text="Cédula", anchor="w")  # Cabecera
tabla.heading("#5", text="FechaInicioRenta", anchor="w")    # Cabecera
tabla.heading("#6", text="FechaFinRenta", anchor="w")   # Cabecera
tabla.heading("#7", text="PrecioRentaDía", anchor="w")  # Cabecera
tabla.heading("#8", text="MarcaAuto", anchor="w")   # Cabecera
tabla.heading("#9", text="ModeloAuto", anchor="w")  # Cabecera
tabla.heading("#10", text="ColorAuto", anchor="w")  # Cabecera
tabla.heading("#11", text="PlacaAuto", anchor="w")  # Cabecera
tabla.bind("<Double-Button-1>", dobleClickTabla)    # Evento sobre la tabla

""" Ingreso de Formulario """
Label(ventana, text="Nombre", width=60, anchor="w").grid(
    row=2, column=0, sticky=W+E)

nombre = Entry(ventana, width=50)
nombre.grid(row=2, column=0)
nombre.focus()  # Muestra el cursor sobre este text

Label(ventana, text="Apellido", width=60, anchor="w").grid(
    row=3, column=0, sticky=W+E)

apellido = Entry(ventana, width=50)
apellido.grid(row=3, column=0)

Label(ventana, text="Dirección", width=60, anchor="w").grid(
    row=4, column=0, sticky=W+E)

direccion = Entry(ventana, width=50)
direccion.grid(row=4, column=0)

Label(ventana, text="Cédula", width=60, anchor="w").grid(
    row=5, column=0, sticky=W+E)

cedula = Entry(ventana, width=50)
cedula.grid(row=5, column=0)

Label(ventana, text="FechainicioRenta", width=60,
      anchor="w").grid(row=6, column=0, sticky=W+E)

inicio = Entry(ventana, width=50)
inicio.grid(row=6, column=0)

Label(ventana, text="FechaFinRenta", width=60,
      anchor="w").grid(row=7, column=0, sticky=W+E)

fin = Entry(ventana, width=50)
fin.grid(row=7, column=0)

Label(ventana, text="PrecioRentaDía", width=60,
      anchor="w").grid(row=8, column=0, sticky=W+E)

precio = Entry(ventana, width=50)
precio.grid(row=8, column=0)

Label(ventana, text="MarcaAuto", width=60, anchor="w").grid(
    row=9, column=0, sticky=W+E)

marca = Entry(ventana, width=50)
marca.grid(row=9, column=0)

Label(ventana, text="ModeloAuto", width=60, anchor="w").grid(
    row=10, column=0, sticky=W+E)

modelo = Entry(ventana, width=50)
modelo.grid(row=10, column=0)

Label(ventana, text="ColorAuto", width=60, anchor="w").grid(
    row=11, column=0, sticky=W+E)

color = Entry(ventana, width=50)
color.grid(row=11, column=0)

Label(ventana, text="PlacaAuto", width=60, anchor="w").grid(
    row=12, column=0, sticky=W+E)

placa = Entry(ventana, width=50)
placa.grid(row=12, column=0)

""" Botones de la Aplicación """
crear = Button(ventana, text="Insertar Datos", command=insertarDatos,
               bg="dodgerblue", fg="black", width=20, height=3)
crear.grid(row=2, column=1, columnspan=1, rowspan=3)

actualizar = Button(ventana, text="Actualizar Datos", command=actualizarDatos,
                    bg="dodgerblue", fg="black", width=20, height=3)
actualizar.grid(row=5, column=1, columnspan=1, rowspan=3)
actualizar["state"] = "disabled"

eliminar = Button(ventana, text="Eliminar Datos", command=eliminarDatos,
                  bg="dodgerblue", fg="black", width=20, height=3)
eliminar.grid(row=8, column=1, columnspan=1, rowspan=3)
eliminar["state"] = "disabled"

buscar = Button(ventana, text="Buscar Datos", command=buscarDatos,
                bg="dodgerblue", fg="black", width=20, height=3)
buscar.grid(row=11, column=1, columnspan=1, rowspan=3)

mostrarDatos()

ventana.mainloop()  # Control de la Ventana Principal
