#Funcao para calculo do indice de massa corporal(IMC)
def calcular_imc(peso, altura):

#Funcao e formula para o calculo do IMC
imc = peso / (altura ** 2)

#Retorna o imc calculado
return imc

#Funcao para classificacao do IMC
def classificar_imc(imc):

#Abre a condicional
#Se o IMC for maior que 18.5
if imc < 18.5:

#Retorna Abaixo do peso
return "Abaixo do peso"

#Se o IMC estiver entre 18.5 e 24.9
elif 18.5 <= imc < 24.9:

#Retorna Peso normal
return "Peso normal"

#Se o IMC estiver entre 25 e 29.9
elif 25 <= imc < 29.9:

#Retorna Sobrepeso
return "Sobrepeso"

#Se o IMC estiver entre 30 e 34.9
elif 30 <= imc < 34.9:

#Retorna Obesidade grau 1
return "Obesidade grau 1"

#Se o IMC estiver entre 35 e 39.9
elif 35 <= imc < 39.9:

#Retorna Obesidade grau 1
return "Obesidade grau 2"

#Se o IMC nao satisfazer nenhuma das condicoes anteriores
else:
#Retorna Obesidade grau 3
return "Obesidade grau 3"

#Funcao que sugere sugestao de atividade fisica
def sugestao_atividade_fisica(classificacao_imc):

#Abre uma condicional
#Se Abaixo do peso
if classificacao_imc == "Abaixo do peso":

#Entao retorna sugestao para essa classificacao
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
proteínas e calorias."

#Se Peso normal
elif classificacao_imc == "Peso normal":

#Entao retorna sugestao para essa classificacao
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado."

#Se Sobrepeso
elif classificacao_imc == "Sobrepeso":

#Entao retorna sugestao para essa classificacao
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
de exercícios de resistência."

#Se Obesidade grau 1
elif classificacao_imc == "Obesidade grau 1":

#Entao retorna sugestao para essa classificacao
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
programa de reeducação alimentar."

#Se Obesidade grau 2
elif classificacao_imc == "Obesidade grau 2":

#Entao retorna sugestao para essa classificacao
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional."

#Se nao se encaixa em nenhuma das condicoes anteriores entao Obesidade grau 3
else:

#Entao retorna sugestao para essa classificacao
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
fisioterapia, e consultas regulares com um nutricionista."

#Pede para digitar o peso
peso = float(input("Digite seu peso (em kg): "))

#Pede para digitar a altura
altura = float(input("Digite sua altura (em metros): "))

imc = calcular_imc(peso, altura)
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)

#Printa o IMC
print(f"Seu IMC é: {imc:.2f}")

#Printa a classificacao
print(f"Classificação: {classificacao_imc}")

#Printa a sugestao
print(f"Sugestão de atividade física: {sugestao}")