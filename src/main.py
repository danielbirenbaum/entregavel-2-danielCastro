#Autor: Daniel Birenbaum Guerrieri de Castro
#Github: https://github.com/danielbirenbaum

from modelos import Deteccao
from modelos import ImagemAnotada
from arquivos import lerDados
from arquivos import tratarDados
import cv2


def main():
    try:
        
        dados = lerDados("./dados/anotacoes.csv")
        dadosTratados = tratarDados(dados) #lista de listas com números inteiros para os campos correspondentes
        
    
            
            
            
        
    
    except Exception as e:
        print(f"ERRO main(): {e}")


if __name__ == "__main__":
    main()
