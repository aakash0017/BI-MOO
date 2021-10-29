"""NSGA-II related functions"""

import functools
from nsga2.population import Population
import random
from examples.interfaceTriclusteringNSGAII import InterfaceTriclusteringNSGAII as InterfaceTrNSGA
import examples.triclusteringPlusAffiramationScore as tr
from examples.triclusteringPlusAffiramationScore import Tricluster

class NSGA2Utils(object):
    
    def __init__(self, problem, num_of_individuals, mutation_strength=0.2, num_of_genes_to_mutate=5, num_of_tour_particips=2):
        
        self.problem = problem
        self.num_of_individuals = num_of_individuals
        self.mutation_strength = mutation_strength
        self.number_of_genes_to_mutate = num_of_genes_to_mutate
        self.num_of_tour_particips = num_of_tour_particips
        self.data = problem.zdt_definitions.data

	
	
        
    # def fast_nondominated_sort(self, population):
    #     population.fronts = []
    #     population.fronts.append([])
    #     for individual in population:
    #         individual.domination_count = 0
    #         individual.dominated_solutions = set()
    #
    #         for other_individual in population:
    #             if individual.dominates(other_individual):
    #                 individual.dominated_solutions.add(other_individual)
    #             elif other_individual.dominates(individual):
    #                 individual.domination_count += 1
    #         if individual.domination_count == 0:
    #             population.fronts[0].append(individual)
    #             individual.rank = 0
    #     i = 0
    #     while len(population.fronts[i]) > 0:
    #         temp = []
    #         for individual in population.fronts[i]:
    #             for other_individual in individual.dominated_solutions:
    #                 other_individual.domination_count -= 1
    #                 if other_individual.domination_count == 0:
    #                     other_individual.rank = i+1
    #                     temp.append(other_individual)
    #         i = i+1
    #         population.fronts.append(temp)

    def fast_nondominated_sort(self, population):
        population.fronts = []
        population.fronts.append([])
        for individual in population:
            individual.domination_count = 0
            individual.dominated_solutions = set()

            for other_individual in population:
                if individual.dominates(other_individual):
                    individual.dominated_solutions.add(other_individual)
                elif other_individual.dominates(individual):
                    individual.domination_count += 1
            if individual.domination_count == 0:
                population.fronts[0].append(individual)
                individual.rank = 0
        i = 0
        while len(population.fronts[i]) > 0:
            temp = []
            for individual in population.fronts[i]:
                for other_individual in individual.dominated_solutions:
                    other_individual.domination_count -= 1
                    if other_individual.domination_count == 0:
                        other_individual.rank = i + 1
                        temp.append(other_individual)
            i = i + 1
            population.fronts.append(temp)

    def cmp(self,a, b):
        return (a > b) - (a < b)

    def cmp_to_key(self,mycmp):

        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
        return K

    def __sort_objective(self, val1, val2, m):
        return self.cmp(val1.objectives[m], val2.objectives[m])
    
    def calculate_crowding_distance(self, front):
        if len(front) > 0:
            solutions_num = len(front)
            for individual in front:
                individual.crowding_distance = 0
            
            for m in range(len(front[0].objectives)):
                front = sorted(front, key=lambda individual: individual.objectives[m])
                # front = sorted(front, key=self.cmp_to_key (functools.partial(self.__sort_objective, m=m)))

                front[0].crowding_distance = self.problem.max_objectives[m]
                front[solutions_num-1].crowding_distance = self.problem.max_objectives[m]
                for index, value in enumerate(front[1:solutions_num-1]):
                    front[index].crowding_distance = (front[index+1].crowding_distance - front[index-1].crowding_distance) / (self.problem.max_objectives[m] - self.problem.min_objectives[m])
                
    def crowding_operator(self, individual, other_individual):
        if (individual.rank == None or individual.crowding_distance == None or other_individual.crowding_distance == None):
            print("rank ----- ", individual.rank)
            print("indi --- ", individual.crowding_distance)
            print("other indi --- ", other_individual.crowding_distance)
            print("None objective function value")
        else:
            if (individual.rank < other_individual.rank) or \
                ((individual.rank == other_individual.rank) and (individual.crowding_distance > other_individual.crowding_distance)):
                return 1
            else:
                return -1
    def nonEmptyTriclusterBackUp(self, individual):
        isRowsEmpty = True
        isColsEmpty = True
        # isTimesEmpty = True
        # i=0
        j=0
        k=0

        for i in range(self.data.shape[0]):
           if  individual.features[i] == 1:
               isRowsEmpty = False
           if isRowsEmpty:
               # individual.features[1] = 1
               individual.features[i] = 1
        for j in range(self.data.shape[1]):
           if  individual.features[i + j] == 1:
               isColsEmpty = False
           if isColsEmpty:
               # individual.features[i+1] = 1
               individual.features[i+j] = 1


	
          
    def create_initial_population(self):
        population = Population()
        # self.problem.zdt_definitions.featuresUsed = self.problem.generateEmptyIndividual()
        for i in range(self.num_of_individuals):
            print("Individual-", i)
            individual = self.problem.generateIndividual()
            # self.nonEmptyTriclusterBackUp(individual)
            # individualsTrimax = self.deltaTrimaxOnChild(individual)
            # for indiv in individualsTrimax:
            #     # self.problem.calculate_objectives(indiv)
            #     population.population.append(indiv)
            population.population.append(individual)
        return population

    # def create_initial_population(self):
    #     population = Population()
    #     for i in range(self.num_of_individuals):
    #         print ("Individual-", i)
    #         individual = self.problem.generateIndividual()
    #         population.population.append(individual)
    #     return population
    #
    # def deltaTrimaxOnChild(self, child):
    #     interfaceTrNSGA = InterfaceTrNSGA(self.data)
    #     triclusterChild = interfaceTrNSGA.chromosomeToTricluster(child)
    #     print("MSR child before trimax\t" + str(triclusterChild.msr))
    #     triclusters = tr.find_triclusters_np(self.data)
    #     trimaxChildren = []
    #     for tricluster in triclusters:
    #         newChild = interfaceTrNSGA.triclusterToChromosome(tricluster, self.problem)
    #         self.problem.calculate_objectives(newChild)
    #         trimaxChildren.append(newChild)
    #     return trimaxChildren

      
    def create_children(self, population):
        children = []
        while len(children) < len(population):
            parent1 = self.__tournament(population)
            parent2 = parent1
            while parent1.features == parent2.features:
                parent2 = self.__tournament(population)
            child1, child2 = self.__crossover(parent1, parent2)
            self.__mutate(child1)
            self.__mutate(child2)
            self.problem.calculate_objectives(child1)
            self.problem.calculate_objectives(child2)
            children.append(child1)
            children.append(child2)
            # self.nonEmptyTriclusterBackUp(child1)
            # self.nonEmptyTriclusterBackUp(child1)
            # trimaxChildren1 = self.deltaTrimaxOnChild(child1)
            # trimaxChildren2 = self.deltaTrimaxOnChild(child2)
            # for i in range(len(trimaxChildren1)):
            #     self.problem.calculate_objectives(trimaxChildren1[i])
            #     children.append(trimaxChildren1[i])
            # for j in range(len(trimaxChildren2)):
            #     self.problem.calculate_objectives(trimaxChildren2[j])
            #     children.append(trimaxChildren2[j])
        return children
    
    def __crossover(self, individual1, individual2):
        child1 = self.problem.generateIndividual()
        child2 = self.problem.generateIndividual()
        min_gene_length = min(len(child1.features), len(child2.features))
        min_individual_length = min(len(individual1.features), len(individual2.features))
        min_choromosome = min(min_individual_length, min_gene_length)
        genes_indexes = range(min_choromosome)
        half_genes_indexes = random.sample(genes_indexes, 1)
        for i in genes_indexes:
            if i in half_genes_indexes:
                child1.features[i] = individual2.features[i]
                child2.features[i] = individual1.features[i]
            else:
                child1.features[i] = individual1.features[i]
                child2.features[i] = individual2.features[i]
        return child1, child2

    def __mutate(self, child):
        # mutation_parameter = random.random()
        # self.number_of_genes_to_mutate = int(len(child.features)/4)
        # genes_to_mutate = random.sample(range(0, len(child.features)), self.number_of_genes_to_mutate)
        # if mutation_parameter > 0.7:
        #     for gene in genes_to_mutate:
        #         child.features[gene] = child.features[gene] - self.mutation_strength/2 + random.random() * self.mutation_strength
        #         if child.features[gene] < 0:
        #             print('')
        #             child.features[gene] = 0
        #         elif child.features[gene] > 1:
        #             child.features[gene] = 1

        mutation_parameter = random.random()
        self.number_of_genes_to_mutate = int(len(child.features) / 4)
        genes_to_mutate = random.sample(range(0, len(child.features)), self.number_of_genes_to_mutate)
        if mutation_parameter > 0.7:
            for gene in genes_to_mutate:
                child.features[gene] = 1 if child.features[gene] == 0  else 0
        
    def __tournament(self, population):
        participants = random.sample(list(population), self.num_of_tour_particips)
        best = None
        for participant in participants:
            if best is None or self.crowding_operator(participant, best) == 1:
                best = participant

        return best