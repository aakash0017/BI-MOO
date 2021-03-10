"""Module with main parts of NSGA-II algorithm.
Contains main loop"""

from nsga2.utils import NSGA2Utils
from nsga2.population import Population
import matplotlib.pyplot as plt

class Evolution(object):
    
    def __init__(self, problem, num_of_generations, num_of_individuals):
        self.utils = NSGA2Utils(problem, num_of_individuals)

        self.population = None
        self.num_of_generations = num_of_generations
        self.on_generation_finished = []
        self.num_of_individuals = num_of_individuals
        self.problem = problem
    
    def register_on_new_generation(self, fun):
        self.on_generation_finished.append(fun)
        


    # def refreshFeaturesUsed(self):
    #     self.problem.zdt_definitions.featuresUsed = self.problem.generateEmptyIndividual()
    #     for currIndiv in self.population.population:
    #         for currFeature in range(len(currIndiv.features)):
    #             if currIndiv.features[currFeature] == 1:
    #                 self.problem.zdt_definitions.featuresUsed.features[currFeature] = 1
    #                 print(self.problem.zdt_definitions.featuresUsed.features)

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
			   
    def evolve(self):
        
        self.population = self.utils.create_initial_population()
        print ("=================== ** Initial population done ** ==========================")

        # self.refreshFeaturesUsed()
        print('Population size :' +str(len(self.population.population)))
        print('first non dominated sorting')
        self.utils.fast_nondominated_sort(self.population)
        print('calculating crowding distances')
        for front in self.population.fronts:
            self.utils.calculate_crowding_distance(front)
        children = self.utils.create_children(self.population)
        returned_population = None
        print('taille pop : '+str(len(self.population.population)))
	
        for i in range(self.num_of_generations):
        # for i in range(1):
            # front0MSR = []
            # frontSuivMSR = []
            # front0Vol = []
            # frontSuivVol = []
            # front0LSL = []
            # frontSuivLSL = []
            # frontsPlot =[]
            print('######################################################')
            print('######################################################')
            print('###############      Generation '+str(i)+'   ##################')
            print('######################################################')
            print('######################################################')
            self.population.extend(children)
            # self.refreshFeaturesUsed()
            print('Sorting population')
            self.utils.fast_nondominated_sort(self.population)
            new_population = Population()
            front_num = 0
            mn = 0
            print("above while of evolve -----------")
            print("popu = ", len(new_population))
            while len(new_population) + len(self.population.fronts[front_num]) <= self.num_of_individuals:
                print("under while of evolve -----------")
                print("popu = " , len(new_population))
                print("indi = ",self.num_of_individuals )
                mn+=1
                print('Front_num = '+str(front_num))
                print("objectives are -----", self.population.fronts[0][0].objectives[0],self.population.fronts[0][0].objectives[1] )
                self.utils.calculate_crowding_distance(self.population.fronts[front_num])
                new_population.extend(self.population.fronts[front_num])
                front_num += 1
                print("end of while loop ----- front num = ", front_num)
                print("front len = " ,len(self.population.fronts[front_num]))
            # sifted below code out  of while loop
            print(len(self.population.fronts[front_num]))
            print(self.population.fronts[front_num])
            sorted(self.population.fronts[front_num],key=self.cmp_to_key(self.utils.crowding_operator))
            print(self.population.fronts[front_num])
            print("----------------------",self.population.fronts[front_num], "-------------------------------")
            new_population.extend(self.population.fronts[front_num][0:self.num_of_individuals-len(new_population)])
            returned_population = self.population
            self.population = new_population
            children = self.utils.create_children(self.population)

            for fun in self.on_generation_finished:
                fun(returned_population, i)
            print("till here")

        return returned_population.fronts[0]


            # for frt in range(len(returned_population.fronts)):
            #     for indiv in returned_population.fronts[frt]:
            #         msrSdelta = self.problem.zdt_definitions.f1(indiv)
            #         vol = 0
            #         LSL = 0
            #         if frt == 0:
            #             print('front0 : msr/delta = '+str(msrSdelta))
            #             print('front0 : volume = '+str(vol))
            #             print('front0 : LSL = '+str(LSL))
            #             front0MSR.append(msrSdelta)
            #             front0Vol.append(vol)
            #             front0LSL.append(LSL)
            #
            #         else :
            #             print('other front : msr/delta = '+str(msrSdelta))
            #             print('other front : volume = '+str(vol))
            #             print('other front : LSL = '+str(LSL))
            #             frontSuivMSR.append(msrSdelta)
            #             frontSuivVol.append(vol)
            #             frontSuivLSL.append(LSL)
            # for fun in self.on_generation_finished:
            #     fun(returned_population, i)
	
            

            # Create plot
            # figure = plt.figure()
            # axes = figure.add_subplot(111)
	        # axes.plot(front0MSR, front0Vol, 'r.', label='front0')
            # axes.plot(frontSuivMSR, frontSuivVol, 'b.', label='autres fronts')
            # axes.set_xlabel('MSR/delta')
            # axes.set_ylabel('$Volume$')
            # axes.set_title(' front0 vs other fronts')
            # plt.legend(loc='upper left')
            # plt.savefig('generation'+str(i)+'.png')
            # plt.close(figure)



                
                
            
            
