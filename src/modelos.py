class Deteccao:
    
    def __init__(self,classe_id : int,x_min: int,y_min: int,x_max: int,y_max: int):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        
    def desenhar(self, imagem):
        pass

class ImagemAnotada:
    
    def __init__(self, pthImagem : str, listDeteccoes : list):
        self.pthImagem = pthImagem
        self.listDeteccoes = listDeteccoes
    
    def adicionaDeteccao(self,det):
        self.listDeteccoes.append(det)
        
    def gerarImagem(self):
        pass
    