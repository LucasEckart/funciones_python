# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.2

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
¡Felicitaciones!
Has alcanzado a resolver los ejercicios de profundización
de este módulo de funciones.

El manejo de funciones seguramente sea una herramienta que
utilizará en el proyecto de este curso.

Recomendamos que repase todos los conceptos vistos hasta
el momento del curso para prepararse para comenzar a elaborar el proyecto,
que se comenzará a debatir a partir de la próxima clase.

En caso de que se encuentre al día con las tareas y en claro
con los conceptos vistos hasta ahora, puede chusmear un desafio
avanzado adicional que se encuentra en otro repo de inove:
- Es un ejercicio que integra todo lo visto del curso (como un proyecto)
- Es bastante complejo, pero en el repositorio podrá encontrar
  algunos videos en donde se discute el problema y su resolución
- Podrá encontrar el enunciado en ese repositorio
- Podrá encontrar los resueltos en ese repositorio

Link al repo:
https://github.com/InoveAlumnos/generala_python

IMPORTANTE: Encarar ese desafio es algo personal de cada uno,
de nuestro lado preferimos que pongan su foco en tener los conceptos asimilados
para la próxima clase, para poder comenzar a debatir sobre los proyectos

'''
import random

def dados(cantidad):
    dados = []
    for tirada in range(cantidad):
        dado = random.randint(1, 6)
        dados.append(dado)
    return dados


def numero_repetido (dados_tirados):
    mas_repetido = max(dados_tirados, key = dados_tirados.count)
    return mas_repetido


def cantidad_repetidos(lista, objetivo, dados_guardados):
    for dado in lista:
        if dado == objetivo:
            dados_guardados.append(dado)
    return dados_guardados            
    


if __name__ == "__main__":
    
    dados_guardados = []

    tirar_dados = dados (5)
    print(f'Primera tirada: {tirar_dados}')

    dado_repetido = numero_repetido(tirar_dados)
    print(f'Número repetido: {dado_repetido}')

    dados_guardados = cantidad_repetidos (tirar_dados, dado_repetido, dados_guardados)
    print(f'Dados guardados en la primera tirada: {dados_guardados}\n-------')

    if len(dados_guardados) == 5:
        print(F'GENERALA! FELICIDADES GANASTE EL JUEGUIO VIEJA SOS UN GRANDE!')
        exit()


    tirada_2 =  5 - len(dados_guardados)
    tirar_dados = dados(tirada_2)
    print(f'Segunda tirada: {tirar_dados}')
    
    dados_guardados = cantidad_repetidos (tirar_dados, dado_repetido, dados_guardados)
    print(f'Dados guardados en la segunda tirada: {dados_guardados}\n-------')

    if len(dados_guardados) == 5:
        print(F'GENERALA! FELICIDADES GANASTE EL JUEGUIO VIEJA SOS UN GRANDE!')
        exit()

   
    tirada_3 =  5 - len(dados_guardados)
    tirar_dados = dados(tirada_3)
    print(f'Tercera tirada: {tirar_dados}')
    
    dados_guardados = cantidad_repetidos (tirar_dados, dado_repetido, dados_guardados)
    print(f'Dados guardados en la tercera tirada: {dados_guardados}')

    if len(dados_guardados) == 5:
        print(F'GENERALA! FELICIDADES GANASTE EL JUEGUIO VIEJA SOS UN GRANDE!')
        exit()
    else:
        print(f'Perdiste')


