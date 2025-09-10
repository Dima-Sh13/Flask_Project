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


