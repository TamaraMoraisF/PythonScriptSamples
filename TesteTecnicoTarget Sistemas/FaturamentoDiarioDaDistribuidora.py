import json

maior = menor = 0
faturamentoDiarioMaiorAMedia = 0
totalFaturamento = 0

with open("FaturamentoMarço2023.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

for valor in dados:
    if valor['diaUtil']:
        totalFaturamento = totalFaturamento + valor['faturamento']

        if maior == 0:
            maior = valor['faturamento']
            menor = valor['faturamento']

        if valor['faturamento'] > maior:
            maior = valor['faturamento']

        if valor['faturamento'] < menor:
            menor = valor['faturamento']

for num in dados:
    if num['diaUtil']:
        if num['faturamento'] > totalFaturamento/len(dados):
            faturamentoDiarioMaiorAMedia = faturamentoDiarioMaiorAMedia + 1

print(f'O menor valor de faturamento ocorrido em um dia do mês foi R${menor:,.2f}.')
print(f'O maior valor de faturamento ocorrido em um dia do mês R${maior:,.2f}.')
print(f'Foram {faturamentoDiarioMaiorAMedia} dias no mês em que o valor de faturamento diário foi superior à média '
      f'mensal.')
