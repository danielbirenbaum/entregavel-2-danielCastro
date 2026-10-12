# Segundo trabalho entregável para o processo seletivo da UFRJ Harpea

Escrito e desenvolvido por *Daniel Castro* como trabalho para o p.s da UFRJ Harpea

## Preparação do ambiente

Esse projeto utiliza o gerenciador de pacotes uv, pois é um gerenciador de pacotes extremamente rápido

* Instale o gerenciador de pacotes uv (Linux/MacOS):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

* Ou para Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Mais informações podem ser obtidas no site oficial do gerenciador de pacotes [`uv`](https://docs.astral.sh/uv/getting-started/installation/)

## Dependências 
Esse projeto utiliza o [`numpy`](https://numpy.org/) e o [`OpenCV`](https://opencv.org/) como bibliotecas intrínsicas. Utilizando o pacote [`uv`](https://docs.astral.sh/uv/getting-started/installation/) é fácil garantir que elas estejam instaladas no ambiente virtual.
## Usando o projeto

* Copie o projeto via git clone:

```bash
git clone https://github.com/danielbirenbaum/entregavel-2-danielCastro.git
```

* Sincronize o projeto

```bash
uv sync
```

* Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

* Execute o programa principal:

```bash
uv run src/main.py
```

Capturas do drone aparecerão na tela, podendo dar dois comandos:

Pressione <kbd>Space</kbd>para avançar a página e <kbd>q</kbd> para sair.

## Funcionamento de [`modelos.py`](src/modelos.py)

| Classe         | Funcionalidade | 
| :--------------| :--------: | 
| Deteccao       |     Guarda dados referentes à classe_id, x_min,y_min, x_max, y_max. Refere-se a uma única deteccção, ou seja, uma bounding box|     
| ImagemAnotada  |     Guarda dados referentes à uma cena. Ou seja, representa uma imagem com várias deteccoes.      |     
 
