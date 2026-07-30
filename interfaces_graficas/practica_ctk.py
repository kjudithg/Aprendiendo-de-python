import customtkinter as ctk 

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

calcu=ctk.CTk()
calcu.title("CALCULADORITA")
calcu.geometry("400x480")

#------------------------------------------------------------------------------------
operando_1=0
modo_suma=False

def agregar_numero(num):
    texto_actual=str(label_pantalla.cget("text"))

    if texto_actual== "0":
        label_pantalla.configure(text=str(num))
    else:
        label_pantalla.configure(text=texto_actual+str(num))

def sumar():
    global operando_1 , modo_suma
    operando_1=float(label_pantalla.cget("text"))
    modo_suma=True
    label_pantalla.configure(text="0")

def accion_enter():
    global operando_1, modo_suma
    if modo_suma:
        operando_2=float(label_pantalla.cget("text"))
        resultado=operando_1+ operando_2

        if resultado.is_integer():
            resultado=int(resultado)

        label_pantalla.configure(text=str(resultado))
        modo_suma=False 

def limpiar():
     global operando_1 , modo_suma
     operando_1=0
     modo_suma=False
     label_pantalla.configure(text=0)

#---------------------------------------------------------------

label_titulo=ctk.CTkLabel(calcu, text=" ¡¡¡ VAMOS A SUMAR !!! ", font=("arial",18,"bold"),text_color="#1597e2")
label_titulo.pack(pady=(15,5))

label_pantalla=ctk.CTkLabel(
    calcu,
    text=0,
    font=("arial",30,"bold"),
    width=260,
    height=50,
    fg_color="#a8ddfe",
    corner_radius=8,
    anchor="e"
)
label_pantalla.pack(pady=15)

frame_botones= ctk.CTkFrame(calcu,fg_color="#cdf8ff")
frame_botones.pack(pady=10)

btn1=ctk.CTkButton(frame_botones,text=1,width=60,height=50,command=lambda: agregar_numero(1))
btn1.grid(row=0,column=0,padx=5,pady=5)

btn2=ctk.CTkButton(frame_botones,text=2,width=60,height=50,command=lambda: agregar_numero(2))
btn2.grid(row=0,column=1,padx=5,pady=5)

btn3=ctk.CTkButton(frame_botones,text=3,width=60,height=50,command=lambda: agregar_numero(3))
btn3.grid(row=0,column=2,padx=5,pady=5)

btn4=ctk.CTkButton(frame_botones,text=4,width=60,height=50,command=lambda: agregar_numero(4))
btn4.grid(row=1,column=0,padx=5,pady=5)

btn5=ctk.CTkButton(frame_botones,text=5,width=60,height=50,command=lambda: agregar_numero(5))
btn5.grid(row=1,column=1,padx=5,pady=5)

btn6=ctk.CTkButton(frame_botones,text=6,width=60,height=50,command=lambda: agregar_numero(6))
btn6.grid(row=1,column=2,padx=5,pady=5)

btn7=ctk.CTkButton(frame_botones,text=7,width=60,height=50,command=lambda: agregar_numero(7))
btn7.grid(row=2,column=0,padx=5,pady=5)

btn8=ctk.CTkButton(frame_botones,text=8,width=60,height=50,command=lambda: agregar_numero(8))
btn8.grid(row=2,column=1,padx=5,pady=5)

btn9=ctk.CTkButton(frame_botones,text=9,width=60,height=50,command=lambda: agregar_numero(9))
btn9.grid(row=2,column=2,padx=5,pady=5)


btn_suma=ctk.CTkButton(frame_botones,text="+",width=60,height=50,fg_color="#2b71d9",text_color="black",command=sumar)
btn_suma.grid(row=3,column=0,padx=5,pady=5)

btn_c=ctk.CTkButton(frame_botones,text=" C ",width=60,height=50,fg_color="#d9382b",text_color="black",command=limpiar)
btn_c.grid(row=3,column=1,padx=5,pady=5)

btn0=ctk.CTkButton(frame_botones,text="0",width=60,height=50,fg_color="#2bd966",text_color="black",command=agregar_numero(0))
btn0.grid(row=3,column=2,padx=5,pady=5)

btn_enter=ctk.CTkButton(frame_botones,text="ENTER",width=60,height=50,fg_color="#2bd966",text_color="black",command=accion_enter)
btn_enter.grid(row=4,column=1,padx=5,pady=5)

calcu.mainloop()
