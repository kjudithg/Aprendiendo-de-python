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

VENTANA PRICIPAL Y BUCLE (mainloop) - ALGO QUE SE DEBE COLOCAR SIEMPRE QUE SE TRABAJE CON ESTA LIBRERIA.
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

ADMINISTRADORES DE GEOMETRIA - PACK , GRID , PLACE : ES LA FORMA EN QUE PYTHON POSICIONA Y ACOMODA LOS WIDGETS DENTRO DE LA VENTANA.
    PACK - APILADOR AUTOMATICO:
        COMO FUNCIONA: APILA LOS WIDGETS UNO DEBAJO DE OTRO ( O AL LADO DEL OTRO ) EN ORDEN DE CREACION Y SECUENCIAL.
        USO IDEAL: APLICACIONES SIMPLES, LISTAS SENCILLAS Y PROTOTIPOS RÁPIDOS
    GRID - LA TABLA / CUADRICULA:
        COMO FUNCIONA: DIVIDE LA VENTANA EN FILAS Y COLUMNAS COMO UNA HOJA DE EXCEL.
        USO IDEAL: FORMULARIOS CON ETIQUETAS A LA IZQUIERDA Y CAJAS DE TEXTO A LA DERECHA, CALCUALDORAS O INTERFACES COMPLEJAS.
    PLACE - COORDENADAS EXCACTAS:
        COMO FUNCIONA: POSICIONA EL WIDGET EN COORDENADAS X E Y EXACTAS EN PIXELES DENTRO DE LA VENTANA.
        USO IDEAL: CASOS DONDE UN ELEMENTO DEBE ESTAR FLOTANDO SOBRE OTRO O UN DISEÑO COMPLETAMENTE FIJO.
        DESVENTAJA: SI EL USUARIO MAXIMIZA O REDIMENCIONA LA VENTANA. LOS ELEMENTOS NO SE ADANTAN Y QUEDAN DESAJUSTADOS.

  REGLA DE ORO : NO SE MEZCLA PACK Y GRID DIRECTAMENTE EN EL MISMO CONTENDOR, SI SE INTENTA USAR PACK PARA UNOS ELEMENTOS 
  Y GRID PARA OTROS EN LA MISMA VENTANA, PYTHON SE CONFUNDIRA CALCULANDO TAMAÑOS Y CONGELARA O CERRARA LA APLICACION CON UN ERROR.
  LA SOLUCION A ESTO ES FRAMES: SE CREA UN CONTENDOR INDEPENDEIENTE (CTKFrame) DENTRO DE LA VENTANA,
  UN FRAME PUEDE USAR GRID POR DENTRO MIENTRAS QUE EN LA VENTANA USA PACK POR FUERA.

BOTONES - EVENTOS Y COMMAND
    QUE ES UN EVENTO: ES CUALQUIER ACCION QUE REALIZA EL USUARIO EN LA INTERFAZ GRAFICA:
        -HACER CLIC EN UN BOTON 
        -PRESIONAR LA TECLA ENTER
        -MOVER O HACER SCROLL CON EL RATON.
        -ESCRIBIR UN TEXTO EN UNA CAJA
    PARA RESPONDER A UN EVENTO DE CLIC EN UN BOTON SE USA EL PARAMETRO COMMAND=(FUNCION SIN PARANTESIS DE EJECUCION) .

"""

#PRACTICA
import customtkinter as ctk

#configuracion de tema global
ctk.set_appearance_mode("Ligth")
ctk.set_default_color_theme("blue")


#inicializacion de la ventana principal
app=ctk.CTk() # app - es el nombre de la variable que inicializa la ventana principal
app.title("PRACTICA CON CUSTOMTKINDER")
app.geometry("800x500")

#definir la funcion de ejecuta el boton, esta se debe definir siempre antes que los widgets
def saludar():
    nombre=entrada_nombre.get()# el .get() ayuda a capturar el texto que se ingresa 
    if nombre :
        label_resultado.configure(text=f"¡HOLA {nombre} BIENVENIDO!" )
    else:
        label_resultado.configure(text="POR FAVOR ESCRIBE UN NOMBRE ")

#definir otra funcion para practicar, funcion de suma

def suma():
    try:
        num1=float(numero1.get())
        num2=float(numero2.get())
        if num1 > 0  and num2 > 0 :
            resultado= num1+num2
            if resultado.is_integer():
                resultado=int(resultado)
                label_respuesta.configure(text=f" LA SUMA DA: {resultado}")
        else:
            label_respuesta.configure(text="INGRESA NUMEROS VALIDOS (MAYORES A CERO)")

    except ValueError:
        label_respuesta.configure(text="INGRESA NÚMEROS VALIDOS")

#crear los widgets

label_titulo=ctk.CTkLabel(app,text="INGRESA TU NOMBRE: ", font=("Arial",16))#texto que aparecera y indicara al usuario
label_titulo.pack(pady=10) # establece el tamaño de el contendor del texto 

entrada_nombre=ctk.CTkEntry(app,placeholder_text="ESCRIBE AQUI ...")# contendor de entrada que permite escribir en el y asi capturar lo ingresado
entrada_nombre.pack(pady=10)

boton_guardar=ctk.CTkButton(app,text="SALUDAR", command=saludar)#boton que perimite que al ser tocado se ejecute la funcion establecida 
boton_guardar.pack(pady=10)

label_resultado=ctk.CTkLabel(app,text="", font=("Arial",14,"bold"))#texto que aparecera si la funcion es llamada 
label_resultado.pack(pady=20)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
label_suma=ctk.CTkLabel(app,text="¡¡¡ VAMOS A SUMAR !!!",font=("TIMES NEW ROMAN",16))
label_suma.pack(pady=10)

numero1=ctk.CTkEntry(app,width=200,height=20,corner_radius=4,border_width=2,bg_color="white",text_color="white",placeholder_text="INGRESA UN NUMERO POSITIVO:" )
numero1.pack(pady=5)

numero2=ctk.CTkEntry(app,width=200,height=20,corner_radius=4,border_width=2,bg_color="white",text_color="white",placeholder_text="INGRESA OTRO NUMERO POSITIVO:" )
numero2.pack(pady=5)

boton_sumar=ctk.CTkButton(app,text="SUMAR",command=suma)
boton_sumar.pack(pady=8)

label_respuesta=ctk.CTkLabel(app,text=" ", font=("Times new roman",15,"bold"))
label_respuesta.pack(pady=8)

#inicializar el bucle de la aplicacion

app.mainloop()
#PARA CORRER EL SIGUENTE CODIGO DE COMENTARSE EL ANTERIOR Y VISEVERSA
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
app2=ctk.CTk()
app2.title("PRACTICA DE GEOMETRIA EN COSTUMTKINDER")
app2.geometry("800x500")

def al_presionar():
    print("EL EVENTO DE CLICK FUNCIONO CORRECTAMENTE")

label=ctk.CTkLabel(app2,text="PRUEBA DE GRID:")
label.grid(row=0,column=0,padx=20,pady=20)

boton=ctk.CTkButton(app2,text=" HAZ CLIC ",  command=al_presionar)
boton.grid(row=0,column=1,padx=20,pady=20)

app2.mainloop()