
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

sns.lineplot(data=df, x='dia', y='venda', marker='o')
plt.title('Preço Médio da Gasolina em SP - 1 a 10 de Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.tight_layout()
plt.savefig('gasolina.png')
plt.show()
