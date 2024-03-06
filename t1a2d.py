'''#Construir um programa que faz a leitura de duas
notas de um aluno, N1 e N2, e os respectivos pesos, P1 e P2. O
programa deve calcular a média ponderada alcançada por aluno
e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou
igual a sete;
• A mensagem "Reprovado", se a média for menor do que
sete;
• A mensagem "Aprovado com Distinção", se a média for igual
a dez.'''

N1=float(input("Nota 1: "))
N2=float(input("Nota 2: "))
P1=float(input("Peso 1: "))
P2=float(input("Peso 2: "))

m=((N1*P1)+(N2*P2))/(P1+P2)
if(m>=7):
    print(f"\n Aprovado")
if(m<7):
    print(f"\n Reprovado")
if(m==10):
    print(f"\n Aprovado com distinção")
