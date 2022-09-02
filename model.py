import numpy as np
from matplotlib import pyplot as plt

class SegregationModel:
	def __init__(self, similarity=3, red_blue_ratio=0.5, empty=0.1, side=50):
		self.similarity = similarity/8
		self.red_blue_ratio = red_blue_ratio
		self.empty = empty
		self.side = side
		self.map = np.zeros((self.side+2, self.side+2))
		self.randomly_populate()

	def randomly_populate(self):
		total = self.side*self.side
		number_of_empties = int(total*self.empty)
		number_of_blues = int(self.red_blue_ratio*(total - number_of_empties))
		number_of_reds = (total - number_of_empties) - number_of_blues
		relevant_indices = np.random.choice(np.arange(total), size=number_of_blues+number_of_reds, replace=False)
		reds = [(i%self.side, i//self.side) for i in relevant_indices[:number_of_reds]]
		blues = [(i%self.side, i//self.side) for i in relevant_indices[number_of_reds:]]
		for (i,j) in reds:
			self.map[i+1, j+1] = 1
		for (i,j) in blues:
			self.map[i+1, j+1] = -1
		plt.imshow(self.map)
		plt.show()

	def get_similar_units(self, i, j, val):
		pass


	def run_single_simulation(self):
		for i,row in enumerate(self.map):
			for j,col in enumerate(row):
				n = self.get_similar_units(i, j, col)


if __name__ == '__main__':
	sm = SegregationModel()
	sm.run_single_simulation()