import numpy as np
import matplotlib.pyplot as plt
import statistics as stats

obs_data = np.loadtxt("CircuitoRC.txt")

t_obs = obs_data[:,0]
q_obs = obs_data[:,1]

mean = obs_data[:,1].mean()
dstand =stats.stdev(q_obs)
#print(dstand)


fig1 = plt.figure()
plt.scatter(t_obs, q_obs, alpha = 0.8)
plt.xlabel(r"$t(s)$", fontsize = 8)
plt.ylabel(r"$Q(C)$", fontsize = 8)
fig1.savefig("Figure1.pdf", bbox_inches="tight")


def likelihood(q_obs, q_model):
	chi_squared = (1.0/2.0)*sum(((q_obs - q_model)/(dstand))**2)
	return np.exp(- chi_squared)

def my_model(t_obs, R, C):
	return 10*C*(1 - np.exp(- t_obs/(R*C) ))

R_walk = np.empty((0))
C_walk = np.empty((0))
l_walk = np.empty((0))

R_walk = np.append(R_walk, np.random.random())
C_walk = np.append(C_walk, np.random.random())

q_init = my_model(t_obs, R_walk[0], C_walk[0])
l_walk = np.append(l_walk, likelihood(q_obs, q_init))

#print (R_walk)
#print (C_walk)
#print (l_walk)

n_iterations = 20000
for i in range(n_iterations):
	R_prime = np.random.normal(R_walk[i], 0.1)
	C_prime = np.random.normal(C_walk[i], 0.1)

	q_init = my_model(t_obs, R_walk[i], C_walk[i])
	q_prime = my_model(t_obs, R_prime, C_prime)

	l_prime = likelihood(q_obs, q_prime)
	l_init = likelihood(q_obs, q_init)

	alpha = l_prime/l_init
	
	if(alpha>=1.0):
		R_walk = np.append(R_walk, R_prime)
		C_walk = np.append(C_walk, C_prime)
		l_walk = np.append(l_walk, l_prime)
	else:
		beta = np.random.random()
		if(beta<=alpha):
			R_walk = np.append(R_walk, R_prime)
			C_walk = np.append(C_walk, C_prime)
			l_walk = np.append(l_walk, l_prime)
		else:
			R_walk = np.append(R_walk, R_walk[i])
			C_walk = np.append(C_walk, C_walk[i])
			l_walk = np.append(l_walk, l_init)

fig2 = plt.figure()
plt.scatter(R_walk, C_walk, alpha = 0.8)
plt.xlabel(r"$R(s)$", fontsize = 8)
plt.ylabel(r"$C(C)$", fontsize = 8)
fig2.savefig("Figure2.pdf", bbox_inches="tight")

fig3 = plt.figure()
plt.scatter(R_walk, -np.log(l_walk), alpha = 0.8)
plt.xlabel(r"$R(\Omega)$", fontsize = 8)
plt.ylabel(r"$\frac{1}{2} \chi{^2}$",fontsize = 8)
fig3.savefig("Figure3.pdf", bbox_inches="tight")

fig4 = plt.figure()
plt.scatter(C_walk, -np.log(l_walk), alpha = 0.8)
plt.xlabel(r"$C(C/V)$", fontsize = 8)
plt.ylabel(r"$\frac{1}{2} \chi{^2}$",fontsize = 8)
fig4.savefig("Figure4.pdf", bbox_inches="tight")



min_R = np.amin(R_walk)
max_R = np.amax(R_walk)
min_C = np.amin(C_walk)
max_C = np.amax(C_walk)


from scipy.interpolate import griddata


grid_R, grid_C = np.mgrid[min_R:max_R:200j, min_C:max_C:200j]



n_points = np.size(R_walk)
points = np.ones((n_points,2))
#print(np.shape(points))
points[:,0] = R_walk
points[:,1] = C_walk
grid_l = griddata(points, -np.log(l_walk), (grid_R, grid_C), method='cubic')

fig5 = plt.figure()
plt.imshow(grid_l.T, extent=(min_R, max_R, min_C, max_C), aspect='auto', origin='lower')
fig5.savefig("Figure5.pdf", bbox_inches="tight")

fig6 = plt.figure()
count, bins, ignored = plt.hist(R_walk, 20, normed=True, alpha = 0.8)
fig6.savefig("Figure6.pdf", bbox_inches="tight")

fig7 = plt.figure()
count, bins, ignored = plt.hist(C_walk, 20, normed=True)
fig7.savefig("Figure7.pdf", bbox_inches="tight")

max_likelihood_id = np.argmax(l_walk)
best_R = R_walk[max_likelihood_id]
best_C = C_walk[max_likelihood_id]
#print (np.log10(l_walk[max_likelihood_id]))
print (best_R)
print (best_C)


best_q = my_model(t_obs, best_R, best_C)


fig8 = plt.figure()
plt.scatter(t_obs, q_obs, alpha = 0.9)
plt.plot(t_obs, best_q, color='black')
plt.xlabel(r"$t(s)$", fontsize = 8)
plt.ylabel(r"$Q(C)$", fontsize = 8)
plt.legend([r"$R =5.95 \Omega, C = 10.022 C / V, Q_{m\'ax} = 100.22 C $"], loc="best")
fig8.savefig("Figure8.pdf", bbox_inches="tight")






