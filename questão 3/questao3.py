import json
with open('faturamento.json') as file:
    dados = json.load(file)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
