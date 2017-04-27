import numpy as np
import matplotlib.pyplot as plt
import sys, getopt

def chaos_game(N, p):
	polygon = np.zeros((N, 2))
	angles = np.random.random(N) * 2 * np.pi
	angles.sort()
	r = np.random.randint(0, 101)
	for i in range(N):
		polygon[i] = np.asarray([r*np.cos(angles[i]), r*np.sin(angles[i])])

	point = np.random.randint(-r, r, (2,))

	f = plt.figure()
	for i in range(p):
		plt.scatter(x=point[0], y=point[1], c='b', marker='.')

		die = np.random.randint(0, N)
		point = np.mean([polygon[die], point], axis=0)

	plt.scatter(x=polygon[:,0], y=polygon[:,1], s=100, c='r', marker='*')
	plt.show()


def main(argv):
	N = 3
	points = 2000
	
	try:
		opts, args = getopt.getopt(argv, 'hN:p:')
	except getopt.GetoptError:
		print 'chaos_game.py -N <polygon vertices> -p <generated points>'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print 'chaos_game.py -N <polygon vertices> -p <generated points>'
			sys.exit()
		elif opt == '-N':
			N = int(arg)
		elif opt == '-p':
			points = int(arg)

	chaos_game(N, points)

if __name__ == '__main__':
   main(sys.argv[1:])