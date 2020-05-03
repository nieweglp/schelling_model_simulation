# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:20:19 2020

@author: Paul
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def initialize_world(people, world, population_split):
    population_postitions_1 = []
    population_postitions_2 = []
    slice_population = int(people*population_split)
    for i in range(slice_population):
        population_postitions_1.append([np.random.randint(0, world),
                              np.random.randint(0, world)])
    for i in range(people-slice_population):
        population_postitions_2.append([np.random.randint(0, world),
                              np.random.randint(0, world)])

    world_map = np.zeros((world, world), dtype='int')
    for loc in population_postitions_1:
        world_map[loc[0], loc[1]] = 1
    for loc in population_postitions_2:
        world_map[loc[0], loc[1]] = -1
    return world_map

def check_local_area(local_people):
    local_people=list(local_people)
    local_area_ratio={}
    local_area_ratio['population_first_ratio'] = local_people.count(1)/len(local_people)
    local_area_ratio['population_second_ratio'] = local_people.count(-1)/len(local_people)
    local_area_ratio['neutral_ratio'] = local_people.count(0)/len(local_people)
    return local_area_ratio


def find_new_place(neutral_space):
    rand_new_place = np.random.choice(range(len(neutral_space)))
    return neutral_space[rand_new_place]




def move_on(world_map):
    new_world = world_map.copy()
    #temp_map = np.zeros((world, world), dtype='int')
    nr, nc = np.where(world_map == 0)
    neutral_space = [[nr[i],nc[i]] for i in range(0, world_map.shape[0])]

    for r in range(0, world_map.shape[0]-1):
        for c in range(0, world_map.shape[1]-1):
            neighbors = [world_map[r][c+1], world_map[r+1][c+1],
                         world_map[r+1][c], world_map[r+1,c-1],
                         world_map[r][c-1], world_map[r-1][c-1],
                         world_map[r-1][c], world_map[r-1][c+1]]
            if world_map[r][c] == 1:
                if check_local_area(neighbors)['population_first_ratio'] < threshold:
                    rn, cn = find_new_place(neutral_space)
                    neutral_space.remove([rn, cn])
                    neutral_space.append([r, c])
                    new_world[rn][cn] = 1
            if world_map[r][c] == -1:
                if check_local_area(neighbors)['population_second_ratio'] < threshold:
                    rn, cn = find_new_place(neutral_space)
                    neutral_space.remove([rn, cn])
                    neutral_space.append([r, c])
                    new_world[rn][cn] = -1
    return new_world

people = 10
world = 100
threshold = 0.8
population_split = 0.5




world_map = initialize_world(people, world, population_split)
fig, ax = plt.subplots()

i = 0
while True:
    i += 1
    try:
        world_map = move_on(world_map)
        ax.cla()
        ax.imshow(world_map, cmap='coolwarm')
        ax.set_title('Iteration: {}'.format(i))
        plt.pause(0.1)
    except:
        False
        exit()


if __name__ == "__main__":
    print("executed")






