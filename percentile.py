''''
===============================================================
PROMBLEM DECRIPTION
*Thereom 5.3.1 (Universality of the Uniform)
	...
	(2) Let X be r.v. with CDF F. Then F(X) ~ Unif(0,1)
Example 5.3.3 (p.206)
A large number of students take a certain exam, graded on a scale from 0 to 100. 
Let X be a score of random student. 
Suppose X is continuous distribution with CDF F
(Althougt X seem like dicrete, but a contiuous distribution may be a good approximation) 
Percentile: of a number is the fraction of student who score less than number
Ex: If 60 is score median F(60)=1/2, it mean have have half of the student score above 60 and other hafl score below 60
In general, a student with score x has percentile F(x). Ex: F(70) in (1/2, 1) (F(60)=1/2)

=> Distribution of score on exam looks very non-Uniform
but the distribution of percentile of the student is non-Uniform
================================================================= 
PROGRAM DOES:
+ Generate large number of student scores (non-uniform)
+ Plot histogram of student score and percentile
'''

import sys
import numpy as np
import matplotlib.pyplot as plt 

def generate_prob_score():
	'''
	Generate list of probability of one score appear
	[p1, p2, ..., p100] allow that sum of all p_i equal 1
	score in scale form 0 to 100
	@Parameter:
		number: number of list
		return: list of probability
	'''
	l = np.random.choice(range(1,100), 100+1) # Just sure this distribution is not Uniform
	s = sum(l)
	p = [float(i)/float(s) for i in l]
	return p


class students:
	def __init__(self, number):
		self.num = number
		probs = generate_prob_score()
		self.student_scores = np.random.choice(100+1, number, p=probs)
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
		ax2.set_ylabel('Number scores')
		ax2.set_ylim(0, 20)
		ax2.set_title('Percentile Histogram')	
		plt.hist(self.percentiles, 10)
		plt.tight_layout()

		plt.show()


if __name__=='__main__':
	num_stu = 1000

	if len(sys.argv) == 2:
		num_stu = int(sys.argv[1])
		print num_stu

	school = students(num_stu)
	school.plot()

