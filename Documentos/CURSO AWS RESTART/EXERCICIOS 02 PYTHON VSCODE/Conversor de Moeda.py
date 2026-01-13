
valor_reais = 100.00
cotacao_dolar = 5.60
cotacao_euro = 6.60

conversao_dolar = valor_reais / cotacao_dolar
conversao_euro = valor_reais / cotacao_euro

print(f"Valor original: R$ {valor_reais:.2f}")
print(f"Conversão para Dólar: $ {round(conversao_dolar, 2)}")
print(f"Conversão para Euro: € {round(conversao_euro, 2)}")
