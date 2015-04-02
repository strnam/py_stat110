# 

import numpy as np
import matplotlib.pyplot as plt 
# X (random variables) :
#		- description: score of random student
#  		- valuse: 0-100


class students:
	def __init__(self, number):
		self.num = number
		self.student_scores = np.random.randint(1, 100+1, number)
		self.percentiles = []
		for score in xrange(100+1):
			self.percentiles.append(self.percentile(score))



	def percentile(self, score):
		return float(len(self.student_scores[self.student_scores < score]))/float(self.num)

	def plot(self):
		fig = plt.figure(figsize=(6,3))
		ax1 = fig.add_subplot(121)
		ax1.set_xlabel('Students')
		ax1.set_ylabel('Score')
		ax1.set_title('Student Scores Histogram')	
		plt.hist(self.student_scores, bins=100)

		ax2 = fig.add_subplot(122)
		ax2.set_xlabel('Percentiles')
		ax2.set_ylabel('Students')
		ax2.set_ylim(0, 20)
		ax2.set_title('Percentile Histogram')	
		plt.hist(self.percentiles, 10)
		plt.tight_layout()

		plt.show()


if __name__=='__main__':
	school = students(10000)
	school.plot()

