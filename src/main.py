#Autor: Daniel Birenbaum Guerrieri de Castro
#Github: https://github.com/danielbirenbaum

from modelos import Deteccao
from modelos import ImagemAnotada
from arquivos import lerDados
from arquivos import tratarDados
from pathlib import Path
import cv2


def main():
    try:
        
        dados = lerDados("./dados/anotacoes.csv")
        dadosTratados = tratarDados(dados) #lista de listas com números inteiros para os campos correspondentes
        #print(dadosTratados)
        
        pasta_imagens = Path("./imagens")
        
        keepItarating = True
        #Itera sob todos os arquivos de imagens
        for paths in sorted(pasta_imagens.iterdir()):
            
            cenaAtualNome = paths.name # cena alvo para buscar em dadosTratados
            
            imgAntd = ImagemAnotada(paths)
            
            #Itera sob todos os possíveis quadrados a serem desenhados
            for indexador in dadosTratados:
                
                if (indexador[0] == cenaAtualNome):
                    imgAntd.adicionaDeteccao(Deteccao(indexador[1],indexador[2],indexador[3],indexador[4],indexador[5]))
            
            imgFinal = imgAntd.gerarImagem()
            cv2.imshow(cenaAtualNome, imgFinal)
            print("#######################")
            print(f"Nome da imagem: {cenaAtualNome}")
            print(f"Quantidade de caixas: {len(imgAntd.listDeteccoes)}")
            
            while True:
                tecla = cv2.waitKey(0)
                
                if tecla == ord(' '):  
                    cv2.imwrite(f"./resultados/{cenaAtualNome}",imgFinal)
                    break 
                    
                elif tecla == ord('q'):
                    #Destrói todas as imagens mostrada, indica para parar o loop de analisar novas imagens
                    cv2.imwrite(f"./resultados/{cenaAtualNome}",imgFinal)
                    cv2.destroyAllWindows()
                    keepItarating = False
                    break
                
            if not(keepItarating):
                break
    
    except Exception as e:
        print(f"ERRO main(): {e}")


if __name__ == "__main__":
    main()
