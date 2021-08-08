# Simulador de Trading de Cripto

Objetivo é criar um robô para fazer 'trade' de cripto moedas em um ambiente 100% simulado. Características do simulador:
- Apenas 3 cripto disponíveis: BTCUSDT, ETHUSDT e DOGEUSDT
- Cada grupo recebe o equivalente a USD 10k em $$ virtual
- Não há incidência de nenhuma taxa por transação
- Apesar de todo o ambiente ser simulado (carteira, dinheiro etc), as cotações são acessadas em tempo real utilizando a API da binance.
- O trabalho pode ser realizado em qualquer linguagem

Para testes, usar o token = 'token_dummy_001' (conforme notebook exemplo). Para a operação 'pra valer', o professor irá passar tokens para cada grupo que devem ser utilizados para as operações.

Em caso de qualquer problema, favor entrar em contato!

## Descrição das rotas

No notebook "notebook_example.ipynb" você irá encontrar exemplos de como usar a API.

- available_cripto: Lista das cripto disponíveis
- cripto_quotation: retorna a cotação da cripto solicitada nos últimos minutos
- status: status da carteira: dinheiro, criptos e total (baseado na cotação atual das moedas)
- buy: compra cripto (quantidade de acordo com parâmetro 'quantity')
- sell: vende cripto (quantidade de acordo com valor 'quantity')
- history: retorna o histórico das operações de buy/sell

## Run Notebooks 

Para executar **0_exemplo_APIs**, clique aqui: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BernardoAflalo/cripto-simulator-client/blob/main/0_exemplo_APIs.ipynb)

Para executar **1_treino_simples**, clique aqui: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BernardoAflalo/cripto-simulator-client/blob/main/1_treino_simples.ipynb)

Para executar **2_my_robot**, clique aqui: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BernardoAflalo/cripto-simulator-client/blob/main/2_my_robot.ipynb)


## Download do histórico

Para realizar o treinamento dos modelos, o histórico das cripto moedas, minuto a minuto, estão disponíveis em:

- BTC: https://drive.google.com/u/0/uc?id=1K1-mXTk426z8ZvbmWrx8zrbC-C6GxxGg&export=download
- DOGE: https://drive.google.com/u/0/uc?id=17c2r9qbnsxPVxaYukrp6vhTY-CQy8WZa&export=download
- ETH: https://drive.google.com/u/0/uc?id=1b2nqwR11tWWZ8B1R3AXUB_iCuu1oELm6&export=download

## Exemplo de robô

Exemplo de robô simples, que a cada minuto checa a cotação do bitcoin, aplica um modelo dummy e envia ordens de compra ou venda

```
import time
def meu_modelo_linear_dummy(df):
  if random.randint(0,1) == 1:
    return 30
  else:
    return -30

def tratamento_df(df):
  return df.tail(1)
 
while True:
  df = api_post('cripto_quotation', {'token': token, 'ticker': 'BTCUSDT'})
  df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
  ## operacoes de feature eng. conforme o treinamento
  df_tratado = tratamento_df(df)
  tendencia = meu_modelo_linear_dummy(df_tratado)

  if tendencia > 0:
    payload = {'token': token,
              'ticker': 'BTCUSDT',
                'quantity': 1}

    api_post('buy', payload)
    print('buy')
  else:
      payload = {'token': token,
              'ticker': 'BTCUSDT',
                'quantity': 1}
      # ver se eu tenho bitcoin e, se tiver, vende
      api_post('sell', payload)
      print('sell')
  payload = {'token': token}
  print(api_post('status', payload))
  time.sleep(60)
```
