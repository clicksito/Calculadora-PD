# Titulo
print("Calculadora Ponderaciones")

# Variables
# Universidades
universidad = input("Ingrese Su Universidad (UDEC, UBB, UCH, USACH, PUC): ")
# Porcentajes
nem = int(input("Ponga su puntaje NEM: "))
ranking = int(input("Ponga su puntaje Ranking: "))
m1 = int(input("Ponga su puntaje de M1: "))
m2 = int(input("Ponga su puntaje de M2: "))
lect = int(input("Ponga su puntaje de Competencia lectora: "))
history = int(input("Ponga su puntaje de Historia: "))
ciencias = int(input("Ponga su puntaje de Ciencias: "))

if universidad == "UDEC":
    nemudecinf = nem * 0.20
    rankingudecinf = ranking * 0.15
    m1udecinf = m1 * 0.25
    m2udecinf = m2 * 0.15
    lectudecinf = lect * 0.15
    historyudecinf = history * 0
    cienciasudecinf = ciencias * 0.10

totaludecinf = nemudecinf + rankingudecinf + m1udecinf + \
    m2udecinf + lectudecinf + historyudecinf + cienciasudecinf
carrera = input("Escoja su carrera (Informatica, Industrial, Medicina): ")
if carrera == "Informatica":
    print(totaludecinf)
