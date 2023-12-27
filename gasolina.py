# código de geração do gráfico 
import pandas as pd
import seaborn as sns

dados_gasolina = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  grafico_gasolina = sns.lineplot(
      x = 'Data',
      y = 'Venda',
      df = gas
  )
  
  grafico_gasolina.set(
      title = 'Valor Diário da Gasolina no Município de São Paulo',
      xlabel = 'Dia',
      ylabel = 'Preço (R$)'
  )
  
  figura = grafico_gasolina.get_figure()    
  figura.savefig('gasolina.png', dpi=600)
