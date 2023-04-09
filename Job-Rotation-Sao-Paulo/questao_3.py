import json

# Leitura do arquivo JSON
with open('dados.json', 'r') as f:
    dados = json.load(f)

# Lista com os valores de faturamento diário
faturamento_diario = [dia['valor'] for dia in dados]

# Cálculo do menor valor de faturamento diário
menor_valor = min(faturamento_diario)

# Cálculo do maior valor de faturamento diário
maior_valor = max(faturamento_diario)

# Cálculo da média mensal de faturamento diário
media_mensal = (sum(faturamento_diario)) / (len(faturamento_diario) - faturamento_diario.count(0))

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = len([dia for dia in faturamento_diario if dia > media_mensal])

# Impressão dos resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias no mês em que o faturamento diário foi superior à média mensal:", dias_acima_media)
