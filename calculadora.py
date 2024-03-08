# Titulo
print("Calculadora Ponderaciones")

# Variables
# Universidades
carrera = input(
    "Ingrese su carrera (informatica, industrial, medicina, geologia, comercial): ")
universidad = input(
    "Ingrese su universidad (UDEC, UBB, UDD, UNAB, UCSC, UCH, PUC, PUCV, USM, UST, USS): ")
# Porcentajes
nem = int(input("Ponga su puntaje NEM: "))
ranking = int(input("Ponga su puntaje Ranking: "))
m1 = int(input("Ponga su puntaje de M1: "))
m2 = int(input("Ponga su puntaje de M2: "))
lect = int(input("Ponga su puntaje de Competencia lectora: "))
history = int(input("Ponga su puntaje de Historia: "))
ciencias = int(input("Ponga su puntaje de Ciencias: "))

if carrera == ("informatica") and universidad == ("UDEC"):
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
elif carrera == ("industrial") and universidad == ("UDEC"):
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
elif carrera == ("medicina") and universidad == ("UDEC"):
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
elif carrera == ("geologia") and universidad == ("UDEC"):
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
elif carrera == ("comercial") and universidad == ("UDEC"):
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
elif carrera == ("informatica") and universidad == ("UBB"):
    neminfubb = nem * 0.10
    rankinginfubb = ranking * 0.40
    m1infubb = m1 * 0.15
    m2infubb = m2 * 0.10
    lectinfubb = lect * 0.15
    historyinfubb = history * 0.10
    cienciasinfubb = ciencias * 0.10
    totalinfubb = neminfubb + rankinginfubb + m1infubb + \
        m2infubb + lectinfubb + historyinfubb + cienciasinfubb
    infubbtotal = input("Quieres ver tu puntaje? (Si/No): ")
    if infubbtotal == ("Si"):
        print(totalinfubb)
    elif infubbtotal == ("No"):
        print("Gracias por usar.")
elif carrera == ("industrial") and universidad == ("UBB"):
    nem_industrial_ubb = nem * 0.10
    ranking_industrial_ubb = ranking * 0.50
    m1_industrial_ubb = m1 * 0.10
    m2_industrial_ubb = m2 * 0.10
    lect_industrial_ubb = lect * 0.10
    history_industrial_ubb = history * 0.10
    ciencias_industrial_ubb = ciencias * 0.10
    total_ind_ubb = m1_industrial_ubb + m2_industrial_ubb + nem_industrial_ubb + \
        ranking_industrial_ubb + lect_industrial_ubb + \
        history_industrial_ubb + ciencias_industrial_ubb
    indubb_total = input("Quieres ver tu puntaje? (Si/No): ")
    if indubb_total == ("Si"):
        print(total_ind_ubb)
    elif indubb_total == ("No"):
        print("Gracias por usar")
input("Presione enter para salir")
