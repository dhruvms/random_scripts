import numpy as np
import matplotlib.pyplot as plt
import sys, getopt

def affine(f, p):
	A = np.reshape(f[:4], (2, 2))
	b = f[4:]

	p = np.dot(A, p) + b
	return p

def barnsley_fern(p):
	f1 = np.asarray([0.0, 0.0, 0.0, 0.16, 0.0, 0.0])
	f2 = np.asarray([0.85, 0.04, -0.04, 0.85, 0.0, 1.60])
	f3 = np.asarray([0.20, -0.26, 0.23, 0.22, 0.0, 1.60])
	f4 = np.asarray([-0.15, 0.28, 0.26, 0.24, 0.0, 0.44])

	probs = np.cumsum(np.asarray([0.01, 0.85, 0.07, 0.07]))
	point = np.asarray([0.0, 0.0])

	f = plt.figure()
	for i in range(p):
		plt.scatter(x=point[0], y=point[1], c='g', marker='.')

		s = np.random.rand()
		result = np.digitize(s, probs)

		if result == 0:
			point = affine(f1, point)
		elif result == 1:
			point = affine(f2, point)
		elif result == 2:
			point = affine(f3, point)
		else:
			point = affine(f4, point)

	plt.show()

def main(argv):
	points = 2000
	
	try:
		opts, args = getopt.getopt(argv, 'hp:')
	except getopt.GetoptError:
		print 'barnsley_fern.py -p <number of points>'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print 'barnsley_fern.py -p <number of points>'
			sys.exit()
		elif opt == '-p':
			points = int(arg)
	
	barnsley_fern(points)

if __name__ == '__main__':
   main(sys.argv[1:])