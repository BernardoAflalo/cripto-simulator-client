# Para rodar os notebooks

- 0_exemplo_API: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BernardoAflalo/cripto-simulator-client/blob/main/0_exemplo_APIs.ipynb)

- 1_Treino Simples: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BernardoAflalo/cripto-simulator-client/blob/main/1_treino_simples.ipynb)

- 2 My Robot: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BernardoAflalo/cripto-simulator-client/blob/main/2_my_robot.ipynb)


# Simulador de Trading de Cripto

Objetivo é criar um robô para fazer 'trade' de cripto moedas em um ambiente 100% simulado. Características do simulador:
- Apenas 1 cripto disponível: BTC
- Cada grupo/ pessoa recebe o equivalente a USD 10k em $$ virtual
- Não há incidência de nenhuma taxa por transação
- Apesar de todo o ambiente ser simulado (carteira, dinheiro etc), as cotações são reais, mas defasadas em alguns dias
- O trabalho pode ser realizado em qualquer linguagem

## Tokens

Para testes, usar o token = 'token_dummy_001' (conforme notebook exemplo).

Cada grupo receberá o token oficial que devem utilizar para comprar e vender cripto.

## Notebooks

### 0_exemplo_APIs.ipynb

Você irá encontrar exemplos de como usar a API.

- available_cripto: Lista das cripto disponíveis
- cripto_quotation: retorna a cotação da cripto solicitada nos últimos minutos
- status: status da carteira: dinheiro, criptos e total (baseado na cotação atual das moedas)
- buy: compra cripto (quantidade de acordo com parâmetro 'quantity')
- sell: vende cripto (quantidade de acordo com valor 'quantity')
- history: retorna o histórico das operações de buy/sell

Fique à vontade para utilizar o token_dummy_001, mas o trabalho só é contabilizado quando fizerem as operações com o próprio token gerado conforme anteriormente!

### 1_treino_simples.ipynb

Exemplo de como fazer o download dos dados e criar um modelo simples inicial, utilizando:

- Variável dependente: a diferença percentual da média dos próximos 10min com o minuto atual;
- Variável independente: variáveis lagadas, médias móveis, cruzamento de média móveis e um contador de tempo

Toda a parte de engenharia de features está contida no arquivo 'feature_eng.py'. Ao final, um arquivo 'pickle' com o modelo é gerado, para ser utilizado na próxima etapa da construção do robô.

### 2_my_robot.ipynb

Exemplo simples de robô utilizando o 'pickle' gerado anteriormente. A lógica implementada é:

1. Confere o preço do ativo
2. Realiza a engenharia de feature
3. Filtra os valores mais recente de preço e features
4. Aplica o modelo, prevendo a probabilidade do preço subir ou cair nos próximos minutos
5. Calcula a quantidade de moedas a ser comprada/ vendida
6. Se a tendência for positiva e acima de um limite, reajusta quantidade comprada pela quantidade de $$ em conta e realiza a compra. Se for negativa, realiza a venda de maneira similar, conferindo qual a posição atual do ativo
7. Retorna o status da carteira e espera 60 segundos para a próxima iteração


## Download do histórico

Para realizar o treinamento dos modelos, o histórico das cripto moedas, minuto a minuto, estão disponíveis em:

- BTC: https://drive.google.com/u/0/uc?id=1K1-mXTk426z8ZvbmWrx8zrbC-C6GxxGg&export=download

Atenção: os dados de treinamento estão defasados, pois é uma foto de cotações passadas.
