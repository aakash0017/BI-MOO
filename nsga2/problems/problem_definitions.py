class ProblemDefinitions():

    def __init__(self):
        raise NotImplementedError

    def f1(self, individual):
        raise NotImplementedError

    def f2(self, individual, wg, wc, wt):
        raise NotImplementedError

    def f3(self, individual):
        raise NotImplementedError


    def perfect_pareto_front(self):
        raise NotImplementedError

