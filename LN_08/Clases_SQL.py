from Funciones_SQL import *

class Datos():
    def mostrar_datos(self):
        ListaTabla(conexion(),"DATOS")

    def busqueda_datos(self):
        buscarTabla(conexion(),"DATOS","DNI")

    def ingreso_datos(self):
        insertarTabla(conexion(),"DATOS")

    def modificar_datos(self):
        modificarTabla(conexion(),"DATOS","DNI")

    def eliminar_datos(self):
        eliminarTabla(conexion(),"DATOS","DNI")


class Empresa():
    def mostrar_empresa(self):
        ListaTabla(conexion(), "EMPRESA")

    def busqueda_empresa(self):
        buscarTabla(conexion(), "EMPRESA","Nombre_empresa")

    def ingreso_empresa(self):
        insertarTabla(conexion(), "EMPRESA")

    def modificar_empresa(self):
        modificarTabla(conexion(), "EMPRESA","Nombre_empresa")

    def eliminar_empresa(self):
        eliminarTabla(conexion(), "EMPRESA","Nombre_empresa")


class Productos():
    def mostrar_productos(self):
        ListaTabla(conexion(), "PRODUCTOS")

    def busqueda_productos(self):
        buscarTabla(conexion(), "PRODUCTOS","Nombre_producto")

    def ingreso_productos(self):
        insertarTabla(conexion(), "PRODUCTOS")

    def modificar_productos(self):
        modificarTabla(conexion(), "PRODUCTOS","Nombre_producto")

    def eliminar_empresa(self):
        eliminarTabla(conexion(), "PRODUCTOS","Nombre_producto")


class Ventas():
    def mostrar_ventas(self):
        ListaTabla(conexion(), "VENTAS")

    def busqueda_ventas_IDE(self):
        buscarTabla(conexion(), "VENTAS","DNI")

    def busqueda_ventas_EMPRESA(self):
        buscarTabla(conexion(), "VENTAS","Nombre_empresa")

    def ingreso_ventas(self):
        insertarTabla(conexion(), "VENTAS")

    def eliminar_ventas(self):
        eliminarTabla(conexion(), "VENTAS","DNI")

def opc():
    print('1:Ingresar VENTA\n2:Mostrar VENTAS\n3:Buscar VENTAS realizadas por el usuario\n'
          '4:Buscar VENTAS realizadas por el nombre de la empresa\n5:Eliminar VENTAS\n'
          '6:Mostrar detalle de VENTAS\n7:Mostrar PRODUCTOS\n8:Mostrar EMPRESAS\n'
          '9:Mostrar opciones\n10:Terminar el Programa ')

def inicio(con):
    cursor = con.cursor()
    dni=input("Ingrese su DNI-->  ")
    contraseña = input("Ingrese su Contraseña-->  ")
    cursor.execute("SELECT DNI FROM DATOS WHERE DNI=? AND Contraseña=?",(dni,contraseña))
    validador=cursor.fetchone()
    if validador:
        return True
    else:
        return False


def menu():
    v=Ventas()
    p=Productos()
    e=Empresa()
    val=inicio(conexion())
    if val:
        opc()
        num=["1","2","3","4","5","6","7","8","9","10"]
        executor=input("Ingrese su elección --> ")
        while executor not in num:
            executor = input("Ingrese una opción valida--> ")
        while True:
            if executor=="1":
                v.ingreso_ventas()
            elif executor=="2":
                v.mostrar_ventas()
            elif executor == "3":
                v.busqueda_ventas_IDE()
            elif executor=="4":
                v.busqueda_ventas_EMPRESA()
            elif executor=="5":
                v.eliminar_ventas()
            elif executor=="6":
                eliminar_detalle(conexion())
                detalle(conexion())
                mostrar_detalle()
            elif executor=="7":
                p.mostrar_productos()
            elif executor=="8":
                e.mostrar_empresa()
            elif executor=="9":
                opc()
            elif executor=="10":
                break
            executor = input("--> ")
            while executor not in num:
                executor = input("Ingrese una opción valida--> ")
        else:
            print("Usuario no existe")

