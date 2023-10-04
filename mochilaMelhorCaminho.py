import openpyxl

tabCidade= './planilhas/cidades.xlsx'
tabArestas = './planilha/arestas.xlsx'

cidade = openpyxl.load_workbook(tabCidade)
arestas = openpyxl.load_workbook(tabArestas)

class Aresta:
    def __init__(self, origem, destino, distancia):
        self.origem=origem
        self.destino=destino
        self.distancia=distancia
        
    def obterDestino(self):
        return self.destino
    
    def obterDistancia(self):
        return self.distancia
    
    def obterOrigem(self):
        return self.origem

class pedido:
    def __init__(self, valor, destino, peso):
        self.valor= valor
        self.destino=destino
        self.peso=peso  
        
    
class carga:
    def __init__(self, maxPeso,valor) :
        self.peso=maxPeso
        self.valor-valor


class cidade:
    def __init__(self) -> None:
        
    
    
class caminhoMinimo:
    def __init__(self):
        pass