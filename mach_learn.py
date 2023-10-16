import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

base = pd.read_excel("Horas Sprint - Boty.xlsx")

plt.scatter(base["Horas Planejadas"], base["Horas Gastas"])

# Adicione títulos aos eixos X e Y
plt.xlabel("Horas Planejadas")  # Título do eixo X
plt.ylabel("Horas Gastas")  # Título do eixo Y

reg = linear_model.LinearRegression()

reg.fit(base["Horas Planejadas"].values.reshape(-1, 1), base["Horas Gastas"])

user_input = input("Digite o valor de horas a serem planejadas: ")
input_value = float(user_input)  # Converte a entrada do usuário em um dado do tipo float

# Faça a previsão usando o modelo treinado com o valor inserido pelo usuário
prediction = reg.predict([[input_value]])

plt.scatter(base["Horas Planejadas"], base["Horas Gastas"])
plt.scatter(input_value, prediction[0], color="k")
x = np.array(base["Horas Planejadas"])
y = reg.intercept_ + x * reg.coef_
plt.plot(x, y, "r")
plt.show()

print(f'A previsão para o valor inserido é: {prediction[0]} horas gastas')