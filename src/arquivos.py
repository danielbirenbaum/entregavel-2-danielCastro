import csv

def lerDados(pth : str):
    try:
        
        with open(pth, mode='r', newline='', encoding='utf-8') as d:
            data = csv.reader(d, delimiter=',')
            next(data)
            return list(data)
                
    except FileNotFoundError:
        print(f"Arquivo {pth} não encontrado.")
            
def tratarDados(dados : list):
    pass