#Algoritmo responsavel por fazer o calculo de juros, a partir de um valor inicial, de uma taxa de juros e de um numro de dias de atraso
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
taxa_juros_diaria = taxa_juros_anual / 365 / 100

#Função destinada a fazer o calculo de juros em especifico
juros = valor_principal * taxa_juros_diaria * dias_atraso

#Função destinada a soma do valor principal e juros, assim evidenciando o valor total
valor_total = valor_principal + juros

#Parte na qual dá o retorno do valor total e juros respectivamente
return valor_total, juros

valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
print(f"Valor total a ser pago: R${valor_total:.2f}")
print(f"Valor dos juros: R${juros:.2f}")