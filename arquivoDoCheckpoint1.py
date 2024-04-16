# Vinícius Barros Souza 558818
# Rafael Milléo Carrenho 554726

LIMITE_APROVADO = 60
LIMITE_EXAME = 40

print("1º Semestre")
check1_s1 = float(input("Nota do checkpoint 1 (Semestre 1) de 0 a 100 = "))
check2_s1 = float(input("Nota do checkpoint 2 (Semestre 1) de 0 a 100 = "))
check3_s1 = float(input("Nota do checkpoint 3 (Semestre 1) de 0 a 100 = "))
sprint1_s1 = float(input("Nota do Sprint 1 (Semestre 1) de 0 a 100 = "))
sprint2_s1 = float(input("Nota do Sprint 2 (Semestre 1) de 0 a 100 = "))
globalSolution_s1 = float(input("Nota do Global Solution (Semestre 1) = "))

print("2º Semestre")
check1_s2 = float(input("Nota do checkpoint 1 (Semestre 2) de 0 a 100 = "))
check2_s2 = float(input("Nota do checkpoint 2 (Semestre 2) de 0 a 100 = "))
check3_s2 = float(input("Nota do checkpoint 3 (Semestre 2) de 0 a 100 = "))
sprint1_s2 = float(input("Nota do Sprint 1 (Semestre 2) de 0 a 100 = "))
sprint2_s2 = float(input("Nota do Sprint 2 (Semestre 2) de 0 a 100 = "))
globalSolution_s2 = float(input("Nota do Global Solution (Semestre 2) = "))

mediaSprint_s1 = (sprint1_s1 + sprint2_s1) / 2
mediaSprint_s2 = (sprint1_s2 + sprint2_s2) / 2

#bloco para calcular qual é o menor numero

if check1_s1 >= check3_s1 and check2_s1 >= check3_s1:
    check3_s1 = 0
elif check2_s1 >= check1_s1 and check3_s1 >= check1_s1:
    check1_s1 = 0
elif check3_s1 >= check2_s1 and check1_s1 >= check2_s1:
    check2_s1 = 0

if check1_s2 >= check3_s2 and check2_s2 >= check3_s2:
    check3_s2 = 0
elif check2_s2 >= check1_s2 and check3_s2 >= check1_s2:
    check1_s2 = 0
elif check3_s2 >= check2_s2 and check1_s2 >= check2_s2:
    check2_s2 = 0

somaCheckpoint_s1 = (check1_s1 + check2_s1 + check3_s1)
somaCheckpoint_s2 = (check1_s2 + check2_s2 + check3_s2)

mediaSemestre1 = (((somaCheckpoint_s1 + mediaSprint_s1)/3) * 0.4) + (globalSolution_s1 * 0.6)
mediaSemestre2 = (((somaCheckpoint_s2 + mediaSprint_s2)/3) * 0.4) + (globalSolution_s2 * 0.6)
mediaFinal = (mediaSemestre1 * 0.4) + (mediaSemestre2 * 0.6)


#variavel com a nota final
situacaoAluno = "Reprovado"
if mediaFinal >= LIMITE_APROVADO:
    situacaoAluno = "Aprovado"
elif mediaFinal >= LIMITE_EXAME:
    situacaoAluno = "Exame"

print("Média final = ", mediaFinal)
print("Situação do aluno ", situacaoAluno)
