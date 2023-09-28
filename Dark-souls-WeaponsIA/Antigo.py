#Tentativa de heuristica
import pandas as pd
import random
import numpy as np

bosses = pd.read_csv('bosses.csv')
weapons = pd.read_csv('DS3_weapon.csv')
weapons[['physical', 'magic', 'fire', 'lightning', 'dark']] = weapons['Damage'].str.split('/', expand=True)
weapons[['physicalAttack', 'magicAttack', 'fireAttack', 'lightningAttack', 'darkAttack']] = weapons['Damage Reduction'].str.split('/', expand=True)
none_resistente = []
for i in range (287):
    none_resistente.append('0')
weapons['none'] = none_resistente

condition_heavy = weapons['Weight'] > 13
condition_fire = weapons['fire'] != '0'
condition_lightning = weapons['lightning'] != '0'
condition_magic = weapons['magic'] != '0'
condition_physical = weapons['physical'] != '0'

heavy_weapons = weapons[condition_heavy]
light_weapons = weapons[~condition_heavy]
fire_weapons = weapons[condition_fire]
lightning_weapons = weapons[condition_lightning]
magic_weapons = weapons[condition_magic]
physical_weapons = weapons[condition_physical]

graph = {
'begin': [('Resist_fire_weapons'), ('lightning_weapons'), ('magic_weapons'), ('physical_weapons'), ('none')],
'none': [('fire_weapons'), ('lightning_weapons'), ('magic_weapons'), ('physical_weapons')],
'fire_weapons':[],
'lightning_weapons': [],
'magic_weapons': [],
'physical_weapons': [],
}













#Algoritmo genetico
import pandas as pd
import random
import numpy as np

bosses = pd.read_csv('bosses.csv')
weapons = pd.read_csv('DS3_weapon.csv')
weapons[['physical', 'magic', 'fire', 'lightning', 'dark']] = weapons['Damage'].str.split('/', expand=True)
weapons[['physicalAttack', 'magicAttack', 'fireAttack', 'lightningAttack', 'darkAttack']] = weapons['Damage Reduction'].str.split('/', expand=True)
none_resistente = np.zeros(287)
weapons['none'] = none_resistente


def objective_state(boss):
    objective = []
    objective.append(boss['Velocidade'])
    objective.append(1)#eficiencia máxima na fraqueza
    objective.append(0) #eficiencia máxima na resistecia
    return objective
    
def select_weapons(states):
    chosen_weapons_index = [random.randint(0,286)for _ in range(states)]
    return chosen_weapons_index

def weapons_poinst(chosen_weapons_index,boss,states):
    list_weapon = []
    for i in range (states):
        loop = []
        loop.append(0 if weapons.at[chosen_weapons_index[i],'Weight'] > 10 else 1)
        loop.append(1 if (int)(weapons.at[chosen_weapons_index[i],boss['Fraqueza']]) > 0 else 0)
        loop.append(1 if (int)(weapons.at[chosen_weapons_index[i],boss['Resistente']]) > 0 else 0)
        list_weapon.append(loop)
    return list_weapon

def fitness(weapon_points,objective):
    fn = 0
    for i in range(3):
            if weapon_points[i] == objective[i]:
                fn += 1
    return fn

def selection_probability(chosen_weapon_points,number_states,objective):
    fitness_value = [fitness(chosen_weapon_points[i],objective) for i in range(number_states)]
    total_fitness = sum(fitness_value)
    probabilities = [fitness_value[i]/total_fitness for i in range(number_states)]
    return fitness_value, probabilities

def define_culling(weapon_index,probabilities, states):
    culling_weapons = []
    for i in range(states):
        if probabilities[i] > 0.20: culling_weapons.append(weapon_index(i))
    
    while (len(culling_weapons) < 4):
        culling_weapons.append(culling_weapons[0])
    return culling_weapons

def crossover()

if __name__ == '__main__':
    
    states = 4
    numbem_boss = random.randint(0,21)
    boss= bosses.iloc[numbem_boss]
    objective = objective_state(boss)
    weapons_index = select_weapons(states)
    print(weapons_index)
    weapons_points = weapons_poinst(weapons_index,boss,states)
    print(objective)
    print(weapons_points) 
    fitness_value, probabilities = selection_probability(weapons_points,states,objective)
    print(probabilities)
    print(boss['Nomes'])
    culling_weapons = define_culling(weapons_index,probabilities,states)

#-----------------------------------------------------------------------------------

import numpy as np
import random as random

Objetivo = [1, 2, 3,8, 0, 4, 7, 6, 5]

def fitness(estado):
    fn = 0
    for i in range(9):
            if estado[i] == Objetivo[i]:
                fn += 1
    return fn

def generate_chromosomes(tamanho):
    chromosomes = [np.random.permutation([1, 2, 3, 4, 5, 6, 7, 8, 0]).tolist() for _ in range(tamanho)]
    return chromosomes

def selection_probability(chromosomes,number_states):
    fitness_value = [fitness(chromosomes[i]) for i in range(number_states)]
    total_fitness = sum(fitness_value)
    probabilities = [fitness_value[i]/total_fitness for i in range(number_states)]
    return fitness_value, probabilities

def aleatory_chromosomes(states):
    chromosomes = generate_chromosomes(states)
    fitness_value, probabilities = selection_probability(chromosomes,states)
    for i in range(states):
        print(f"Cromossomo {i+1}:")
        print(chromosomes[i])
        print(f"Fitness: {fitness_value[i]}")
        print(f"Probabilidade de Selecao: {probabilities[i]}\n")

def culling(states):
    chromosomes = generate_chromosomes(states)
    fitness_value, probabilities = selection_probability(chromosomes, states)
    culling_chromosomes = []
    for i in range(states):
        if probabilities[i] > 0.15:
            
            culling_chromosomes.append(chromosomes[i])
            
    return culling_chromosomes

def equal_value(c1):
    for i in range(9):
        for j in range(9):
            if i != j and c1[i]==c1[j]:
                return i
    return -1

#ponto de corte será aleatório para varias as soluçoes a fim de nao ter um padrão nas estruturas geradas 
def crossover(c1, c2):

    cut_point = random.randint(1, len(c1) - 2)
    
    new_c1 = c1.copy()
    
    
    new_c1[cut_point:] = c2[cut_point:]
    
    
    while(True):
        equal_value_index = equal_value(new_c1)
        if(equal_value_index == -1):
            break
        new_c1[equal_value_index] = random.randint(0, 9)
    
    return new_c1

def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    
    new_value = random.choice([val for val in range(len(chromosome)) if val != chromosome[mutation_point]])

    chromosome[mutation_point] = new_value

if __name__ == '__main__':
    states = 4
    print("\n----CROMOSSOMOS ALEATÓRIOS----")
    aleatory_chromosomes(states)
    print("--------------------------------------------------------")
    
    print("\n----CULLING AND CROSSOVER AND MUTATION----")
    states = 4
    culling_chromosomes = culling(states)
    
    while len(culling_chromosomes) < 4:
        culling_chromosomes.append(culling_chromosomes[0])
    
    old_chromosomes = culling_chromosomes.copy()
    fitness_value, probabilities = selection_probability(culling_chromosomes, states)
    
    culling_chromosomes[0]= crossover(culling_chromosomes[0], culling_chromosomes[1])
    culling_chromosomes[1]= crossover(old_chromosomes[1], old_chromosomes[0])
    culling_chromosomes[2] = crossover(culling_chromosomes[2], culling_chromosomes[3])
    culling_chromosomes[3] = crossover(old_chromosomes[3], old_chromosomes[2])
    
    fitness_value, probabilities = selection_probability(culling_chromosomes, states)
    
    for i in range(states):
        mutate(culling_chromosomes[i])
        print(f"Cromossomo {i+1}:")
        print(culling_chromosomes[i])
        print(f"Fitness: {fitness_value[i]}")
        print(f"Probabilidade de Selecao: {probabilities[i]}\n")