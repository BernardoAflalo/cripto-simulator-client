import numpy as np
import pandas as pd
import requests
import statsmodels.api as sm
import math
import pickle
import time

urlbase = 'https://mighty-bastion-45199.herokuapp.com/'


def get_result(x):
    try:
        result = pd.DataFrame.from_dict(x.json())
    except:
        result = x.text
    return result

def api_post(route, payload):
    url = urlbase + route
    x = requests.post(url, data = payload)
    df = get_result(x)
    if type(df) == pd.core.frame.DataFrame:
        if 'datetime' in df.columns:
            df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
	
    return df

def api_get(route):
    url = urlbase + route
    x = requests.get(url)
    df = get_result(x)
    return df

def compute_quantity(coin_value, invest_value, significant_digits):
    a_number = invest_value/coin_value
    rounded_number =  round(a_number, significant_digits - int(math.floor(math.log10(abs(a_number)))) - 1)
    return rounded_number.iloc[0]

def how_much_i_have(ticker, token):
    status = api_post('status', payload = {'token': token})
    status_this_coin = status.query(f"ticker == '{ticker}'")
    if status_this_coin.shape[0] > 0:
        return status_this_coin['quantity'].iloc[0]
    else:
        return 0

def feature_eng(df):
    # Duas variáveis lagged percentual:
    df['lag_1']= 100*df['close'].diff(1)/df['close']
    df['lag_2']= 100*df['close'].diff(2)/df['close']

    # Moving averages e razões entre elas
    df['ma_10']= df['close'].rolling(10).mean()
    df['ma_30']= df['close'].rolling(30).mean()
    df['ratio_ma'] = df['ma_10']/df['ma_30']

    # Um contador de minutos desde o início da série
    df['time']=(df['datetime'].astype(np.int64)/6e10).astype(int)
    cols2drop = set(['symbol', 'datetime', 'close_time', 'open', 'high', 'low', 'forward_average']).intersection(set(df.columns))
    df = df.drop(columns=cols2drop)
    df = df.dropna()
    df['time'] = df['time']-26038829
    df = sm.add_constant(df)
    return df
	
def my_robot(tempo, token):
    model = pickle.load(open('model_dummy.pickle', 'rb'))
    ticker = 'DOGEUSDT'
    count_iter = 0
    valor_compra_venda = 10
    
    while count_iter < tempo:
        
       
        # Pegando o OHLC dos últimos 500 minutos
        df = api_post('cripto_quotation', {'token': token, 'ticker': ticker})

        # Realizando a engenharia de features
        df = feature_eng(df)

        # Isolando a linha mais recente
        df_last = df.iloc[[np.argmax(df['time'])]]

        # Calculando tendência, baseada no modelo linear criado
        tendencia = model.predict(df_last).iloc[0]

        # A quantidade de cripto que será comprada/ vendida depende do valor_compra_venda e da cotação atual
        qtdade = compute_quantity(coin_value = df_last['close'], invest_value = valor_compra_venda, significant_digits = 2)

        # Print do datetime atual
        print('-------------------')
        print(f"@{pd.to_datetime('now')}")

        if tendencia > 0.02:
            # Modelo detectou uma tendência positiva
            print(f"Tendência positiva de {str(tendencia)}")

            # Verifica quanto dinheiro tem em caixa
            qtdade_money = how_much_i_have('money', token)

            if qtdade_money>0:
                # Se tem dinheiro, tenta comprar o equivalente a qtdade ou o máximo que o dinheiro permitir
                max_qtdade = compute_quantity(coin_value = df_last['close'], invest_value = qtdade_money, significant_digits = 2)
                qtdade = min(qtdade, max_qtdade)

                # Realizando a compra
                print(f'Comprando {str(qtdade)} {ticker}')
                api_post('buy', payload = {'token': token, 'ticker': ticker, 'quantity': qtdade})

        elif tendencia < -0.02:
            # Modelo detectou uma tendência negativa
            print(f"Tendência negativa de {str(tendencia)}")

            # Verifica quanto tem da moeda em caixa
            qtdade_coin = how_much_i_have(ticker, token)

            if qtdade_coin>0:
                # Se tenho a moeda, vou vender!
                qtdade = min(qtdade_coin, qtdade)
                print(f'Vendendo {str(qtdade)} {ticker}')
                api_post('sell', payload = {'token': token, 'ticker': ticker, 'quantity':qtdade})
        else:
            # Não faz nenhuma ação, espera próximo loop
            print(f"Tendência neutra de {str(tendencia)}. Nenhuma ação realizada")

        # Print do status após cada iteração
        print(api_post('status', payload = {'token': token}))       
        count_iter +=1
        time.sleep(60)