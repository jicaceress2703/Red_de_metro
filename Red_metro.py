import csv
from optparse import Values
def ruta(origen,destino,red_trans,**kwarg):
    red_trans=red()
    origen_aux=origen
    count=red_trans.estaciones().find(origen_aux)
    rutas=[]
    for i in red_trans.estacionAd()[count]:
        


class red:
    def __init__(self,archivo):
        self.archivo=archivo
        self.puntos=[]
        self.colores=[]
        self.adyacentes=[]
    
    def estaciones(self):
        for lista in self.archivo:
            self.puntos.append(lista[0])
        return self.puntos

    def colorEstacion(self):
        for lista in self.archivo:
            self.colores.append(lista[1])
        return self.colores

    def estacionAd(self):
        for lista in self.archivo:
            self.adyacentes.append(lista[2])
        return self.adyacentes
    

red_transporte=list()

with open('red.csv') as red_tren:
    reader= csv.reader(red_tren)
    next(reader)
    for rows in reader:
        red_transporte.append(rows)





