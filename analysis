import matplotlib.pyplot as plt
from gcpgy import tt
gtt=tt
from gcpbt import tt
btt=tt
from gcpwp import tt
wtt=tt
import numpy as np

alg=['greedy', 'backtracking','welshpowell']
tt=[gtt,btt,wtt]
ypos=np.arange(len(alg))
plt.xticks(ypos,alg)
plt.ylabel("Time(s)")
plt.xlabel("greedy vs backtracking vs welsh powell")
plt.title ("Effeciencies Analysis of greedy vs backtracking vs welshpowell algorithms")
l=plt.bar(ypos,tt)
l[0].set_color('r')
l[1].set_color('g')
plt.legend()
plt.show()
