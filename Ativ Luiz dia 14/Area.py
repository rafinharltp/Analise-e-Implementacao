#Algoritmo no qual tem a funcionalidade de calcular area de comodos
def calcular_area_comodos():
#Declaracao da variavel
total_area = 0

#Inicializacao de um loop para fazer mais de um calculo de area
while True:

#Pede a largura do comodo em metros
largura = float(input("Digite a largura do cômodo (em metros): "))
#Pede o comprimento do comodo em metros
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

#Determina a area
area_comodo = largura * comprimento
#Retorna a area ao usuario
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

total_area += area_comodo

#Pergunta se deseja adicionar mais comodos para calculo de area
mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()

#Caso o usuario nao deseje adicionar mais comodos o loop para
if mais_comodos != 's':
break

#Retorna a area total
return total_area

#Faz o calculo da area total
area_total = calcular_area_comodos()

#Printa a frase e a area total da casa
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")