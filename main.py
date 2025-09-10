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
#flsk --app main --debug run





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
 
