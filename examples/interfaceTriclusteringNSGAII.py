import examples.triclusteringPlusAffiramationScore as tr
from examples.triclusteringPlusAffiramationScore import Tricluster
import numpy as np


class InterfaceTriclusteringNSGAII():

	def __init__(self, data):
		self.data = data



	def chromosomeToTricluster(self, chromosome):
		rowsTricluster=[]
		colsTricluster=[]
		# timesTricluster=[]
		invRowsTricluster = []
		i = 0
		j = 0

		

		

		for i in range(self.data.shape[0]):
			if chromosome.features[i]==1:
				rowsTricluster.append(i)

		for j in range(self.data.shape[1]):
			if chromosome.features[i+j]==1:
				colsTricluster.append(j)

		# for k in range(self.data.shape[2]):
		# 	if chromosome.features[i+j+k]==1:
		# 		timesTricluster.append(k)

		# for l in range(self.data.shape[0]):
		# 	if chromosome.features[i+j+l]==1:
		# 		invRowsTricluster.append(l)
		
		# rowsTricluster, colsTricluster, invRowsTricluster  = np.array(rowsTricluster), np.array(colsTricluster), np.array(invRowsTricluster)

		rowsTricluster, colsTricluster = np.array(rowsTricluster), np.array(colsTricluster)
		
		msr = tr.mean_squared_residue_np(self.data, rowsTricluster, colsTricluster)

		# tricluster = Tricluster(rowsTricluster, colsTricluster,  invRowsTricluster, msr)
		tricluster = Tricluster(rowsTricluster, colsTricluster, msr)


		return(tricluster)


	def triclusterToChromosome(self, tricluster, problem):
		chromosome = problem.generateEmptyIndividual()
		lL = self.data.shape[0]
		lC = self.data.shape[1]
		# lT = self.data.shape[2]
		lIR= self.data.shape[0]

		for row in tricluster.rows:
			chromosome.features[row] = 1
		for col in tricluster.cols:
			chromosome.features[lL + col] = 1
		# for time in tricluster.times:
		# 	chromosome.features[lL+lC+time] = 1
		for invRow in tricluster.inverted_rows:
			chromosome.features[lL+lC+invRow] = 1

		return(chromosome)

