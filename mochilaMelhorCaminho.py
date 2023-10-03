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

