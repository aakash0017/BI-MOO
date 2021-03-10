import sys

from metrics.problems.zdt import ZDT3Metrics
from nsga2.evolution import Evolution
from nsga2.problems.zdt import ZDT
from nsga2.problems.zdt.zdt3_definitions import ZDT3Definitions

from plotter import Plotter
import examples.triclusteringPlusAffiramationScore as tr
from examples.triclusteringPlusAffiramationScore import Tricluster


def print_generation(population, generation_num):
    print("Generation: {}".format(generation_num))

# def print_metrics(population, generation_num):
#     pareto_front = population.fronts[0]
#     metrics = ZDT3Metrics()
#     # hv = metrics.HV(pareto_front)
#     # hvr = metrics.HVR(pareto_front)
#     # print("HV: {}".format(hv))
#     print("HVR: {}".format(hvr))

collected_metrics = {}
# def collect_metrics(population, generation_num):
#     pareto_front = population.fronts[0]
#     metrics = ZDT3Metrics()
#     hv = metrics.HV(pareto_front)
#     hvr = metrics.HVR(pareto_front)
#     collected_metrics[generation_num] = hv, hvr




delta = 300


path1 = 'tp1'
# names1 =[path1+'tp1',path1+'tp2', path1+'tp3',path1+'tp4']
data = tr.readFiles(path1)



zdt_definitions = ZDT3Definitions(data, delta)
# plotter = Plotter(zdt_definitions)
problem = ZDT(zdt_definitions)
evolution = Evolution(problem, 100, 20)
# evolution.register_on_new_generation(plotter.plot_population_best_front)
evolution.register_on_new_generation(print_generation)
# evolution.register_on_new_generation(print_metrics)
# evolution.register_on_new_generation(collect_metrics)
pareto_front = evolution.evolve()

# plotter.plot_x_y(collected_metrics.keys(), map(lambda x: x[1], collected_metrics.values()), 'generation', 'HVR', 'HVR metric for ZDT3 problem', 'hvr-zdt3')
