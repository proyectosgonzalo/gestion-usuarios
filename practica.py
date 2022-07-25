#IMPORTACIONES
from tkinter import*
from tkinter import messagebox 
import sqlite3

#-------------------- FUNCIONES ---------------------------------

#FUNCION CONECTAR

def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	
	#EXCEPCIÓN
	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		#CREAMOS UN CUADRO DE INFORMACIÓN DE CREACION DE LA BBDD
		messagebox.showinfo("BBDD", "BBDD creada con éxito")

	except:

		messagebox.showwarning("¡ATENCIÓN", "La base de datos ya existe")


#FUNCION SALIR

def salirAplicacion():

	valor=messagebox.askquestion("Salir", "Desea salir de la aplicación")

	if valor == "yes":
		messagebox.showinfo(" Salir de la APP", " Pulse OK para salir de la aplicación...")
		root.destroy()


#FUNCION LIMPIAR

def limpiarCampos():

	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete(1.0, END)


#FUNCIÓN CREAR USUARIO

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get()+
		"','" + miPass.get()+
		"','" + miApellido.get()+
		"','" + miDireccion.get()+
		"','" + textoComentario.get("1.0",END) + "')")"""

	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END) 

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
	
	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito")


#FUNCIÓN LEER

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" +miId.get())
	#Funcion que devurlve un array
	elUsuario=miCursor.fetchall()
	#Recorremos el bucle
	for usuario in elUsuario:

		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

#FUNCION ACTUALIZAR
	
def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', APELLIDO='" + miApellido.get() +
		"', PASSWORD='" + miPass.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())
	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro ACTUALIZADO con éxito")

#FUNCION BORRAR 

def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get() )
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro ELIMINADO con éxito")
#------------------------  FIN FUNCIONES --------------------------
#INTERFAZ GRÁFICA
root=Tk()
root.title(" Aplicación Registro Usuarios ")
#------------------------  MENU  --------------------------


#1º     -CREAMOS EL MENÚ
barraMenu=Menu(root)#MENU CUELGA DE ROOT
root.config(menu=barraMenu, width=300, height=300)#CONFIGURAR ESE MENU

#INCLUIR LOS ELEMENTOS DE LA BARRA DE MENÚ
bbddMenu=Menu(barraMenu, tearoff=0)#SE QUITA LAS LINEAS DE ABAJO
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir" , command=salirAplicacion)


borrarMenu=Menu(barraMenu, tearoff=0)#SE QUITA LAS LINEAS DE ABAJO
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)


crudMenu=Menu(barraMenu, tearoff=0)#SE QUITA LAS LINEAS DE ABAJO
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)


ayudaMenu=Menu(barraMenu, tearoff=0)#SE QUITA LAS LINEAS DE ABAJO
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

#PONERLO VISUALMENTE EN LA BARRA DE MENÚ
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#------------------------  FIN MENU  --------------------------

#------------------------  CAMPOS  --------------------------

miFrame=Frame(root)
miFrame.pack()

#FUNCION STRINGVAR PARA PODER RESCATAR LA INFO COMO TEXTO
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

#VAMOS POR LOS ENTRY (DONDE SE ESCRIBE)
cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)



cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")


cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)


textoComentario= Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#VAMOS POR LOS LABEL
idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e",padx=10,pady=10)


nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="e",padx=10,pady=10)


passLabel=Label(miFrame, text="Pass")
passLabel.grid(row=2, column=0, sticky="e",padx=10,pady=10)


apellidoLabel=Label(miFrame, text="Apellido")
apellidoLabel.grid(row=3, column=0, sticky="e",padx=10,pady=10)


direccionLabel=Label(miFrame, text="Dirección")
direccionLabel.grid(row=4, column=0, sticky="e",padx=10,pady=10)


comentarioLabel=Label(miFrame, text="Comentarios")
comentarioLabel.grid(row=5, column=0, sticky="e",padx=10,pady=10)

#------------------------  FIN DE CAMPOS  --------------------------


#------------------------  BOTONES  --------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1,column=0, sticky="e", padx=10,pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1,column=1, sticky="e", padx=10,pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1,column=2, sticky="e", padx=10,pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1,column=3, sticky="e", padx=10,pady=10)

#------------------------  FIN BOTONES  --------------------------










#FIN DE LA APLICACIÓN
root.mainloop()



