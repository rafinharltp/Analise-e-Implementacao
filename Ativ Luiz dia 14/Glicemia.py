#Algoritmo responsavel por diagnoesticar pacientes com ou nao diabetes
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

#Abre um condicional no qual se a glicemia em jejum for maior ou igual a 126 ou a glicemia pos prandial for maior ou igual a 200
if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:

#Entao a funcao retorna diabetes
return "Diabetes"

#Abre mais um condicional no qual se a glicemia em jejum estiver entre 100 e 126 ou a glicemia pos prandial estiver entre 140 e 200
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:

#Entao retorna pre diabetes
return "Pré-diabetes"

#Abre a ultima condicional senao se encaixa nas opcoes acima
else:

#Entao retorna normal
return "Normal"

#Pede ao usuario do algoritmo digitar o valor da glicemia em jejum nas unidade mg/dl
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))

#Pede ao usuario do algoritmo digitar o valor da glicemia em pos prandial nas unidade mg/dl
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

#Faz o calculo do resultado
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)

#Retorna o diagnostico
print(f"O diagnóstico é: {resultado}")