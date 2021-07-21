"""Module with definition of ZDT problem interface"""

from nsga2.individual import Individual
from nsga2.problems import Problem
import random
import functools

class ZDT(Problem):

    def __init__(self, zdt_definitions):
        self.zdt_definitions = zdt_definitions
        self.max_objectives = [None, None]
        self.min_objectives = [None, None]
        self.function1 = []
        self.function2 = []
        self.problem_type = None
        self.n = zdt_definitions.n

    def __dominates(self, individual2, individual1):
        worse_than_other = self.zdt_definitions.f1(individual1) <= self.zdt_definitions.f1(individual2)\
                           and self.zdt_definitions.f2(individual1) <= self.zdt_definitions.f2(individual2)
                               # and self.zdt_definitions.f3(individual1) >= self.zdt_definitions.f3(individual2)
        better_than_other = self.zdt_definitions.f1(individual1) < self.zdt_definitions.f1(individual2)\
                            or self.zdt_definitions.f2(individual1) < self.zdt_definitions.f2(individual2)\
                            # or self.zdt_definitions.f3(individual1) > self.zdt_definitions.f3(individual2)
        return worse_than_other and better_than_other


    def nonEmptyTriclusterBackUp(self, individual):
        isRowsEmpty = True
        isColsEmpty = True
        # isTimesEmpty = Truey
        i=0
        j=0
        # k=0

        for i in range(self.zdt_definitions.data.shape[0]):
           if  individual.features[i] == 1:
                isRowsEmpty = False
           if isRowsEmpty:
               individual.features[1] = 1

        for j in range(self.zdt_definitions.data.shape[1]):
           if  individual.features[i + j] == 1:
                isColsEmpty = False
           if isColsEmpty:
               individual.features[i+1] = 1
        
        # for k in range(self.zdt_definitions.data.shape[2]):
        #    if  individual.features[i +j + k] == 1:
        #         isTimesEmpty = False
        # if isTimesEmpty:
        #    individual.features[i+j+1] = 1

	#
    def generateIndividual(self):
        individual = Individual()
        individual.features = []
        for i in range(self.n):
            individual.features.append(random.randint(0,2))
        self.nonEmptyTriclusterBackUp(individual)
        individual.dominates = functools.partial(self.__dominates, individual1=individual)
        self.calculate_objectives(individual)
        return individual

    # def generateEmptyIndividual(self):
    #     individual = Individual()
    #     individual.features = []
    #     for i in range(self.n):
    #         individual.features.append(0)
    #     self.nonEmptyTriclusterBackUp(individual)
    #     individual.dominates = functools.partial(self.__dominates, individual1=individual)
    #     return individual

    def calculate_objectives(self, individual):
        individual.objectives = []
        individual.objectives.append(self.zdt_definitions.f1(individual))
        individual.objectives.append(self.zdt_definitions.f2(individual))
        self.function1.append(self.zdt_definitions.f1(individual))
        self.function2.append(self.zdt_definitions.f2(individual))
        # individual.objectives.append(self.zdt_definitions.f3(individual))
        for i in range(2):

            if self.min_objectives[i] is None or individual.objectives[i] < self.min_objectives[i]:
                self.min_objectives[i] = individual.objectives[i]
            if self.max_objectives[i] is None or individual.objectives[i] > self.max_objectives[i]:
                self.max_objectives[i] = individual.objectives[i]
