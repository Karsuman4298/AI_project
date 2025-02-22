import pygad
import numpy as np

def fitness_function(ga_instance, solution, solution_idx):
    return np.sum(solution)  # Modify based on your use case

print("Starting Genetic Algorithm Optimization...")  # ✅ Add this

ga_instance = pygad.GA(
    num_generations=10,  # Reduce for quick testing
    num_parents_mating=2,
    fitness_func=fitness_function,
    sol_per_pop=5,
    num_genes=5,
    mutation_percent_genes=10
)

ga_instance.run()

print("Optimization complete!")  # ✅ Add this
print("Best solution:", ga_instance.best_solution())  # ✅ Print best result
