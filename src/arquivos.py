import csv
from modelos import Deteccao

#Retorna uma lista de listas com cada row do csv (todas as informações possíves do csv)
def lerDados(pth : str):
    try:
        
        with open(pth, mode='r', newline='', encoding='utf-8') as d:
            data = csv.reader(d, delimiter=',')
            next(data)
            return list(data)
                
    except FileNotFoundError:
        print(f"ERRO lerDados(): Arquivo {pth} não encontrado.")
        raise
    
    except Exception as e:
        print(f"ERRO lerDados(): {e}.")
        raise
    
# Tratará a lista de listas do csv para a criação das instâncias    
# Usa o argumento referência para verificar com os dados de mapeamento_imagens.csv
def tratarDados(dados : list, pthReferencia):
    try:
        
        ref = lerDados(pthReferencia) #lista de listas com o mapeamento
        #Dicionário do tipo -> cena_0x : (largura,altura)
        dictValores = {}
        for row in ref:
            dictValores[row[0]] = (int(row[2]),int(row[3]))
        
        dadosTratados = []
        for row in dados:
            dadosTratados.append([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5])])
            #(classe_id,x_min,y_min,x_max,y_max)
            
            #Verificação dos dados
            #Classe ID
            if (int(row[1]) not in [0,1]):
                raise Exception("Classe ID só pode ser 0 ou 1")
            #x_min
            if (not(int(row[2]) >= 0 and int(row[4]) >= int(row[2]))):
                raise Exception("x_min não pode ser menor que 0 ou x_min não pode ser maior que x_max")
            #y_min
            if (not(int(row[3]) >= 0 and int(row[5]) >= int(row[3]))):
                raise Exception("y_min não pode ser menor que 0 ou y_min não pode ser maior que y_max")
            #y_max e x_max para altura e largura
            if (int(row[5]) > dictValores[row[0]][1] or int(row[4]) > dictValores[row[0]][0]):
                raise Exception("x_max ou y_max não podem ser maior que a largura nem altura das imagens reespectivamente")
                 
        return dadosTratados
    
    except Exception as e:
        print(f"ERRO tratarDados(): {e}.")
        raise