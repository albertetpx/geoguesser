import mysql.connector as mysql
import random

# Funciones de usuario
def pedirListaBD():
    bd = mysql.connect(user="skriwelae",password="claumestra",host="skriwelae.mysql.pythonanywhere-services.com", database="skriwelae$world")
    cursor = bd.cursor()
    query = "select name from country;"
    cursor.execute(query)
    listaPaises = cursor.fetchall()
    bd.close()
    return listaPaises

def seleccionarPaisRandom():
    listaPaises = pedirListaBD()            #listaPaises es una lista de tuplas
    paisRandom = random.choice(listaPaises) #paisRandom es una tupla de una posición
    return paisRandom[0]

def comprobarCapital(pais,capitalUsuario):
    bd = mysql.connect(user="skriwelae",password="claumestra",host="skriwelae.mysql.pythonanywhere-services.com", database="skriwelae$world")
    cursor = bd.cursor()
    query = f"select ct.name from country c join city ct on c.capital=ct.id where c.name='{pais}';"
    cursor.execute(query)
    capitalOK = cursor.fetchall()[0][0]
    bd.close()
    #Comprobamos si la capital es correcta
    if capitalUsuario == capitalOK:
        return True, capitalOK
    else:
        return False, capitalOK