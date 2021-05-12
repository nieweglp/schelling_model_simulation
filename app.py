import matplotlib.pyplot as plt
from simulation import initialize_world, move_on

PEOPLE = 500
WORLD = 100
THRESHOLD = 0.6
POPULATION_SPLIT = 0.7


def main(people, world, threshold, population_split):
    
    world_map = initialize_world(people, world, population_split)
    fig, ax = plt.subplots()

    i = 0
    while True:
        try:
            i += 1
            world_map = move_on(world_map, threshold)
            ax.cla()
            ax.imshow(world_map, cmap='coolwarm')
            ax.set_title('Iteration: {}'.format(i))
            plt.pause(0.1)
        except:
            False
            exit()


if __name__ == "__main__":
    main(PEOPLE, WORLD, THRESHOLD, POPULATION_SPLIT)