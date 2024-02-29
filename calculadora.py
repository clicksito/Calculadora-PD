# Titulo
print("Calculadora Ponderaciones")

# Variables
# Universidades
universidad = input("Ingrese Su Universidad (UDEC, UBB, UCH, USACH, PUC): ")
# Carrera
carrera = input("Escoja su carrera (Informatica, Industrial, Medicina): ")
# Porcentajes
nem = input("Ponga su puntaje NEM: ")
ranking = input("Ponga su puntaje Ranking: ")
m1 = input("Ponga su puntaje de M1: ")
m2 = input("Ponga su puntaje de M2: ")
lect = input("Ponga su puntaje de Competencia lectora: ")
history = input("Ponga su puntaje de Historia: ")
ciencias = input("Ponga su puntaje de Ciencias: ")

if universidad == "UDEC":
    nemudecinf = nem * 20
    rankingudecinf = ranking * 15
    m1udecinf = m1 * 25
    m2udecinf = m2 * 15
    lectudecinf = lect * 15
    historyudecinf = history * 0
