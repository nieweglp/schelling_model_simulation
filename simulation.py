# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:20:19 2020

@author: Paul
"""

import matplotlib.pyplot as plt
import numpy as np
#import time


people = 100
world = 10
threshold = 0.5


def initialize_world(people, world):
	population_postitions_1 = []
	population_postitions_2 = []
	slice_population = int(people/2)
	for i in range(slice_population):
		population_postitions_1.append([np.random.randint(0, world),
						      np.random.randint(0, world)])
		population_postitions_2.append([np.random.randint(0, world),
						      np.random.randint(0, world)])
	
	world_map = np.zeros((world, world), dtype='int')
	for loc in population_postitions_1:
		world_map[loc[0], loc[1]] = 1
	for loc in population_postitions_2:
		world_map[loc[0], loc[1]] = -1
		
	return world_map

world_map = initialize_world(people, world)

def check_local_area(local_people):
	local_people=list(local_people)
	local_area_ratio={}
	local_area_ratio['population_first_ratio'] = local_people.count(1)/len(local_people)
	local_area_ratio['population_second_ratio'] = local_people.count(-1)/len(local_people)
	local_area_ratio['neutral_ratio'] = local_people.count(0)/len(local_people)
	return local_area_ratio

new_world = world_map


nr, nc = np.where(world_map == 0)
neutral_space = [[nr[i],nc[i]] for i in range(0, world_map.shape[0])]

def find_new_place():
	rand_new_place = np.random.choice(range(len(neutral_space)))
	return neutral_space[rand_new_place]


temp_map = np.zeros((world, world), dtype='int')
for r in range(0, world_map.shape[0]):
	for c in range(0, world_map.shape[1]):
		temp_map[r][c] = check_local_area([world_map[r][c+1], world_map[r+1][c+1], world_map[r+1][c], world_map[r+1,c-1], world_map[r][c-1], world_map[r-1][c-1], world_map[r-1][c], world_map[r-1][c+1]])['population_first_ratio']
#		if world_map[r][c] == 1:
#			if check_local_area([world_map[r][c+1], world_map[r+1][c+1], world_map[r+1][c],
#			     world_map[r+1,c-1], world_map[r][c-1], world_map[r-1][c-1],
#			        world_map[r-1][c], world_map[r-1][c+1]])['population_first_ratio'] < threshold:
#				rn, cn = find_new_place()
#				neutral_space.remove([rn, cn])
#				neutral_space.append([r, c])
#				new_world[rn][cn] = 1
#		if world_map[r][c] == -1:
#			if check_local_area([world_map[r][c+1], world_map[r+1][c+1], world_map[r+1][c],world_map[r+1,c-1], world_map[r][c-1], world_map[r-1][c-1],world_map[r-1][c], world_map[r-1][c+1]])['population_second_ratio'] < threshold:
#				rn, cn = find_new_place()
#				neutral_space.remove([rn, cn])
#				neutral_space.append([r, c])
#				new_world[rn][cn] = -1
#				
world_map == new_world
			


world_map[-1][0]
	
		
elif: world_map[r][c] == -1:
	...
else:
	continue
	
fig, ax = plt.subplots()
ax.cla()
ax.imshow(world_map, cmap='coolwarm')
ax.set_title('People in population: {}'.format(people*2))
#	plt.pause(0.1)




