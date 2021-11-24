import random


class Genes:
    at_random_range = (-5, 5)
    an_random_range = (-10, 10)
    genom_length = 1000
    mutation_chance = 1  # (из 100)

    def __init__(self, at_genes=[], an_genes=[]):
        self.at_genes = at_genes
        self.an_genes = an_genes
        for i in range(self.genom_length):
            self.at_genes.append(random.randint(*self.at_random_range))
            self.an_genes.append(random.randint(*self.an_random_range))

    def mutate(self):
        for i in range(self.genom_length):
            if random.randint(1, 100) <= self.mutation_chance:
                self.at_genes[i] = random.randint(*self.at_random_range)
            if random.randint(1, 100) <= self.mutation_chance:
                self.an_genes[i] = random.randint(*self.an_random_range)
        return Genes(self.at_genes, self.an_genes)

    def copy(self):
        return Genes(self.at_genes.copy(), self.an_genes.copy())
if __name__ == '__main__':
    print('this module is not for direct call!')
