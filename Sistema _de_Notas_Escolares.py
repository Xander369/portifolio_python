def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas)/
len(notas)

def
determinar_situacao(media):
"""Determina a situação do aluno com base na média"""
if media >= 7:
    return "Aprovado"
elif 5 <= media <7:
    return "Recuperação"
else:
    return "Reprovado"

#Entrada de Dados
nome = input('Digite o nome do aluno:')

#Coleta das três notas do aluno
notas = []
for i in range(1, 4):
    nota =
    float(input(f'Digite a {i}'))