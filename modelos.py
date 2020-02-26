import json

class Resultados:
    def __init__(self, nombre, satis, comen, uno, dos, tres, cuatro, fecha, hora):
        """Constructor de clase Resultados"""
        self.nombre = nombre
        self.satis = satis
        self.comen = comen
        self.uno = uno
        self.dos = dos
        self.tres = tres
        self.cuatro = cuatro
        self.fecha = fecha
        self.hora = hora
        self.datos= {}

    def guardarDatos(self):
        if self.nombre == "Sepomex":
            archivo = open('static/archivo/sepomex.json')
            self.datos = json.load(archivo)
            self.datos['baseDeIncidencias'].append({
            self.satis:{
                'comentario': self.comen,
                'Usuario': self.uno,
                'Bot': self.dos,
                'usuario': self.tres,
                'bot': self.cuatro,
                'fecha': self.fecha,
                'hora': self.hora
                }
            })
            with open('static/archivo/sepomex.json', 'w') as file:
                json.dump(self.datos, file, indent=2)
        elif self.nombre == "Sepomex T":
            archivo = open('static/archivo/sepomext.json')
            self.datos = json.load(archivo)
            self.datos['baseDeIncidencias'].append({
            self.satis:{
                'comentario': self.comen,
                'Usuario': self.uno,
                'Bot': self.dos,
                'usuario': self.tres,
                'bot': self.cuatro,
                'fecha': self.fecha,
                'hora': self.hora
                }
            })
            with open('static/archivo/sepomext.json', 'w') as file:
                json.dump(self.datos, file, indent=2)
        elif self.nombre == "Grupo Vanguardia":
            archivo = open('static/archivo/grupovanguardia.json')
            self.datos = json.load(archivo)
            self.datos['baseDeIncidencias'].append({
            self.satis:{
                'comentario': self.comen,
                'Usuario': self.uno,
                'Bot': self.dos,
                'usuario': self.tres,
                'bot': self.cuatro,
                'fecha': self.fecha,
                'hora': self.hora
                }
            })
            with open('static/archivo/grupovanguardia.json', 'w') as file:
                json.dump(self.datos, file, indent=2)
        elif self.nombre == "Grupo Vanguardia T":
            archivo = open('static/archivo/grupovanguardiat.json')
            self.datos = json.load(archivo)
            self.datos['baseDeIncidencias'].append({
            self.satis:{
                'comentario': self.comen,
                'Usuario': self.uno,
                'Bot': self.dos,
                'usuario': self.tres,
                'bot': self.cuatro,
                'fecha': self.fecha,
                'hora': self.hora
                }
            })
            with open('static/archivo/grupovanguardiat.json', 'w') as file:
                json.dump(self.datos, file, indent=2)
        return

class Consultas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}
        if self.nombre == "Sepomex":
            archivo = open('static/archivo/sepomex.json')
            self.datos = json.load(archivo)
        elif self.nombre == "Sepomex T":
            archivo = open('static/archivo/sepomext.json')
            self.datos = json.load(archivo)
        elif self.nombre == "Grupo Vanguardia":
            archivo = open('static/archivo/grupovanguardia.json')
            self.datos = json.load(archivo)
        elif self.nombre == "Grupo Vanguardia T":
            archivo = open('static/archivo/grupovanguardiat.json')
            self.datos = json.load(archivo)
    
    def estadistica(self):
        falsos = 0
        verdadero = 0
        error = 0
        acerto = 0
        total = len(self.datos["baseDeIncidencias"])
        for llave in self.datos["baseDeIncidencias"]:
            if list(llave)[0] == 'false':
                falsos += 1
            elif list(llave)[0] == 'true':
                verdadero += 1
        error = (falsos*100)/total
        error = round(error)
        acerto = (verdadero*100)/total
        acerto = round(acerto)
        resultados = {"acerto": acerto, "erro": error}
        return resultados
        
