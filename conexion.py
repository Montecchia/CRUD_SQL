#Importamos la libreria para conectar la db
import mysql.connector 

host = "localhost"
user = "root"
passwd = ""
database = "bd1"

class Bd:
    def ConectarBD():
        try:
            conexion=mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
            print("Conexion Correcta")
            return conexion
        except mysql.connector.Error as e:
            print("Error al conectar:",e.args[0])
            return None

    def AgregarCliente(nombre, telefono, correo, sucursal):
        conexion = Bd.ConectarBD()
        cursor=conexion.cursor()

        sql = "INSERT INTO clientes(nombre, telefono, correo, sucursal) VALUES (%s, %s, %s, %s)"
        datos = (nombre, telefono, correo, sucursal)
        cursor.execute(sql, datos)

        conexion.commit()

        conexion.close()
    
    def EliminarCliente(nombre, telefono, correo, codigo):
        conexion = Bd.ConectarBD()
        cursor = conexion.cursor()

        sql = "DELETE FROM clientes WHERE nombre=%s AND telefono=%s AND correo=%s AND numero=%s"
        datos = (nombre, telefono, correo, codigo)
        cursor.execute(sql, datos)

        conexion.commit()

        conexion.close()

    def ModificarCliente(nombre, telefono, correo, sucursal, codigo):
        conexion = Bd.ConectarBD()
        cursor=conexion.cursor()

        sql = "UPDATE clientes SET nombre=%s,telefono=%s,correo=%s,sucursal=%s WHERE numero=%s"
        datos = (nombre, telefono, correo, sucursal, codigo)
        cursor.execute(sql,datos)
        conexion.commit()

        conexion.close()
    
    def MostrarClientes():
        conexion = Bd.ConectarBD()
        cursor = conexion.cursor()
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexion.close()

        return resultados
    
    def MostrarSucursales():
        conexion = Bd.ConectarBD()
        cursor = conexion.cursor()
        sql = "SELECT * FROM sucursales"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexion.close()

        return resultados
    
    ConectarBD()