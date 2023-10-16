import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Carregue o arquivo Excel existente
base = pd.read_excel("Horas Sprint - Boty.xlsx")

# Plote os dados
plt.scatter(base["Horas Gastas"], base["Horas Planejadas"])
plt.xlabel("Horas Gastas")
plt.ylabel("Horas Planejadas")

# Crie um modelo de regressão linear
reg = linear_model.LinearRegression()
reg.fit(base["Horas Gastas"].values.reshape(-1, 1), base["Horas Planejadas"])

# Solicite ao usuário um valor de horas a serem gastas
user_input = input("Digite o valor de horas a serem gastas: ")
input_value = float(user_input) #Conversão do dado em float

# Faça a previsão com base no valor inserido pelo usuário
prediction = reg.predict([[input_value]])

# Plote o resultado
plt.scatter(base["Horas Gastas"], base["Horas Planejadas"])
plt.scatter(input_value, prediction[0], color="k")
x = np.array(base["Horas Gastas"])
y = reg.intercept_ + x * reg.coef_
plt.plot(x, y, "r")
plt.show()

print(f'A previsão para o valor inserido é: {prediction[0]} horas planejadas')

# Carregue o arquivo Excel resultante (se existir)
try:
    result_df = pd.read_excel("Horas_Sprint_Resultado.xlsx")
except FileNotFoundError:
    result_df = pd.DataFrame()

# Verifique se o valor já está presente no arquivo resultante
if input_value not in result_df["Horas Gastas"].values:
    # Crie um novo DataFrame com as informações de horas gastas e previsão de horas planejadas
    data = {'Horas Gastas': [input_value],
            'Horas Planejadas': [prediction[0]]}

    # Crie um DataFrame a partir do dicionário 'data'
    new_data = pd.DataFrame(data)

    # Concatene o novo DataFrame com o DataFrame resultante
    result_df = pd.concat([result_df, new_data], ignore_index=True)

    # Exporte o DataFrame atualizado para um arquivo Excel
    result_df.to_excel("Horas_Sprint_Resultado.xlsx", index=False)
