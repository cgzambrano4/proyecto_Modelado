
""" Importar la libreria de interfaz gráfica """
from tkinter import*  # Todas las librerias
from tkinter import ttk  # tabla de tkinter
from tkinter import messagebox  # Mensajes y/o Alertas 

""" Importar la libreria de pymongo, es un intermediario entre el dbms y python """
import pymongo  # Libreria de Conexión Python-MongoDB
from bson.objectid import ObjectId

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
# Control de Conexión a la BD
cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
base = cliente[MONGO_DB]  # Obtención de la BD
coleccion = base[MONGO_C]  # Obtención de la Colección
ID_CLIENTE=""

def mostrarDatos():
    try:
        registros = tabla.get_children()    # Obtencion de los datos de la tabla
        for registro in registros:
            tabla.delete(registro)
        """ Lectura de los documentos """
        for documento in coleccion.find():  # Lectura de cada uno de los Documentos
            # Muestra los datos en la tabla
            tabla.insert('', 0, text=documento["_id"], values=documento["Nombre"])
            cliente.close()  # Cierre de la sesión
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:  # Demora en tiempo de conexión
        print("Tiempo excedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:  # Fallo de la conexión
        print("Falló la conexión "+errorConexion)

def insertarDatos():
    """ Validación si no se ingresa datos """
    if len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(direccion.get()) != 0 and len(cedula.get()) != 0 and len(inicio.get()) != 0 and len(fin.get()) != 0 and len(precio.get()) != 0 and len(marca.get()) != 0 and len(modelo.get()) != 0 and len(color.get()) != 0 and len(placa.get()) != 0 :
        try:
            """ Obtención de los datos del formulario """
            documento={"Nombre":nombre.get(),"Apellido":apellido.get(),"Dirección":direccion.get(),"Cédula":cedula.get(),"FechainicioRenta":inicio.get(),"FechaFinRenta":fin.get(),"PrecioRentaDía":precio.get(),"MarcaAuto":marca.get(),"ModeloAuto":modelo.get(),"ColorAuto":color.get(),"PlacaAuto":placa.get()}
            coleccion.insert(documento)

            """ Borrado de teclado """
            nombre.delete(0,END)
            apellido.delete(0,END)
            direccion.delete(0,END)
            cedula.delete(0,END)
            inicio.delete(0,END)
            fin.delete(0,END)
            precio.delete(0,END)
            marca.delete(0,END)
            modelo.delete(0,END)
            color.delete(0,END)
            placa.delete(0,END)
            nombre.focus()
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacíos")
    mostrarDatos()

def actualizarDatos():
    global ID_CLIENTE
    if len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(direccion.get()) != 0 and len(cedula.get()) != 0 and len(inicio.get()) != 0 and len(fin.get()) != 0 and len(precio.get()) != 0 and len(marca.get()) != 0 and len(modelo.get()) != 0 and len(color.get()) != 0 and len(placa.get()) != 0 :
        try:
            idBuscar = {"_id":ObjectId(ID_CLIENTE)}
            nuevosValores={"Nombre":nombre.get(),"Apellido":apellido.get(),"Dirección":direccion.get(),"Cédula":cedula.get(),"FechainicioRenta":inicio.get(),"FechaFinRenta":fin.get(),"PrecioRentaDía":precio.get(),"MarcaAuto":marca.get(),"ModeloAuto":modelo.get(),"ColorAuto":color.get(),"PlacaAuto":placa.get()}
            coleccion.update(idBuscar,nuevosValores)
            nombre.delete(0,END)
            apellido.delete(0,END)
            direccion.delete(0,END)
            cedula.delete(0,END)
            inicio.delete(0,END)
            fin.delete(0,END)
            precio.delete(0,END)
            marca.delete(0,END)
            modelo.delete(0,END)
            color.delete(0,END)
            placa.delete(0,END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror("Los campos no pueden estar vacíos")
    mostrarDatos()
    crear["state"]="normal"
    actualizar["state"]="disabled"
    eliminar["state"]="disabled"

def eliminarDatos():
    global ID_CLIENTE
    try:
        idBuscar={"_id":ObjectId(ID_CLIENTE)}
        coleccion.delete_one(idBuscar)
        nombre.delete(0,END)
        apellido.delete(0,END)
        direccion.delete(0,END)
        cedula.delete(0,END)
        inicio.delete(0,END)
        fin.delete(0,END)
        precio.delete(0,END)
        marca.delete(0,END)
        modelo.delete(0,END)
        color.delete(0,END)
        placa.delete(0,END)
    except pymongo.errors.ConnectionFailure as error:
        print(error)
    crear["state"]="normal"
    actualizar["state"]="disabled"
    eliminar["state"]="disabled"
    mostrarDatos()

"""
def buscarDatos():
    mostrarDatos(nombre.get())
"""

def dobleClickTabla(event):
    global ID_CLIENTE
    ID_CLIENTE=str(tabla.item(tabla.selection())["text"])
    documento=coleccion.find({"_id":ObjectId(ID_CLIENTE)})[0]
    nombre.delete(0,END)
    nombre.insert(0,documento["Nombre"])
    apellido.delete(0,END)
    apellido.insert(0,documento["Apellido"])
    direccion.delete(0,END)
    direccion.insert(0,documento["Dirección"])
    cedula.delete(0,END)
    cedula.insert(0,documento["Cédula"])
    inicio.delete(0,END)
    inicio.insert(0,documento["FechainicioRenta"])
    fin.delete(0,END)
    fin.insert(0,documento["FechaFinRenta"])
    precio.delete(0,END)
    precio.insert(0,documento["PrecioRentaDía"])
    marca.delete(0,END)
    marca.insert(0,documento["MarcaAuto"])
    modelo.delete(0,END)
    modelo.insert(0,documento["ModeloAuto"])
    color.delete(0,END)
    color.insert(0,documento["ColorAuto"])
    placa.delete(0,END)
    placa.insert(0,documento["PlacaAuto"])
    crear["state"]="disabled"
    actualizar["state"]="normal"
    eliminar["state"]="normal"

""" Desarrollo """
# Ventana
ventana = Tk()  # Declaración de la Ventana Principal
ventana.title("Proyecto de MongoDB: Renta de Carros")
ventana.geometry('1200x460')  # Tamaño de la Ventana
ventana.resizable(False, False)  # No se puede ampliar

""" Tabla de Visualización de Datos """
# Declaración de la tabla para los datos
tabla = ttk.Treeview(ventana, columns=[f"#{n}" for n in range(1, 11)])
tabla.grid(row=1, column=0, columnspan=12)
tabla.heading("#0", text="ID_Cliente")
tabla.heading("#1", text="NOMBRE")
tabla.heading("#2", text="APELLIDO")
tabla.heading("#2", text="DIRECCIÓN")
tabla.heading("#3", text="CÉDULA")
tabla.heading("#4", text="FECHA_INICIO_RENTA")
tabla.heading("#5", text="FECHA_FIN_RENTA")
tabla.heading("#6", text="PRECIO_RENTA_DÍA")
tabla.heading("#7", text="MARCA_AUTO")
tabla.heading("#8", text="MODELO_AUTO")
tabla.heading("#9", text="COLOR_AUTO")
tabla.heading("#10", text="PLACA_AUTO")
tabla.bind("<Double-Button-1>",dobleClickTabla)

""" Ingreso de Formulario """
Label(ventana, text="Nombre", width=20).grid(row=2, column=0, sticky=W+E)
nombre = Entry(ventana, width=50)
nombre.grid(row=2, column=1, sticky=W+E)
nombre.focus()

Label(ventana, text="Apellido", width=20).grid(row=3, column=0, sticky=W+E)
apellido = Entry(ventana, width=50)
apellido.grid(row=3, column=1, sticky=W+E)

Label(ventana, text="Dirección", width=20).grid(row=4, column=0, sticky=W+E)
direccion = Entry(ventana, width=50)
direccion.grid(row=4, column=1, sticky=W+E)

Label(ventana, text="Cédula", width=20).grid(row=5, column=0, sticky=W+E)
cedula = Entry(ventana, width=50)
cedula.grid(row=5, column=1, sticky=W+E)

Label(ventana, text="FechainicioRenta", width=20).grid(row=6, column=0, sticky=W+E)
inicio = Entry(ventana, width=50)
inicio.grid(row=6, column=1, sticky=W+E)

Label(ventana, text="FechaFinRenta", width=20).grid(row=7, column=0, sticky=W+E)
fin = Entry(ventana, width=50)
fin.grid(row=7, column=1, sticky=W+E)

Label(ventana, text="PrecioRentaDía", width=20).grid(row=8, column=0, sticky=W+E)
precio = Entry(ventana, width=50)
precio.grid(row=8, column=1, sticky=W+E)

Label(ventana, text="MarcaAuto", width=20).grid(row=9, column=0, sticky=W+E)
marca = Entry(ventana, width=50)
marca.grid(row=9, column=1, sticky=W+E)

Label(ventana, text="ModeloAuto", width=20).grid(row=10, column=0, sticky=W+E)
modelo = Entry(ventana, width=50)
modelo.grid(row=10, column=1, sticky=W+E)

Label(ventana, text="ColorAuto", width=20).grid(row=11, column=0, sticky=W+E)
color = Entry(ventana, width=50)
color.grid(row=11, column=1, sticky=W+E)

Label(ventana, text="PlacaAuto", width=20).grid(row=12, column=0, sticky=W+E)
placa = Entry(ventana, width=50)
placa.grid(row=12, column=1, sticky=W+E)

""" Botones de la Aplicación """
crear = Button(ventana, text="Insertar Datos", command=insertarDatos,bg="dodgerblue", fg="black", width=20, height=3)
crear.grid(row=3, column=2, columnspan=1, rowspan=4, sticky=W+E+N+S)

actualizar = Button(ventana, text="Actualizar Datos", command=actualizarDatos,bg="dodgerblue", fg="black", width=20, height=3)
actualizar.grid(row=8, column=2, columnspan=1, rowspan=4, sticky=W+E+N+S)
actualizar["state"]="disabled"

eliminar = Button(ventana, text="Eliminar Datos", command=eliminarDatos,bg="dodgerblue", fg="black", width=20, height=3)
eliminar.grid(row=5, column=3, columnspan=1, rowspan=4, sticky=W+E+N+S)
eliminar["state"]="disabled"

"""
buscar = Button(ventana, text="Buscar Datos", command=buscarDatos,bg="dodgerblue", fg="black", width=20, height=3)
buscar.grid(row=8, column=3, columnspan=1, rowspan=4, sticky=W+E+N+S)
"""

mostrarDatos()

ventana.mainloop()  # Control de la Ventana Principal
