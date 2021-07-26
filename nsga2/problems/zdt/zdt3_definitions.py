import math
from nsga2 import seq
from nsga2.problems.problem_definitions import ProblemDefinitions
from examples.interfaceTriclusteringNSGAII import InterfaceTriclusteringNSGAII as InterfaceTrNSGA
import examples.triclusteringPlusAffiramationScore as tr
import math

class ZDT3Definitions(ProblemDefinitions):

    # def __init__(self, data, delta):
    def __init__(self, data):

        self.data = data

        # self.n = data.shape[0] + data.shape[1] + data.shape[0]
        self.n = data.shape[0] + data.shape[1]
        # self.delta = delta
        self.featuresUsed = None

    def f1(self, individual):
        interfaceTrNSGA = InterfaceTrNSGA(self.data)
        tricluster = interfaceTrNSGA.chromosomeToTricluster(individual)
        # return tr.mean_squared_residue_np(self.data, tricluster.rows, tricluster.cols,
        #                                   tricluster.inverted_rows)
        return tr.mean_squared_residue_np(self.data, tricluster.rows, tricluster.cols)

    def f2(self, individual):
        # print('this is the type of idividual: ', type(individual))
        interfaceTrNSGA = InterfaceTrNSGA(self.data)
        # print('shape of data is:', self.data.shape)
        tricluster = interfaceTrNSGA.chromosomeToTricluster(individual)
        # print(len(individual.features))
        # print(tricluster)
        if len(tricluster.cols) == 0 or len(tricluster.rows) == 1:
            return 1
        total_area = self.data.shape[0] * self.data.shape[1]
        area_bicluster = len(tricluster.rows)/len(tricluster.cols)
        # print("Calculating area")
        #maximise area
        return (1- 1/area_bicluster)



    ##############################################################################################################################

#     def sumXtc(self, tricluster):
#         res = 0
# 	for gene in tricluster.rows:
# 	    res = res + gene
# 	return res



#     def sumXXtc(self, tricluster):
#         res = 0
# 	for gene in tricluster.rows:
# 	    res = res + gene**2
# 	return res

#     def sumXg(self, tricluster):
#         res = 0
# 	for time in tricluster.times:
# 	    res = res + time
# 	return res



#     def sumXXg(self, tricluster):
#         res = 0
# 	for time in tricluster.times:
# 	    res = res + time**2
# 	return res
# ##############################################################################################################################

#     def sumXYt(self, tricluster, t):
#         res = 0
# 	for gene in tricluster.rows:
# 	    for condition in tricluster.cols:
# 		res = res + gene*self.data[gene][condition][t]
# 	return res
    
#     def sumYt(self, tricluster, t):
#         res = 0
# 	for gene in tricluster.rows:
# 	    for condition in tricluster.cols:
# 		res = res + self.data[gene][condition][t]
# 	return res
    

#     def TDt(self, tricluster, t, currSumXtc, currSumXXtc, currSumXg, currSumXXg):
# 	res=0
# 	denom = (len(tricluster.rows)*currSumXXtc-currSumXtc**2)
# 	if denom != 0:
# 	    res = (len(tricluster.rows)*self.sumXYt(tricluster, t)-(currSumXtc*self.sumYt(tricluster, t)))/denom
# 	return res

#     def Tr(self, tricluster, currSumXtc, currSumXXtc, currSumXg, currSumXXg):
#           res = 0
# 	  denom = ((len(tricluster.times) -1)*len(tricluster.times))
#           if denom != 0:
#               for time1 in tricluster.times:
#                    for time2 in tricluster.times:
#                         res = res + (abs(self.TDt(tricluster, time1, currSumXtc, currSumXXtc, currSumXg, currSumXXg) - self.TDt(tricluster, time2, currSumXtc, currSumXXtc, currSumXg, currSumXXg)))/ denom
#           return res

# ##############################################################################################################################
  
#     def sumXYc(self, tricluster, c):
#         res = 0
# 	for time in tricluster.times:
# 	    for gene in tricluster.rows:
# 		res = res + gene*self.data[gene][c][time]
# 	return res
    
#     def sumYc(self, tricluster, c):
#         res = 0
# 	for time in tricluster.times:
# 	    for gene in tricluster.rows:
# 		res = res + self.data[gene][c][time]
# 	return res
    

#     def CDc(self, tricluster, c, currSumXtc, currSumXXtc, currSumXg, currSumXXg):
# 	res = 0
# 	denom = (len(tricluster.rows)*currSumXXtc-currSumXtc**2)
# 	if denom != 0:
# 		res = (len(tricluster.rows)*self.sumXYc(tricluster, c)-(currSumXtc*self.sumYc(tricluster, c)))/denom
# 	return res

#     def Cr(self, tricluster, currSumXtc, currSumXXtc, currSumXg, currSumXXg):
#          res = 0
# 	 denom = ((len(tricluster.cols) -1)*len(tricluster.cols))
# 	 if denom != 0:
# 		 for condition1 in tricluster.cols:
# 		      for condition2 in tricluster.cols:
# 		           res = res + (abs(self.CDc(tricluster, condition1, currSumXtc, currSumXXtc, currSumXg, currSumXXg )-self.CDc(tricluster, condition2, currSumXtc, currSumXXtc, currSumXg, currSumXXg)))/denom 
#          return res
# ##############################################################################################################################

#     def sumXYg(self, tricluster, g):
#         res = 0
# 	for time in tricluster.times:
# 	    for condition in tricluster.cols:
# 		res = res + time*self.data[g][condition][time]

# 	return res
    
#     def sumYg(self, tricluster, g):
#         res = 0
# 	for time in tricluster.times:
# 	    for condition in tricluster.cols:
# 		res = res + self.data[g][condition][time]
# 	return res
    


#     def GDg(self, tricluster, g, currSumXtc, currSumXXtc, currSumXg, currSumXXg):
# 	res = 0
# 	denom = (len(tricluster.times)*currSumXXg-currSumXg**2)
# 	if denom != 0:
# 		res = (len(tricluster.times)*self.sumXYg(tricluster, g)-(currSumXg*self.sumYg(tricluster, g)))/denom
# 	return res

#     def Gr(self, tricluster, currSumXtc, currSumXXtc, currSumXg, currSumXXg):
#         res = 0
# 	denom = ((len(tricluster.rows) -1)*len(tricluster.rows))
# 	if denom !=0:
# 		for gene1 in tricluster.rows:
# 		     for gene2 in tricluster.rows:
# 		          res = res + (abs(self.GDg(tricluster, gene1, currSumXtc, currSumXXtc, currSumXg, currSumXXg)-self.GDg(tricluster, gene2, currSumXtc, currSumXXtc, currSumXg, currSumXXg)))/denom

#         return res
# ##############################################################################################################################
#     def LSL(self, tricluster):
# 	currSumXtc = self.sumXtc(tricluster)
# 	currSumXXtc = self.sumXtc(tricluster)
# 	currSumXg = self.sumXtc(tricluster)
# 	currSumXXg = self.sumXtc(tricluster)
#         return ( self.Cr(tricluster, currSumXtc, currSumXXtc, currSumXg, currSumXXg) + self.Gr(tricluster, currSumXtc, currSumXXtc, currSumXg, currSumXXg) + self.Tr(tricluster, currSumXtc, currSumXXtc, currSumXg, currSumXXg) )/3



#     def weights(self, wg, wc, wt, tricluster):
#          return len(tricluster.rows)*wg + len(tricluster.cols)*wc + len(tricluster.times)*wt


#     def distinction(self, wdg, wdc, wdt, tricluster, chrFeatUsed):
# 	CDNg = 0
# 	CDNc = 0
# 	CDNt = 0
# 	for row in chrFeatUsed.rows:
# 		if not(row in tricluster.rows):
# 			CDNg +=1
# 	for col in chrFeatUsed.cols:
# 		if not(col in tricluster.cols):
# 			CDNc +=1
# 	for time in chrFeatUsed.times:
# 		if not(time in tricluster.times):
# 			CDNt +=1
# 	return CDNg*wdg/len(tricluster.rows) + CDNc*wdc/len(tricluster.cols) + CDNt*wdt/len(tricluster.times)

#     def f2(self, individual, wg=0.2, wc=0.2, wt=0.2, wdg=0.2, wdc=0.2, wdt=0.2 ):
# 	 #LSL
# 	 interfaceTrNSGA = InterfaceTrNSGA(self.data)
# 	 tricluster = interfaceTrNSGA.chromosomeToTricluster(individual)
# 	 chrFeatUsed = interfaceTrNSGA.chromosomeToTricluster(self.featuresUsed)
# 	 res = self.LSL(tricluster) - self.weights(wg, wc, wt, tricluster) - self.distinction(wdg, wdc, wdt, tricluster, chrFeatUsed)
# 	 #print(res)
#          return res
 

# ##############################################################################################################################








#     def f3(self, individual):
# 	#volume
# 	interfaceTrNSGA = InterfaceTrNSGA(self.data)
# 	tricluster = interfaceTrNSGA.chromosomeToTricluster(individual)
#         return (float(len(tricluster.rows)) + float(len(tricluster.cols)) + float(len(tricluster.times)) + float(len(tricluster.inverted_rows)) )/ (float(self.data.shape[0]) + float(self.data.shape[1]) + float(self.data.shape[2]))


#     def f4(self, individual):
# 	#sum gene expression of tricluster
# 	interfaceTrNSGA = InterfaceTrNSGA(self.data)
# 	tricluster = interfaceTrNSGA.chromosomeToTricluster(individual)
	
# 	res = 0
# 	for row in tricluster.rows:
# 		for col in tricluster.cols:
# 			for time in tricluster.times:
# 				res = res + self.data[row][col][time]
#         return res
    

    def perfect_pareto_front(self):
        step = 0.01
        domain = seq(0, 0.0830015349, step) \
                 + seq(0.1822287280, 0.2577623634, step) \
                 + seq(0.4093136748, 0.4538821041, step) \
                 + seq(0.6183967944, 0.6525117038, step) \
                 + seq(0.8233317983, 0.8518328654, step)
        return domain, map(lambda x1: 1 - math.sqrt(x1) - x1*math.sin(10*math.pi*x1), domain)
