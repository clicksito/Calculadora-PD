# Titulo
print("Calculadora Ponderaciones")

# Variables
# Universidades
carrera = input("Ingrese su carrera: ")
# Porcentajes
nem = int(input("Ponga su puntaje NEM: "))
ranking = int(input("Ponga su puntaje Ranking: "))
m1 = int(input("Ponga su puntaje de M1: "))
m2 = int(input("Ponga su puntaje de M2: "))
lect = int(input("Ponga su puntaje de Competencia lectora: "))
history = int(input("Ponga su puntaje de Historia: "))
ciencias = int(input("Ponga su puntaje de Ciencias: "))

if carrera == ("informatica"):
    neminf = nem * 0.20
    rankinginf = ranking * 0.15
    m1inf = m1 * 0.25
    m2inf = m2 * 0.15
    lectinf = lect * 0.15
    cienciasinf = ciencias * 0.10
    totalinf = neminf + rankinginf + m1inf + \
        m2inf + lectinf + cienciasinf
    infudectotal = input("Quieres ver tu puntaje? (Si/No): ")
    if infudectotal == ("Si"):
        print(totalinf)
    elif infudectotal == ("No"):
        print("Gracias por usar")
elif carrera == ("industrial"):
    nemindu = nem * 0.20
    rankingindu = ranking * 0.15
    m1indu = m1 * 0.25
    m2indu = m2 * 0.15
    lectindu = lect * 0.15
    cienciasindu = ciencias * 0.10
    totalindu = nemindu + rankingindu + m1indu + \
        m2indu + lectindu + cienciasindu
    induudectotal = input("Quieres ver tu puntaje? (Si/No): ")
    if induudectotal == ("Si"):
        print(totalindu)
    elif induudectotal == ("No"):
        print("Gracias por usar")
elif carrera == ("medicina"):
    nemmed = nem * 0.15
    rankingmed = ranking * 0.25
    m1med = m1 * 0.35
    lectmed = lect * 0.15
    cienciasmed = ciencias * 0.10
    totalmed = m1med + nemmed + rankingmed + lectmed + cienciasmed
    medudectotal = input("Quieres ver tu puntaje? (Si/No): ")
    if medudectotal == ("Si"):
        print(totalmed)
    elif medudectotal == ("No"):
        print("Gracias por usar")
elif carrera == ("geologia"):
    nemgeol = nem * 0.15
    rankingeol = ranking * 0.25
    m1geol = m1 * 0.30
    lectgeol = lect * 0.20
    cienciasgeol = ciencias * 0.10
    totalgeol = nemgeol + rankingeol + m1geol + lectgeol + cienciasgeol
    geoludectotal = input("Quieres ver tu puntaje? (Si/No): ")
    if geoludectotal == ("Si"):
        print(totalgeol)
    elif geoludectotal == ("No"):
        print("Gracias por usar")
elif carrera == ("comercial"):
    nemingeco = nem * 0.15
    rankingingeco = ranking * 0.25
    m1ingeco = m1 * 0.30
    m2ingeco = m2 * 0.05
    lectingeco = lect * 0.15
    historyingeco = history * 0.10
    cienciasingeco = ciencias * 0.10
    totalingeco = nemingeco + rankingingeco + m1ingeco + \
        m2ingeco + lectingeco + historyingeco + cienciasingeco
    totaludecingeco = input("Desea ver su puntaje? (Si/No): ")
    if totaludecingeco == ("Si"):
        print(totalingeco)
    elif totaludecingeco == ("No"):
        print("Gracias por usar")
