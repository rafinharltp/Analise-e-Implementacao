#Algoritmo com a funcao de calcular medias e se foi aprovado ou reprovado
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):

#Determinacoes das variaveis
total_notas = 0
num_alunos = len(notas)
aprovados = []
reprovados = []

#Coloca a nota do aluno em uma lista de notas
for aluno, nota in notas.items():
total_notas += nota

#Verifica se a nota do aluno e suficente para aprovacao
if nota >= nota_minima_aprovacao:

#Se for o enquadra na classe aprovados
aprovados.append(aluno)

#Caso nao o enquadra na classe reprovados
else:
reprovados.append(aluno)

#Faz o calculo da media de notas da turma como um todo
media_turma = total_notas / num_alunos

#Retorna a media da turma, os aprovados e reprovados respectivamente
return media_turma, aprovados, reprovados

#Notas dos alunos
notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

#Definicao da nota minima de aprovacao
nota_minima_aprovacao = 70

#Funcao que calcula a media e aprovacao dos alunos
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

#Printa a media da turma
print(f"Média da turma: {media_turma:.2f}")

#Printa os alunos aprovados
print(f"Alunos aprovados: {', '.join(aprovados)}")

#Printa os alunos reprovados
print(f"Alunos reprovados: {', '.join(reprovados)}")