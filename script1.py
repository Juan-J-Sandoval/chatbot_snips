import io, json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_ES

#creación del motor para entrenamiento y posteriormente analizar los nuevos datos.
# Se le manda como parámetro la configuración del idioma
motor = SnipsNLUEngine(config=CONFIG_ES)

#Extracción de los datos de entrenamiento, intenciones y entidades 
with io.open("datoset.json") as f:
    dataset = json.load(f)

#Se le pasan los datos en formato JSON para su entrenamiento
motor.fit(dataset)

#Se pasa la nueva intención al motor para saber si su entrenamiento funcionó
parseo=motor.parse(u"Que clima hará mañana en Burgos de Osma?")
#Se imprimen los resultados en formato JSON
print(json.dumps(parseo, indent=2))