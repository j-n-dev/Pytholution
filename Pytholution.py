# libraries and stuff
import numpy as np
import matplotlib.pyplot as plt
import random as rng
import sys # for argv

steps = 100
birthChance = 100
deathChance = 10
replicationChance = 0
pop = 0

if len(sys.argv) == 6:
    steps = int(sys.argv[1])
    birthChance = int(sys.argv[2])
    deathChance = int(sys.argv[3])
    replicationChance = int(sys.argv[4])
    pop = int(sys.argv[5]);

#used later for generating the graph
pops = []

lowestPop = 0
peakPop = 0
for step in range(0, steps):
    if pop > peakPop: peakPop = pop
    if pop < lowestPop: lowestPop = pop
    pops.append(pop) # add the current population to the pops array
    # display info about current simulation
    print("Step #" + str(step + 1) + " of " + str(steps))
    print("Population: " + str(pop))

    # this is where the actual simulation occurs
    if rng.randint(0, 100) < birthChance: pop += 1 # chance of creature appearing out of nowhere

    for dude in range(0, pop):
        if rng.randint(0, 100) < deathChance: pop -= 1 # chance of creature dying
        if rng.randint(0, 100) < replicationChance: pop += 1 # chance of creature replicating

# save results to text file
np.savetxt("output.txt", pops)

# print results idk
print("-------------------------------------")
print("The results are in.")
print("Avg population: " + str(sum(pops) / len(pops)))
print("Lowest population: " + str(lowestPop))
print("Peak population: " + str(peakPop))

# graph generation
# storing data about the population history
x = np.arange(0, steps)
y = np.array(pops)

# display graph
plt.title("Population over time")
plt.xlabel("Step")
plt.ylabel("Population")
plt.plot(x, y, color="blue")
plt.show()
