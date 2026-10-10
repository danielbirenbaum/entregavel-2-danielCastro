import cv2

class Deteccao:
    
    def __init__(self,classe_id : int,x_min: int,y_min: int,x_max: int,y_max: int):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        
    def desenhar(self, imagem):
        if self.classe_id == 0:
            cv2.rectangle(imagem, (self.x_max,self.y_max),(self.x_min,self.y_min), (0, 255, 0), 1)
        else:
            cv2.rectangle(imagem, (self.x_max,self.y_max),(self.x_min,self.y_min), (0, 0, 255), 1)

class ImagemAnotada:
    
    def __init__(self, pthImagem , listDeteccoes : list = []):
        self.pthImagem = pthImagem
        self.listDeteccoes = listDeteccoes
    
    def adicionaDeteccao(self, det : Deteccao):
        self.listDeteccoes.append(det)
        
    def gerarImagem(self):
        imagem = cv2.imread(self.pthImagem)
        
        for deteccao in self.listDeteccoes:
            deteccao.desenhar(imagem)
        
        return imagem  