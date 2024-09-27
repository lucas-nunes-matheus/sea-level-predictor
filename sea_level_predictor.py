import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Ler dados do arquivo
    df = pd.read_csv("epa-sea-level.csv")

    # Criar gráfico de dispersão
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    plt.scatter(x, y)

    # Criar a primeira linha de melhor ajuste
    slope, intercept, _, _, _ = linregress(x, y)
    years_extended = np.arange(x.min(), 2051)  # Estender anos até 2050
    line1 = slope * years_extended + intercept
    plt.plot(years_extended, line1, label='Linha de Melhor Ajuste (Todos os Dados)', color='red')

    # Criar a segunda linha de melhor ajuste (de 2000 até o ano mais recente)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    line2 = slope2 * years_recent + intercept2
    plt.plot(years_recent, line2, label='Linha de Melhor Ajuste (A partir de 2000)', color='green')

    # Adicionar rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salvar gráfico e retornar dados para teste (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()