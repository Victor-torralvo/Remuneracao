import pandas as pd

#Importando a tabela csv.
with open('remuneracaoServidores.csv', encoding="UTF-8", errors='ignore') as arquivo:
    data_original = pd.read_csv(arquivo, sep = ';', low_memory=False)

#Tratamento de dados

data_original['REMUNERAÇÃO BÁSICA'] = data_original['REMUNERAÇÃO BÁSICA'].str.replace(',','.').astype(float)
data_original['IRRF'] = data_original['IRRF'].str.replace(',','.').astype(float)
data_original['BRUTO'] = data_original['BRUTO'].str.replace(',','.').astype(float)
data_original['LÍQUIDO'] = data_original['LÍQUIDO'].str.replace(',','.').astype(float)

#Criando um subset apenas com  as colunas necessarias para o trabalho.

data_resumo = data_original[["ÓRGÃO","CARGO",'REMUNERAÇÃO BÁSICA','IRRF','BRUTO','LÍQUIDO']]

#Lista com as 3 maiores Remuneracoes basicas.
maior_salario_cargo = data_resumo.sort_values(by='REMUNERAÇÃO BÁSICA',ascending=False).head(3)
print("\nLista dos 3 Maiores Salarios: \n",maior_salario_cargo.to_string())

#Media Remuneracao Basica por cargo em cada orgao:

salario_orgao_cargo = data_resumo.groupby(["ÓRGÃO","CARGO"])['REMUNERAÇÃO BÁSICA'].mean().round(2).reset_index()
salario_orgao_cargo = salario_orgao_cargo.sort_values(by= 'REMUNERAÇÃO BÁSICA',ascending = False)
print('\nMaiores medias de remuneracao basica por cargo em orgaos: \n',salario_orgao_cargo.head(3).to_string())

#Media Salarial Bruta e Liquida de cada orgao:

media_salarial = data_resumo.groupby("ÓRGÃO")[['BRUTO','LÍQUIDO']].mean().round(2).reset_index()
media_salarial = media_salarial.sort_values(by = 'BRUTO', ascending=False)
print('\nMaiores medias salariais brutas e liquidas: \n',media_salarial.head(3).to_string())

#Maiores medias salariais por cargo:
salario_cargo_orgao = data_resumo.groupby(["CARGO"])['REMUNERAÇÃO BÁSICA'].mean().round(2).reset_index()
salario_cargo_orgao = salario_cargo_orgao.sort_values(by = 'REMUNERAÇÃO BÁSICA', ascending=False)
print('\nMaiores medias salariais por cargo: \n',salario_cargo_orgao.head(3).to_string())


#correlacao entre irrf, bruto e liquido

corre= data_resumo['IRRF'].corr(data_resumo['BRUTO'])
print("\nCorrelacao de IRRF com BRUTO:\n", corre)

corre = data_resumo['IRRF'].corr(data_resumo['LÍQUIDO'])
print("\nCorrelacao de IRRF com Liquido:\n", corre)


#valor total pago

total = data_resumo["BRUTO"].sum().round(2)
print("\nValor total:\n", total)