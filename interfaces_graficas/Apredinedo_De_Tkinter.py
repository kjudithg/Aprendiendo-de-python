#APREDNIENDO SOBRE INTERFACES DE USUARIO EN PYTHON CON CUSTOM TKINTER SUB LIBRERIA DE TKINTER
"""
QUE ES CUSTOM TKINTER (CTK):
TKINDER ES LA LIBRERIA NATIVA DE PYTHON PARA INFERFACES GRAFICAS, CUSTOM TKINTER ES UNA EXTENDION CONSTRUIDA SOBRE TKINTER
QUE LE DA UN ASPECTO MODERNO Y ESTILIZADO AUTOMATICAMENTE.
SE INSTALA EN LA TERMIAL CON EL COMANDO pip install customtkinter

QUE ES UN GUI Y CUALES SON SUS COMPONENTES BASICOS:
GUI(GRAPHICAL USER INTERFACE / INTERFAS GRAFICA DE USUARIO) ES LA PARTE VISUAL DE UN PROGRAMA CON EL QUE EL USUARIO INTERACTUA

 WIDGETS (COMPONENTES): 
        WINDOW/CTk - LA VENTANA CONTENEDOR PRINCIPAL.
        LABEL /CTkLabel - MUESTRA TEXTO O IMAGENES (NO INTERACRIVO).
        ENTRY /CTkEntry - CAMPO DE TEXTO DE UNA SOLA LINEA PARA RECIBIR ENTRADAS DE USURIO.
        BUTTON /CTkButton - BOTON QUE EJECUTA UNA FUNCION AL HACER CLIC.
        FRAME /CTkFrame - RECUADRO CONTENEDOR PARA AGRUPAR OTROS WIDGETS YORGANIZAR EL DISEÑO.

VENTANA PRICIPAL Y BUCLE (mainloop)
 import customtkinter as ctk
 app = ctk.CTK() - INTANCIA LA VENTANA PRINCIPAL.
 app.mainloop() - INICIA UN BUCLE INFINITO DE EVENTOS (ESCUCHA CLICS, PULSACIONES DE TECLAS, REDIMENSIONAMIENTOS) 
 SIN ESTO EL PROGRAMA ABRIRIA LA VENTANA Y SE CERRARIA EN MILISEGUNDOS .

CONFIGURACION DE LA VENTANA
 app = ctk.CTK() - INTANCIA LA VENTANA PRINCIPAL.
 app.title("MI APP") -  DEFINE EL TITULO EN LA BARRA SUPERIOR
 app.geometry("500*400") - DEFINE LAS DIMENSIONES INICIALES EN PIXELES (ANCHO X ALTO).

MODOS DE APARIENCIA 
 ctk.set_appearence_mode("dark")/"ligth"/"system" - PERMITE CAMBIAR EL TEMA VISUAL FACILMENTE DE FORMA GLOBAL.
 ctk.set.appearence_color_theme("blue")

RELACION CON LA PROGRAMACION ORIENTADA A OBJETOS - CADA WIDGET ES UN OBJETO, AL CREARLO SE INIDICA CUAL ES SU PADRE O CONTENEDOR.
"""

#PRACTICA
import customtkinter as ctk

#configuracion de tema global
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

#inicializacion de la ventana principal
app=ctk.CTk() # app - es el nombre de la variable que inicializa la ventana principal
app.title("PRACTICA CON CUSTOMTKINDER")
app.geometry("400x300")

#definir la funcion de ejecuta el boton, esta se debe definir siempre antes que los widgets
def saludar():
    nombre=entrada_nombre.get()# el .get() ayuda a capturar el texto que se ingresa 
    if nombre :
        label_resultado.configure(text=f"¡HOLA {nombre} BIENVENIDO!" )
    else:
        label_resultado.configure(text="POR FAVOR ESCRIBE UN NOMBRE ")

#crear los widgets
label_titulo=ctk.CTkLabel(app,text="INGRESA TU NOMBRE: ", font=("Arial",16))#texto que aparecera y indicara al usuario
label_titulo.pack(pady=10) # establece el tamaño de el contendor del texto 

entrada_nombre=ctk.CTkEntry(app,placeholder_text="ESCRIBE AQUI ...")# contendor de entrada que permite escribir en el y asi capturar lo ingresado
entrada_nombre.pack(pady=10)

boton_guardar=ctk.CTkButton(app,text="SALUDAR", command=saludar)#boton que perimite que al ser tocado se ejecute la funcion establecida 
boton_guardar.pack(pady=10)

label_resultado=ctk.CTkLabel(app,text="", font=("Arial",14,"bold"))#texto que aparecera si la funcion es llamada 
label_resultado.pack(pady=20)

#inicializar el bucle de la aplicacion

app.mainloop()