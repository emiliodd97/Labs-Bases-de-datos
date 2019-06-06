#Universidad del Valle
#Emilio Diaz
#15316

from pprint import pprint
import psycopg2
from psycopg2 import Error

'''
	Laboratorio 8 
'''
password_ = input("Ingrese su Contrasena postgres: ")


def inicio_Transaccion():
    trans = psycopg2.connect(user="postgres", password=password_, host="127.0.0.1", port="5432",
                             database="esquemaEquipos")
    return trans


def incisoA():
    trans = inicio_Transaccion()
    trans.autocommit = False
    CPU = input("Ingrese la Velocidad del RAM ")
    RAM = input("Ingrese el tamano de RAM: ")
    query = '''
    SELECT "modelo", "precio"
	FROM public."PC"
	WHERE "PC"."velocidad" = ''' + str(CPU) + ''' 
	AND "PC"."ram" = ''' + str(RAM) + ''';'''
    try:
        cursor = trans.cursor()
        cursor.execute(query)
        Result = cursor.fetchall()
        trans.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        Result = ("ERROR en transaccion, se revertiran todas las operaciones anteriores ", error)
        trans.rollback()
    finally:
        if (trans):
            cursor.close()
            trans.close()
            return Result


def incisoB():
    trans = inicio_Transaccion()
    trans.autocommit = False
    Model = input("Ingrese el nombre del Modelo: ")
    query = '''
    DELETE FROM public."PC" 
    WHERE "PC"."modelo" = \'''' + Model + '''\'; 
    '''
    query2 = '''
    DELETE FROM public."Producto" 
    WHERE "Producto"."modelo" = \'''' + Model + '''\'; '''

    try:
        cursor = trans.cursor()
        cursor.execute(query)
        Result = cursor.statusmessage
        cursor.execute(query2)
        Result = Result + " || " + (cursor.statusmessage)
        trans.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        Result = ("ERROR en transaccion, se revertiran todas las operaciones anteriores", error)
        trans.rollback()
    finally:
        if (trans):
            cursor.close()
            trans.close()
            return Result


def incisoC():
    trans = inicio_Transaccion()
    trans.autocommit = False
    Model = input("Ingrese el Modelo: ")
    query = ''' 
    UPDATE public."PC"
	SET "precio" = "precio"-100
	WHERE "modelo" = \'''' + Model + '''\';'''
    try:
        cursor = trans.cursor()
        cursor.execute(query)
        Result = cursor.statusmessage
        trans.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        Result = ("ERROR en transaccion, se revertiran todas las operaciones anteriores ", error)
        trans.rollback()
    finally:
        if (trans):
            cursor.close()
            trans.close()
            return Result


def incisoD():
    trans = inicio_Transaccion()
    trans.autocommit = False
    Fabricante = input("Ingrese el Fabricante: ")
    Model = input("Ingrese el Modelo: ")
    Speed = input("Ingrese la Velocidad: ")
    RAM = input("Ingrese el tamano de RAM: ")
    Drive = input("Ingrese tamano de Disco: ")
    Price = input("Ingrese el precio: ")

    query = '''
			SELECT *
			FROM "public"."PC" INNER JOIN "public"."Producto"
			ON "PC"."modelo" = "Producto"."modelo"
			WHERE "Producto"."fabricante" = \'''' + Fabricante + '''\'
			AND "Producto"."modelo" = \'''' + Model + '''\'
			AND "PC"."velocidad" = ''' + Speed + '''
			AND "PC"."ram" = ''' + RAM + '''
			AND "PC"."disco duro" = ''' + Drive + '''
			AND "PC"."precio" = ''' + Price + '''
            '''
    try:
        cursor = trans.cursor()
        cursor.execute(query)
        Result = cursor.fetchall()
        if len(Result) > 0:
            Result = "ERROR, ya existe la informacion solicitada en la tabla PC"
        else:
            InsertQueryProducto = '''
		INSERT INTO public."Producto"("fabricante", "modelo", "tipo")
		VALUES (\'''' + Fabricante + '''\', \'''' + Model + '''\', 'PC');
		'''
            cursor.execute(InsertQueryProducto)
            insertPC = '''
		INSERT INTO public."PC"("modelo", "velocidad", "ram", "disco duro", "precio")
		VALUES (\'''' + Model + '''\', ''' + Speed + ''', ''' + RAM + ''', ''' + Drive + ''', ''' + Price + ''');
		'''
            cursor.execute(insertPC)
            Result = "Se ha agregado una computadora exitosamente "

        trans.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        Result = ("ERROR en transaccion, se revertiran todas las operaciones anteriores ", error)
        trans.rollback()
    finally:
        if (trans):
            cursor.close()
            trans.close()
            return Result


if __name__ == '__main__':

    opt = int(input("Ingresar numero de inciso: "))
    if opt == 1:
        pprint(incisoA())
    elif opt == 2:
        print(incisoB())
    elif opt == 3:
        print(incisoC())
    elif opt == 4:
        print(incisoD())
    else:
        print("Inciso invalido")
