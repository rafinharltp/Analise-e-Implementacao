#Algoritmo coma funcionalidade de calcular o custo de uma viagem
def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio):

#Equacao que calcula o gasto em combustivel com base na divisao da distancia e o consumo do veiculo multiplicado pelo custo do combustivel
custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

#Equacao que calcula o gasto com pedagios multiplicando o numero e o custo dos pedagios
custo_pedagio_total = numero_pedagios * custo_pedagio

#Equacao do custo total soma do custo total de pedagio e custo total de combustivel
custo_total = custo_combustivel_total + custo_pedagio_total

#Retona custo total, custo total do combustivel, custo total do pedagio respectivamente
return custo_total, custo_combustivel_total, custo_pedagio_total

#Pede para o usuario digitar a distancia
distancia = float(input("Digite a distância da viagem (em km): "))

#Pede para o usuario digitar o custo do combustivel
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))

#Pede para o usuario digitar o consumo medio do veiculo
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))

#Pede para o usuario digitar o numero de pedagios
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))

#Pede para o usuario digitar o custo e um pedagio
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,
custo_combustivel,
consumo_veiculo, numero_pedagios,

custo_pedagio)

#Printa o custo total da viagem
print(f"Custo total da viagem: R${custo_total:.2f}")

#Printa o custo total com combustivel
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")

#Printa o custo total com pedagios
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")