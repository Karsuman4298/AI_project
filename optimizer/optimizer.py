import pygad
import numpy as np

# Define number of genes (CPU, RAM)
num_genes = 2

# Define boundaries (CPU %, RAM in MB)
gene_space = [
    {"low": 0.5, "high": 100},   # CPU: 0.5% - 100%
    {"low": 0, "high": 16}       # RAM: 0MB - 16GB
]

# Define fitness function (Updated)
def fitness_func(ga_instance, solution, solution_idx):
    cpu, ram = solution

    # Penalize negative RAM
    if ram < 0:
        return -1000  # Large negative penalty

    # Example: Minimize CPU & RAM usage while maximizing performance
    return (1 / (cpu + 1)) + (1 / (ram + 1))

# GA configuration
ga_instance = pygad.GA(
    num_generations=50,
    num_parents_mating=5,
    fitness_func=fitness_func,  # Ensure function has 3 parameters
    sol_per_pop=10,
    num_genes=num_genes,
    gene_space=gene_space,  # Enforce valid ranges
    mutation_percent_genes=10
)

# Run GA
ga_instance.run()
