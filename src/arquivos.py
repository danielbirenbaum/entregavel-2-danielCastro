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
def tratarDados(dados : list):
    try:
        
        dadosTratados = []
        for row in dados:
            dadosTratados.append([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5])])
        return dadosTratados
    
    except Exception as e:
        print(f"ERRO tratarDados(): {e}.")
        raise