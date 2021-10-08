import numpy as np
import matplotlib.pyplot as plt

def compute_pi(n):
    all_squares = 0
    fully_covered = 0
    coords = []
    step_size = 1/n
    for i in range(0, n):
        for j in range(0, n):
            lst = []
            lst.append([i/n, j/n]) #bottom left coordinate
            lst.append([(i+1)/n, (j+1)/n]) #top right coordinate
            coords.append(lst)
            
    for i in coords:
        if (i[0][1]**2)+(i[0][0]**2)<=1:
            all_squares += 1
        
        if (i[1][1]**2)+(i[1][0]**2)<1:
            fully_covered += 1
            
    area = step_size**2
    all_squares = all_squares * area
    fully_covered = fully_covered * area
    
    s = [fully_covered*4, all_squares*4]
    return s

def repeat_pi():
    N = []
    R = []
    N.append(10)
    R.append(compute_pi(10))
    for i in range(100,1100, 100):
        N.append(i)
        R.append(compute_pi(i))
    return N, R

def plot_pi(N, R):
    distance = [x[1]-x[0] for x in R]
    plt.plot(N, distance)
    plt.xscale = "log"
    plt.yscale = "log"
    plt.xlabel = "log n"
    plt.ylabel = "log of distance of bounds"
    plt.show()

def sim_pi(n):
    in_circle = 0
    for i in range(n):
        x = np.random.uniform()
        y = np.random.uniform()
        if (x**2) + (y**2) <= 1:
            in_circle+=1
    return 4 * in_circle / n

# Question 1
s = compute_pi(1000)
np.pi
assert s[0] < np.pi
assert s[1] > np.pi

# Question 2
N,R = repeat_pi()
print(R)
assert (R[9][0] - np.pi)**2 < 1e-3
assert (R[9][1] - np.pi)**2 < 1e-3
assert (R[6][0] - np.pi)**2 < (R[5][0] - np.pi)**2
assert (R[6][1] - np.pi)**2 < (R[5][1] - np.pi)**2

# Question 3
plt.plot(N,R)
plt.xscale("log")
plt.xlabel("log n")
plt.ylabel("bounds")
plt.show()

plot_pi(N,R)

# The article has a preicision down to 22 trillion digits of pi. Considering it has
# taken us 1000 digits to get an accuracy of 0.01, it would take a very large number
# to get to that accuracy. If we assume linearity, this would mean that n should be
# in the neighborhood of 2.2 trillion in order to get that accuracy. 

# Question 4
np.random.seed(10) # set the seed to fix randomness

pi_hat = sim_pi(100000)
print(pi_hat)

assert (pi_hat - np.pi)**2 < 1e-3
