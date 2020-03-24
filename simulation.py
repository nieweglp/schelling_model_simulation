# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:20:19 2020

@author: Paul
"""

import matplotlib.pyplot as plt
import numpy as np
#import time


last_person = 100
world = 10

for people in range(1,last_person):
	population_postitions_1 = []
	population_postitions_2 = []
	slice_population = int(people/2)
	for i in range(slice_population):
		population_postitions_1.append([np.random.randint(0, world),
						      np.random.randint(0, world)])
		population_postitions_2.append([np.random.randint(0, world),
						      np.random.randint(0, world)])
	
	world_map = np.zeros((world, world))
	for loc in population_postitions_1:
		world_map[loc[0], loc[1]] = 1
	for loc in population_postitions_2:
		world_map[loc[0], loc[1]] = -1
		
	if people==1:
		fig, ax = plt.subplots()
	ax.cla()
	ax.imshow(world_map, cmap='coolwarm')
	ax.set_title('People in population: {}'.format(people*2))
	plt.pause(0.1)

#, cmap='coolwarm'




