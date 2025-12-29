import random

# ---------- Fitness Function ----------
def fitness(chromosome):
    non_attacking = 0
    n = len(chromosome)

    for i in range(n):
        for j in range(i + 1, n):
            # Check row and diagonal conflicts
            if chromosome[i] != chromosome[j] and \
               abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1

    return non_attacking


# ---------- Create Initial Population ----------
def create_population(pop_size, n):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, n - 1) for _ in range(n)]
        population.append(chromosome)
    return population


# ---------- Selection (Tournament Selection) ----------
def selection(population):
    a = random.choice(population)
    b = random.choice(population)
    return a if fitness(a) > fitness(b) else b


# ---------- Crossover ----------
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child


# ---------- Mutation ----------
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome


# ---------- Genetic Algorithm ----------
def genetic_algorithm(n, pop_size=100, mutation_rate=0.03, generations=1000):
    max_fitness = n * (n - 1) // 2
    population = create_population(pop_size, n)

    for generation in range(generations):
        population.sort(key=fitness, reverse=True)

        if fitness(population[0]) == max_fitness:
            print(f"Solution found at generation {generation}")
            return population[0]

        new_population = population[:10]  # Elitism

        while len(new_population) < pop_size:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    print("No perfect solution found.")
    return population[0]


# ---------- Print Board ----------
def print_board(solution):
    n = len(solution)
    for row in solution:
        line = ["Q" if col == row else "." for col in range(n)]
        print(" ".join(line))


# ---------- Main ----------
if __name__ == "__main__":
    N = int(input("Enter number of queens: "))
    solution = genetic_algorithm(N)

    print("\nSolution:", solution)
    print("\nChessboard:")
    print_board(solution)
