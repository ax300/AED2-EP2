import json
import matplotlib.pyplot as plt


population = {}

def add_person(v_ori, v_dest): #cria o lista de adjacencia 
    global population

    if v_ori in population: #se o no ja existe
        population[v_ori].append(v_dest)
    else: #se o no eh novo
        population[v_ori] = [v_dest]

def plot():
    k_array = []
    v_array = []

    for k, v in population.items():
        k_array.append(k)
        v_array.append(len(v))

    plt.bar(k_array, v_array)
    plt.xlabel('Pessoa')
    plt.ylabel('Grau do Nó')
    plt.xticks(rotation='vertical')
    plt.show()


if __name__ == "__main__":

    with open('cenario3.txt') as f:

        v = f.readline().replace('\n', '')
        e = f.readline().replace('\n', '')

        for l in f.readlines():
            v_ori, v_dest = l.replace('\n', '').split(' ')
            add_person(v_ori, v_dest)

    plot()
