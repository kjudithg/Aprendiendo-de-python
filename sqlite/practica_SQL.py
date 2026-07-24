import sqlite3
import random
import os 
#SACAR LA RUTA DE DONDE SE DEBE CREAR EL ARCHIVO DE LA BASE DE DATOS , ASI SE CREA SOLO EN LA CARPETA INDICADA
ruta_carpeta=os.path.dirname(os.path.abspath(__file__))
ruta_base_datos=os.path.join(ruta_carpeta,"parqueadero.db")

#CREAioCION DE BASE DE DATOS 
conexion= sqlite3.connect(ruta_base_datos)
cursor=conexion.cursor()
#PARA PODER USAR CLAVES FORANEAS 
cursor.execute("PRAGMA foreign_keys = ON;")
#CREACION DE LAS TABLAS DEL SISTEMA DE PARQUEADERO
#TABLA PROPIETARIO
cursor.execute("""
                CREATE TABLE IF NOT EXISTS propietario(
                ID_PROPIETARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                CEDULA_PRO TEXT,
                NOMBRE TEXT,
                CELULAR TEXT,
                CORREO TEXT
               )

                """)
#TABLA VEHICULOS 
cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehiculos (
                ID_VEHICULO INTEGER PRIMARY KEY AUTOINCREMENT,
                PLACA TEXT ,
                MARCA TEXT,
                COLOR TEXT 
               )
                """)
#TABLA REGUISTROS DE INGRESO Y SALIDA DE VEHICULOS RELACIOANADOS A SU PROPIETARIO
cursor.execute("""
                CREATE TABLE IF NOT EXISTS registros_parqueadero(
                ID_REGISTRO INTEGER PRIMARY KEY AUTOINCREMENT,
                ID_PROPIETARIO INTEGER,
                ID_VEHICULO INTEGER,
                FECHA_INGRESO TEXT,
                FECHA_SALIDA TEXT ,
                VALOR_PAGADO REAL,
                FOREIGN KEY (ID_PROPIETARIO) REFERENCES propietario (ID_PROPIETARIO), 
                FOREIGN KEY (ID_VEHICULO) REFERENCES vehiculos (ID_VEHICULO)
               )
                """)

#INSERCION DE DATOS EN LAS TABLAS 
#LISTAS DE DATOS PARA COMBINAR  LOS DATOS  HE INSERTAR EN LA TABLA  DE LOS PROPIETARIOS

nombres=["JUAN","MARIA","CARLOS","ANA","LUIS","DIANA","PEDRO","LAURA","ANDRES","SOFIA","LAURA","ESTEFANIA","THOMAS"]
apellidos=["GOMEZ","RODRIGUEZ","LOPEZ","PEREZ","MARTINEZ","GARCIA","SILVA","TORRES","PINZON","DIAZ","VANEGAS","GARCIA"]
dominios=["gmail.com","ooutlook.com","yahoo.com"]

#BUCLE PARA CONVINAR LOS DATOS EN LAS LISTAS Y LUEGO INSERTARLOS EN LA BASE DE DATOS
for i in range (80):
    #GENERACION AUTOMATICA DE DATOS 
    cedula=random.randint(10000000,99999999)
    nombre_completo=f"{random.choice(nombres)} {random.choice(apellidos)}"
    celular=f"318{random.randint(1000000,9999999)}"
    correo=f"{nombre_completo.lower().replace(' ', '')}{random.randint(1,99)}@{random.choice(dominios)}"

    #SQL PARA INSERTAR LOS DATOS GENERADOS A LA BASE DE DATOS
    cursor.execute("""
                    INSERT INTO propietario (CEDULA_PRO,NOMBRE,CELULAR,CORREO)
                    VALUES(?,?,?,?)
                    """, (cedula,nombre_completo,celular,correo))
    conexion.commit()

#LISTAS DE DATOS PARA COMBINAR LOS DATOS HE INSERTAR EN LA TABLA DE VEHICULOS

marcas=["TOYOTA","CHEVROLET","MAZDA","KIA","RENAULT"]
colores=["NEGRO","BLANCO","GRIS","ROJO","AZUL"]
letras_placa=["AAA","BBB","CCC","DDD","EEE"]

for i in range (80):
    placa=f"{random.choice(letras_placa)}{random.randint(100,999)}"
    marca=random.choice(marcas)
    color=random.choice(colores)

    cursor.execute("""
                    INSERT INTO vehiculos (PLACA,MARCA,COLOR)
                    VALUES(?,?,?)
                    """, (placa,marca,color))
    conexion.commit()

#PARA INSERTAR LOS DATOS EN LA TABLA DE REGISTROS ES MAS DELICADO, HAY QUE TRAER PRIMERO LOS ID DE LOS CLIENTES Y  VEHICULOS,
#YA QUE LA TABLA REGISTROS TIENE A ESTOS COMO CLAVES FORANEAS
cursor.execute("SELECT ID_PROPIETARIO FROM propietario")
lista_propietarios=[fila[0] for fila in cursor.fetchall()]
cursor.execute("SELECT ID_VEHICULO FROM vehiculos")
listas_vehiculos=[fila[0] for fila in cursor.fetchall()]
#BUCLE PARA LA INSERCION DE DATOS
for i in range (160):
    propietario_aleatorio=random.choice(lista_propietarios)
    vehiculos_aleatorios=random.choice(listas_vehiculos)
    fecha_ingreso=f"2026-07-{random.randint(10,18)}"
    fecha_salida=f"2026-07-{random.randint(10,18)}"
    valor=random.choice([5000,8000,12000,15000]) 

    cursor.execute("""
                    INSERT INTO registros_parqueadero(ID_PROPIETARIO,ID_VEHICULO,FECHA_INGRESO,FECHA_SALIDA,VALOR_PAGADO)
                    VALUES(?,?,?,?,?)
                    """, (propietario_aleatorio,vehiculos_aleatorios,fecha_ingreso,fecha_salida,valor))
    conexion.commit()

#HACIENDO CONSULTAS DE DATOS

#OBTENER UNICAMENTE LOS NOMBRE Y CORREOS DE TODOS  LOS PROPIETARIOS  REGISTRADOS
cursor.execute("SELECT NOMBRE, CORREO FROM propietario; ")
resultado=cursor.fetchall()
print(f" NOMBRE Y CORREO DE LOS PROPIETARIOS:")
for r in resultado:
    print(r)

#MOSTRAR TODA LA INFORMACION DE LOS VEHICULOS QUE SEAN DE MARCA TOYOTA 
cursor.execute(" SELECT ID_VEHICULO,PLACA,COLOR FROM vehiculos WHERE MARCA='TOYOTA';")
resultado=cursor.fetchall()
print(f" VEHICULOS CUYA MARCA ES TOYOTA:")
for r in resultado:
    print(r)

#MOSTRAR TODOS LOS INGRESOS DEL PARQUEADERO DONDE EL VALOR PAGADO SEA MAYOR A 8000
cursor.execute("SELECT * FROM registros_parqueadero WHERE VALOR_PAGADO>8000; ")
resultado=cursor.fetchall()
print(f" REGISTROS DEL PARQUEADERO DONDE SE PAGO MAS DE  8000 :")
for r in resultado:
    print(r)

#ENCONTRAR A TODOS LOS PROPIETARIOS CUYO CORREO ELECTRONICO TERMINA EN @GMAIL.COM
cursor.execute(" SELECT NOMBRE FROM propietario WHERE CORREO  LIKE '%@gmail.com'")
resultado=cursor.fetchall()
print(f"PROPIETARIOS QUE TIENEN UN CORREO ELECTRONICO GMAIL:")
for r in resultado:
    print(r)

#LISTAR TODAS LAS PLACAS Y MARCAS DE LOS VEHICULOS QUE SEAN DE COLOR ROJO O BLANCO
cursor.execute("SELECT PLACA , MARCA FROM vehiculos WHERE COLOR = 'ROJO' OR COLOR='BLANCO'")
resultado=cursor.fetchall()
print(f" PLACA Y MARCA DE LOS VEHICULOS CON COLOR ROJO O BLANCO:")
for r in resultado:
    print(r)

#OBTENER EL ID DE REGISTRO , PLACA , MARCA DEL VEHICULO Y NOMBRE DEL PROPIETARIO PARA CADA ENTRADA AL PARQUEADERO
cursor.execute("""
                SELECT R.ID_REGISTRO,V.PLACA,V.MARCA,P.NOMBRE 
                FROM registros_parqueadero AS R
                JOIN propietario  AS P ON R.ID_PROPIETARIO=P.ID_PROPIETARIO
                JOIN vehiculos AS V ON R.ID_VEHICULO=V.ID_VEHICULO 
                """)
resultado=cursor.fetchall()
print(f"VEHICULO Y SU DUEÑO EN EL PARQUEADERO:")
for r in resultado:
    print(r)

#ELEGIR A UN PROPIETARIO  Y MOSTRAR SU HISTORIAL EN EL PARQUEADERO , INDICANDO LA FECHA DE INGRESO , SALIDA Y EL VALOR PAGADO
cursor.execute("""
                SELECT FECHA_INGRESO,FECHA_SALIDA FROM registros_parqueadero 
                WHERE ID_PROPIETARIO = 5 
               
                """)
resultado=cursor.fetchall()
print(f"HISTORIAL EN EL PARQUEADERO DEL PROPIETARIO 5:")
for r in resultado:
    print(r)

#MOSTRAR LA PLACA, COLOR Y VALOR PAGADO DE TODOS LOS REGISTROS DE INGRESO
cursor.execute("""
                SELECT V.PLACA,V.COLOR,R.VALOR_PAGADO 
                FROM registros_parqueadero AS R
                JOIN vehiculos AS V ON R.ID_VEHICULO=V.ID_VEHICULO
                LIMIT 30
                """)
resultado=cursor.fetchall()
print(f" PLACA, COLOR Y VALOR PAGADO DE TODOS LOS REGISTROS EN EL MES:")
for r in resultado:
    print(r)

#CALCULAR EL DINERO TOTAL GANADO EN EL PARQUEADERO
cursor.execute("SELECT SUM(VALOR_PAGADO) AS DINERO_RECAUDADO FROM registros_parqueadero")
resultado=cursor.fetchall()
print(f" GANANCIA TOTAL : ")
for r in resultado:
    print(r)

#CUANTOS VEHICULOS REGISTRADOS HAY POR MARCA , SE DEBE MOSTRAR LA MARCA Y CANTIDAD
cursor.execute("""
                SELECT MARCA , COUNT(ID_VEHICULO)
                FROM vehiculos      
                GROUP BY MARCA 
                """)
resultado=cursor.fetchall()
print(f" NUMERO DE VEHICULOS REGISTRADOS POR CADA MARCA:")
for r in resultado:
    print(r)

#VALOR PROMEDIO RECAUDADO POR CADA REGISTRO DEL PARQUEADERO
cursor.execute(" SELECT AVG(VALOR_PAGADO) AS PROMEDIO_RECAUDADO FROM registros_parqueadero")
resultado=cursor.fetchall()
print(f"INGRESO PROMEDIO:")
for r in resultado:
    print(r)

#MOSTRAR EL NOMBRE DEL PROPIETARIO JUNTO CON LA CANTIDAD TOTAL DE VECES QUE HA USADO EL PARQUEADERO Y SE DEBE ORDENAR DE MAYOR A MENOR
cursor.execute("""
               SELECT P.NOMBRE , COUNT(R.ID_PROPIETARIO)
               FROM registros_parqueadero AS R
               JOIN propietario AS P ON R.ID_PROPIETARIO=P.ID_PROPIETARIO
               GROUP BY P.NOMBRE 
               ORDER BY NOMBRE DESC
               """)
resultado=cursor.fetchall()
print(f"PROPIETARIO Y VECES QUE HAN INGRESADO AL PARQUEADERO:")
for r in resultado:
    print(r)

#MOSTRAR EL NOMBRE DEL PROPIETARIO Y LA SUMA TOTAL DE DINERO QUE HA PAGADO EN SUS INGRESOS AL PARQUEADERO
cursor.execute("""
                SELECT P.NOMBRE , SUM(R.VALOR_PAGADO)
                FROM registros_parqueadero AS R
                JOIN propietario AS P ON R.ID_PROPIETARIO=P.ID_PROPIETARIO
                GROUP BY P.NOMBRE
                """)
resultado= cursor.fetchall()
print(f"PROPIETARIO Y SU DINERO GASTADO EN EL PARQUEADERO:")
for r in resultado:
    print(r)


conexion.close()