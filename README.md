# Simulador de Trading de Cripto

Objetivo é criar um robô para fazer 'trade' de cripto moedas em um ambiente 100% simulado. Características do simulador:
- Apenas 3 cripto disponíveis: BTCUSDT, ETHUSDT e DOGEUSDT
- Cada grupo/ pessoa recebe o equivalente a USD 10k em $$ virtual
- Não há incidência de nenhuma taxa por transação
- Apesar de todo o ambiente ser simulado (carteira, dinheiro etc), as cotações são reais, pois o servidor acessa uma API em tempo real
- O trabalho pode ser realizado em qualquer linguagem

Para testes, usar o token = 'token_dummy_001' (conforme notebook exemplo). Para o projeto final, o aluno deve cadastrar o próprio robô no site https://cripto-dash.herokuapp.com/ preenchendo:
- Nome: nome do aluno, no caso de trabalho individuais ou provas substitutivas. No caso de trabalho em grupo, o nome do grupo
- Descrição do bot (opcional)
- Imagem do robô (opcional)
- Escolha de onde você é (qual curso/ empresa)

Na sequência, clicar em "Gerar Token" e copiar o token que aparecerá na tela! Ele será necessário para as chamadas de API.

Em caso de qualquer problema, favor entrar em contato!

## Descrição das rotas

No notebook "notebook_example.ipynb" você irá encontrar exemplos de como usar a API.

- available_cripto: Lista das cripto disponíveis
- cripto_quotation: retorna a cotação da cripto solicitada nos últimos minutos
- status: status da carteira: dinheiro, criptos e total (baseado na cotação atual das moedas)
- buy: compra cripto (quantidade de acordo com parâmetro 'quantity')
- sell: vende cripto (quantidade de acordo com valor 'quantity')
- history: retorna o histórico das operações de buy/sell



## Download do histórico

Para realizar o treinamento dos modelos, o histórico das cripto moedas, minuto a minuto, estão disponíveis em:

- BTC: https://drive.google.com/u/0/uc?id=1K1-mXTk426z8ZvbmWrx8zrbC-C6GxxGg&export=download
- DOGE: https://drive.google.com/u/0/uc?id=17c2r9qbnsxPVxaYukrp6vhTY-CQy8WZa&export=download
- ETH: https://drive.google.com/u/0/uc?id=1b2nqwR11tWWZ8B1R3AXUB_iCuu1oELm6&export=download
