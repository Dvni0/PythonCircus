# Vinícius Barros Souza 558818
# Leonardo Medeiros da Silva 559220
contador = 1
LIMITE_APROVADO = 60
LIMITE_EXAME = 40
LIMITE_PRESENCA = 75
while contador <= 2:
    check1_s1 = int(input("Nota do checkpoint 1  de 0 a 100 = "))
    check2_s1 = int(input("Nota do checkpoint 2  de 0 a 100 = "))
    check3_s1 = int(input("Nota do checkpoint 3  de 0 a 100 = "))
    sprint1_s1 = int(input("Nota do Sprint 1  de 0 a 100 = "))
    sprint2_s1 = int(input("Nota do Sprint 2  de 0 a 100 = "))
    globalSolution_s1 = int(input("Nota do Global Solution  = "))
    mediaSprint_s1 = (sprint1_s1 + sprint2_s1) / 2
    if check1_s1 >= check3_s1 and check2_s1 >= check3_s1:
       check3_s1 = 0
    elif check2_s1 >= check1_s1 and check3_s1 >= check1_s1:
       check1_s1 = 0
    elif check3_s1 >= check2_s1 and check1_s1 >= check2_s1:
       check2_s1 = 0

    somaCheckpoint_s1 = (check1_s1 + check2_s1 + check3_s1)
    mediaSemestre1 = (((somaCheckpoint_s1 + mediaSprint_s1)/3) * 0.4) + (globalSolution_s1 * 0.6) 
    if contador == 2:
        check21 = check1_s1
        check22 = check2_s1
        check23 = check3_s1
        sprint21 = sprint1_s1
        sprint22 = sprint2_s1
        global2 = globalSolution_s1
        mediasprint2 = (sprint21 + sprint22) / 2
        somacheck2 = somaCheckpoint_s1
        mediasemestre2 = (((somacheck2 + mediasprint2)/3) * 0.4) + (global2 * 0.6)
    contador += 1




#bloco para calcular qual é o menor numero



mediaFinal = (mediaSemestre1 * 0.4) + (mediasemestre2 * 0.6)
presenca = int(input("Presença anual do aluno em porcentagem: "))

#variavel com a nota final

if mediaFinal >= LIMITE_APROVADO and presenca >= LIMITE_PRESENCA :
    situacaoAluno = "Aprovado"
elif presenca < LIMITE_PRESENCA:
    situacaoAluno = "Reprovado"
elif mediaFinal >= LIMITE_EXAME:
    situacaoAluno = "Exame"

elif mediaFinal < LIMITE_APROVADO and mediaFinal < LIMITE_EXAME:
    situacaoAluno = "Reprovado"
print(f"Média final = {mediaFinal:.0f}.")
print("Situação do aluno ", situacaoAluno)
