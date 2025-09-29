# Relatório do T1

Este trabalho foi desenvolvido por Vinícius Fontoura - GRR20206873.

## Introdução

Foram implementadas as funções indicadas no enunciado do trabalho. Alguns detalhes de implementação precisaram ser ajustados para que o código funcionasse corretamente (Vou detalhar mais adiante). 

Os resultados ficaram próximos aos indicados no enunciado, como esperando.

## Implementação

Algumas bibliotecas precisam ser importadas para que o código funcione corretamente.

Devido à atualizações do python, é necessário criar um ambiente virtual e instalar as bibliotecas indicadas no arquivo `requirements.txt`.

```python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Com isso, o código pode ser executado com:

```python
python ex1.py
python ex1_multi.py
```

### Função Descontinuada

O método `figure.gca(projection='3d')` utilizado para criar gráficos 3D foi descontinuado nas versões mais recentes do Matplotlib. Por isso, foi necessário utilizar `figure.add_subplot(111, projection='3d')` para criar os gráficos 3D. A alteração foi na linha 85 do arquivo `ex1_multi.py`.

### Arquivo normalEqn.py

No arquivo `ex1_multi.py`, a "parte 3" fala sobre implementar a função `normal_eqn(X, y)`, no arquivo `normalEqn.py`. Porém, esse arquivo não existe nos arquivos fornecidos. Por isso, criei o arquivo `normalEqn.py` e implementei a função conforme o enunciado.

## Conclusão

Após implementadas as funções, os resultados ficaram próximos aos indicados no enunciado.

### Alpha testado

Para a parte 2 do `ex1_multi.py`, o valor de alpha que apresentou o melhor resultado foi 0.1, com 400 iterações.

### Predição do preço para uma casa de 1650 sq-ft e 3 quartos

Para predizer o preço de uma nova entrada, utilizamos o método de predição com os parâmetros obtidos pelo gradiente descendente e pela equação normal.
O preço predito para uma casa de 1650 sq-ft e 3 quartos foi:

- Usando Gradiente Descendente (400 iterações): 293081.465
- Usando Equação Normal: 293081.464

O que é práticamente o mesmo valor, como esperado.
