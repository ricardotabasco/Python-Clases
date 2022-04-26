monitoreo={"m2": "mayo", "m3":"monica", "m4":"aurora", "m5": "zaid"}
monitoreo["m6"]="ramiro" #agrega un elemento con su clave
monitoreo["m7"]="eder"
monitoreo["m5"]="jiram" #corrije un elemento
print(monitoreo)
del monitoreo["m6"] #elimina un valor del diccionario
print(monitoreo["m4"]) #para acceder al valor de una clave
print(monitoreo.keys()) #imprime todas las claves de un diccionario
print(monitoreo.values()) #imprime todos los valores de un diccionario
print(monitoreo)