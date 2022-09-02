import numpy as np

class SegregationModel:
	def __init__(self, similarity=3, red_blue_ratio=0.5, empty=0.1, side=50):
		self.similarity = similarity
		self.red_blue_ratio = red_blue_ratio
		self.empty = empty
		self.side = side
		self.map = np.zeros((self.side, self.side))
		self.randomly_populate()

	def randomly_populate(self):
		total = self.side*self.side
		number_of_empties = int(total*self.empty)
		number_of_blues = int(self.red_blue_ratio*(total - number_of_empties))
		number_of_reds = (total - number_of_empties) - number_of_blues
		print(total, number_of_empties, number_of_blues, number_of_reds)

if __name__ == '__main__':
	sm = SegregationModel()