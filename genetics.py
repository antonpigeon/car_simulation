import random


class Genes:
    at_random_range = (-5, 5)
    an_random_range = (-10, 10)
    genome_length = 2000

    def __init__(self, mutation_chance):
        self.mutation_chance = mutation_chance
        self.at_genes = []
        self.an_genes = []
        for i in range(self.genome_length):
            self.at_genes.append(random.randint(*self.at_random_range))
            self.an_genes.append(random.randint(*self.an_random_range))

    def __str__(self):
        return str(self.at_genes) + str(self.an_genes)

    def crossover(self, other_genes):
        result = Genes(self.mutation_chance)
        for i in range(self.genome_length):
            if random.random() < 0.5:
                # print(f"crossover in gene {i}")
                result.at_genes[i] = other_genes.at_genes[i]
                result.an_genes[i] = other_genes.an_genes[i]
            else:
                result.at_genes[i] = self.at_genes[i]
                result.an_genes[i] = self.an_genes[i]
        return result

    def mutate(self):
        for i in range(self.genome_length):
            if random.random() <= self.mutation_chance:
                self.at_genes[i] = random.randint(*self.at_random_range)
            if random.random() <= self.mutation_chance:
                self.an_genes[i] = random.randint(*self.an_random_range)


if __name__ == '__main__':
    print('This module is not for direct call!')
