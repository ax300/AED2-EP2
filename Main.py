import json
import matplotlib.pyplot as plt


population = {}

def add_person(v_ori, v_dest): # Cria o lista de adjacencia 
    global population

    if v_ori in population: # Se o no ja existe
        if v_dest not in population[v_ori][1]:
            population[v_ori][1].append(v_dest)
    else: # Se o no eh novo
        population[v_ori] = [False, [v_dest]] # O false indica que o vértice ainda não foi visitado

def plot_individual_degree_nodes():
    k_array = []
    v_array = []

    for k, v in population.items():
        k_array.append(k)
        v_array.append(len(v[1]))

    plt.bar(k_array, v_array) # Mostra somente os 100 primeiros resultados
    plt.xlabel('Pessoa')
    plt.ylabel('Grau do Nó')
    plt.xticks(rotation='vertical')
    plt.show()


def plot_degree_distribuition():
    degree_dict = {}
    x_array = []
    y_array = []

    # cria array de distribuicao de nos
    for k, v in population.items(): 
        if len(v[1]) not in degree_dict:      
            degree_dict[len(v[1])] = [k]
        else:
            degree_dict[len(v[1])].append(k)

    for k, v in degree_dict.items():
        x_array.append(k)
        y_array.append(len(v))

    plt.bar(x_array, y_array) # Mostra somente os 100 primeiros resultados
    plt.xlabel('Grau')
    plt.ylabel('Nº pessoas')
    plt.xticks(rotation='vertical')
    plt.show()


if __name__ == "__main__":

    with open('cenario3.txt') as f:

        v = f.readline().replace('\n', '')
        e = f.readline().replace('\n', '')

        for l in f.readlines():
            v_ori, v_dest = l.replace('\n', '').split(' ')
            add_person(v_ori, v_dest)
    # print(population)
    # plot_individual_degree_nodes()
    plot_degree_distribuition()