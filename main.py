from flask import Flask
#Inicializamos la variable app con Flask
app = Flask(__name__)

#Inicializamos parametros para el servidor de flsk
#set FLASK_APP=main.py

#comando para ejecutar el servidor
#flask --app main run

#comando para ejecutar el servidor en otro puerto
#flask --app main run -p 5002

#comando para ejecutar el servidor en modo debug
#flask --app main --debug run





@app.route("/hola")
def hello_World():
    return "Hola mundo Flask"


@app.route("/frutas")
def list_frutas():
    lista_frutas =["platano", "manzana", "fresa"]
    return lista_frutas

@app.route("/dic")
def list_dic():
    diccionarios = [{"pedro": "maria","Josua":"gringo"}]
    return diccionarios


#tomar parametro desde ruta
@app.route("/name/<name>")
def tu_nombre(name):
    return f"hola, {name}, como estas"

@app.route("/num/<parametro>")

def cuadrado(parametro):
    parametro = int(parametro)
    return f" el cuadrado de {parametro} es {parametro*parametro}"
 
"""
realizar una ruta que dinamicamente pueda solicitar o realizar operaciones de 
suma,resta,multiplicacion y division segun 2 parametros numericos recibidos
"""

@app.route("/suma/<num1>/<num2>")
def suma(num1,num2):
    num1= int(num1)
    num2= int(num2)
    result = num1 + num2
    return str(result)


def operaciones_matematicas(num1, num2):
    suma = num1 + num2
    resta = num1- num2
    mult = num1 * num2
    div = num1/ num2
    return f"Suma: {suma}, Resta: {resta}, Multiplicacion: {mult}, Division: {div}"

@app.route("/mates/<int:num1>/<int:num2>/<ope>")
def mat_ope(num1, num2, ope):
    
    answer = 0
    if ope == "suma":
        answer= f"La solucion es {num1 + num2}"
    elif ope == "resta":
         answer= f"La solucion es {num1 - num2}"
    elif ope == "multiplicacion":
         answer= f"La solucion es {num1 * num2}"
    elif ope == "division":
         answer= f"La solucion es {num1 / num2}"

    return answer      
