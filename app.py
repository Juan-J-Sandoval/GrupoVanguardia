from flask import Flask, render_template, request
import json, time, modelos
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    url = 'https://www.google.com.mx'
    nombre = ''
    if request.method == 'POST':
        url = request.form['urlOculta']
        nombre = request.form['nombre']
        satis = request.form['satis']
        comen = request.form['comen']
        uno = request.form['uno']
        dos = request.form['dos']
        tres = request.form['tres']
        cuatro = request.form['cuatro']
        chatbot = modelos.Resultados(nombre, satis, comen, uno, dos, tres, cuatro, time.strftime("%x"), time.strftime("%X"))
        chatbot.guardarDatos()
        #print(chatbot.datos)
    return render_template('index.html', url = url, nombre = nombre)

@app.route('/consultas')
def consultas():
    return render_template('consulDatos.html')


@app.route('/req', methods=['GET'])
def req():
    nombre = request.args.get('nombre')
    boton = request.args.get('boton')
    chatbot = modelos.Consultas(nombre)
    if boton == "datos":
        datotabla = chatbot.datos
        return json.dumps(datotabla)
    elif boton == "esta":
        dato = chatbot.estadistica()
        return dato


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070, debug=True)

#http://0.0.0.0:8070/consultas
