import sys

from plotter import Plotter
from metrics.problems.zdt import ZDT3Metrics
import plotly.express as px
from nsga2.evolution import Evolution
from nsga2.problems.zdt import ZDT
from nsga2.problems.zdt.zdt3_definitions import ZDT3Definitions
import matplotlib.pyplot as plt

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




delta = 100


path1 = 'yeast_output.txt'
# names1 =[path1+'tp1',path1+'tp2', path1+'tp3',path1+'tp4']
#bcl dataste
data = tr.readFiles(path1)



zdt_definitions = ZDT3Definitions(data, delta)
# plotter = Plotter(zdt_definitions)
problem = ZDT(zdt_definitions)
evolution = Evolution(problem, 50, 20)

# evolution.register_on_new_generation(plotter.plot_population_best_front)
evolution.register_on_new_generation(print_generation)
# evolution.register_on_new_generation(print_metrics)
# evolution.register_on_new_generation(collect_metrics)
pareto_front = evolution.evolve()

# plotter = Plotter(problem)
# plotter.plot_x_y(collected_metrics.keys(), map(lambda x: x[1], collected_metrics.values()), 'generation', 'HVR', 'HVR metric for ZDT3 problem', 'hvr-zdt3')

# function1 = [i[0] for i in problem.min_objectives[0]]
# function2 = [i[1] for i in problem.min_objectives[1]]
# plt.xlabel('Function 1', fontsize=15)
# plt.ylabel('Function 2', fontsize=15)
# plt.scatter(function1, function2)
# plt.show()

# print(problem.function1)
# print(problem.function2)

plt.xlabel('MSR', fontsize=15)
plt.ylabel('Area', fontsize=15)
print(problem.function2)
print(problem.function1)
plt.scatter(problem.function1, problem.function2)
plt.show()
print("'generation 100 individual: 20 dataset: som_yeast ")
print('Lowest MSR is ' ,problem.min_objectives[0])
print('heighest msr is ', problem.max_objectives[0])
fig = px.scatter(x=problem.function1, y=problem.function2, )
fig2 = px.line(y=problem.function1)
fig3 = px.line(y=problem.function2)
fig.show()
fig2.show()
fig3.show()
