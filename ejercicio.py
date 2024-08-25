#Ejercicio de MySQL en Python usando GUI tkinter

from conexion import *

#Importamos la libreria tkinter con alias tk
import tkinter as tk

#Importamos los modulos de tkinter
from tkinter import *            #Importamos todos los modulos generales
from tkinter import ttk          #Importamos el modulo
from tkinter import messagebox   #Importamos el modulo para mensajes popup

#Creamos la clase de tkinter para darle valores al GUI   

class Clientes:      

    global campoNombre, campoTelefono, campoCorreo, campoSucursal, clientesTree, sucursalesTree, codigoCliente
    campoNombre = None
    campoTelefono = None
    campoCorreo = None
    campoSucursal = None
    codigoCliente = None
    sucursalesTree = None

    #Creamos la funcion para crear la interfaz
def Interfaz():
    global campoNombre, campoTelefono, campoCorreo, campoSucursal, clientesTree, sucursalesTree

    #Manejo de errores
    try:
        #Creamos la ventana principal
        base = Tk()
        base.geometry("1300x350") #En pixeles
        #Titulo para la ventana
        base.title("BD Clientes")

        #Desde aqui se empieza a crear el interior de la GUI

        #Caja de ingreso de valores (ventana, titulo y separaciones)
        controlBox = LabelFrame(base, text="Datos cliente", padx=5, pady=5)
        #Posicionamos la caja en la primer fila y columna
        controlBox.grid(row=0,column=0,padx=10,pady=10)

        #Creacion de etiquetas
        labelName = Label(controlBox, 
                            text="Nombre:", 
                            width=10, 
                            font = ("arial", 10)).grid(row=0, column=0)
        labelTelefono = Label(controlBox, 
                            text="Telefono:", 
                            width=10, 
                            font = ("arial", 10)).grid(row=1, column=0)
        labelCorreo = Label(controlBox, 
                            text="Correo:", 
                            width=10, 
                            font = ("arial", 10)).grid(row=2, column=0)
        labelSucursal = Label(controlBox, 
                            text="Sucursal:", 
                            width=10, 
                            font = ("arial", 10)).grid(row=3, column=0)

        #Creacion de campos de texto

        campoNombre = Entry(controlBox,
                            width=30)
        campoNombre.grid(row=0, column=1)
        campoTelefono= Entry(controlBox,
                                width=30)
        campoTelefono.grid(row=1, column=1)
        campoCorreo= Entry(controlBox,
                            width=30)
        campoCorreo.grid(row=2, column=1)
        
        #Selector de sucursal
        seleccionarSucursal = tk.StringVar()
        campoSucursal = ttk.Combobox(controlBox,
                                        width=27,
                                        values=[],
                                        state="readonly",
                                        textvariable=seleccionarSucursal)
        campoSucursal.grid(row=3, column=1)

        #Funcion que agrega un cliente con los valores ingresados
        

        #Creacion de botones

        botonEliminar = Button(controlBox,
                                text="Eliminar",
                                width=15,
                                command=EliminarCliente)
        botonEliminar.grid(row=4,column=0, pady=10)
        botonGuardar = Button(controlBox,
                                text="Guardar",
                                width=15,
                                command=AgregarCliente)
        botonGuardar.grid(row=4,column=1, pady=10)
        botonModificar = Button(controlBox,
                                text="Modificar",
                                width=15,
                                command=ModificarCliente)
        botonModificar.grid(row=4,column=2, pady=10)
        
        #Caja de clientes
        clientesBox = LabelFrame(base,
                                    text="Lista de clientes", 
                                    padx=5,
                                    pady=5)
        clientesBox.grid(row=0,column=1,padx=10,pady=10)
        
        #Creacion del treeview clientes

        clientesTree = ttk.Treeview(clientesBox, 
                                    columns=("Codigo", 
                                            "Nombre",
                                            "Telefono",
                                            "Correo",
                                            "Sucursal"),
                                    show='headings',
                                    height=5)
        
        #Definición de las columnas
        clientesTree.column("# 1",anchor=CENTER, width=100)
        clientesTree.heading("# 1",text="Codigo")
        clientesTree.column("# 2",anchor=CENTER)
        clientesTree.heading("# 2",text="Nombre")
        clientesTree.column("# 3",anchor=CENTER)
        clientesTree.heading("# 3",text="Telefono")
        clientesTree.column("# 4",anchor=CENTER)
        clientesTree.heading("# 4",text="Correo")
        clientesTree.column("# 5",anchor=CENTER, width=100)
        clientesTree.heading("# 5",text="Sucursal")
        
        #Muestra el treeview
        clientesTree.pack()

        #Mostrar la tabla
        ActualizarClientes()

        #Mostrar los datos del cliente al hacer clic en la tabla
        clientesTree.bind("<<TreeviewSelect>>", SeleccionarCliente) #Descripcion del evento de clickear

        #Caja de sucursales
        sucursalesBox = LabelFrame(base,
                                    text="Sucursales", 
                                    padx=5,
                                    pady=5)
        sucursalesBox.grid(row=1,column=0,padx=10,pady=10)

        #Treeview de sucursales
        sucursalesTree = ttk.Treeview(sucursalesBox, 
                                      columns=("Codigo", 
                                               "Nombre"),
                                      show='headings',
                                      height=3)
        
        #Columnas de sucursales
        sucursalesTree.column("# 1",anchor=CENTER)
        sucursalesTree.heading("# 1",text="Codigo")
        sucursalesTree.column("# 2",anchor=CENTER)
        sucursalesTree.heading("# 2",text="Nombre")

        sucursalesTree.pack()

        ActualizarSucursales()



        #Definimos el ciclo de ejecucion
        base.mainloop() #Siempre al final
    
    except ValueError as e:
        #Gestion de errores al crear la intefaz
        print("Error al mostrar la interfaz:", e.args[0])

#Ejecutamos la funcion para iniciar la interfaz

def AgregarCliente():
    global campoNombre, campoTelefono, campoCorreo, campoSucursal

    Bd.AgregarCliente(campoNombre.get(),
                      campoTelefono.get(),
                      campoCorreo.get(),
                      campoSucursal.get())

    campoNombre.delete(0,END)
    campoTelefono.delete(0,END)
    campoCorreo.delete(0,END)

    messagebox.showinfo("Información", "Cliente agregado con éxito")

    ActualizarClientes()
                
def ModificarCliente():
    global campoNombre, campoTelefono, campoCorreo, campoSucursal, codigoCliente
    if codigoCliente:
        Bd.ModificarCliente(campoNombre.get(), 
                            campoTelefono.get(),
                            campoCorreo.get(), 
                            campoSucursal.get(), 
                            codigoCliente)
    
    campoNombre.delete(0,END)
    campoTelefono.delete(0,END)
    campoCorreo.delete(0,END)

    messagebox.showinfo("Información", "Cliente modificado con éxito")

    ActualizarClientes()

def EliminarCliente():
    global campoNombre, campoTelefono, campoCorreo, campoSucursal
    Bd.EliminarCliente(campoNombre.get(),
                       campoTelefono.get(),
                       campoCorreo.get(),
                       codigoCliente)
    campoNombre.delete(0,END)
    campoTelefono.delete(0,END)
    campoCorreo.delete(0,END)

    messagebox.showinfo("Información", "Cliente eliminado con éxito")

    ActualizarClientes()

def ActualizarClientes():
    global clientesTree
    for fila in clientesTree.get_children():
        clientesTree.delete(fila)
    for fila in Bd.MostrarClientes():
        clientesTree.insert("","end",values=fila)

def SeleccionarCliente(event): #Por ser un clic necesita un evento
     global campoNombre, campoTelefono, campoCorreo, campoSucursal, clientesTree, codigoCliente
     #Guardamos el cliente que se selecciono con el mouse
     clienteSeleccionado = clientesTree.focus()
     #Si se selecciono un cliente se procede a obtener sus valores
     if clienteSeleccionado:
         valores = clientesTree.item(clienteSeleccionado)["values"]

         codigoCliente = str(valores[0])
         campoNombre.delete(0,END)
         campoNombre.insert(0,valores[1])
         campoTelefono.delete(0,END)
         campoTelefono.insert(0,valores[2])
         campoCorreo.delete(0,END)
         campoCorreo.insert(0,valores[3])
         campoSucursal.delete(0,END)
         campoSucursal.insert(0,valores[4])

def ActualizarSucursales():
    global sucursalesTree, campoSucursal
    sucursales = []
    for fila in sucursalesTree.get_children():
        sucursalesTree.delete(fila)
    for fila in Bd.MostrarSucursales():
        sucursales += str(fila[0])
        sucursalesTree.insert("","end",values=fila)
        campoSucursal["values"] = sucursales

Interfaz() 

    
            

