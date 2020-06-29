from Person import Person
import json

population = {}
person_index = []

def add_person(v_ori, v_dest):
    global population

    if v_ori in population:
        population[v_ori].append(v_dest)
    else:
        population[v_ori] = [v_dest]

if __name__ == "__main__":

    with open('cenario3.txt') as f:

        v = f.readline().replace('\n', '')
        e = f.readline().replace('\n', '')

        for l in f.readlines():
            v_ori, v_dest = l.replace('\n', '').split(' ')
            add_person(v_ori, v_dest)

    # print(json.dumps(population, indent=4))
    print(population)