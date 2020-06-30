"""EQUILIBRIUM ANALYSIS OF PARTICLES IN TWO BOXES
Uses a random number between 0 and 1, and probability as particle left in a box/total particle.
That random number decides particles go from left to right or right to left."""


### SAHIL ISLAM ###
### Date: 11 May, 2020 ###

import matplotlib.pyplot as plt
import numpy as np
import math
import random

total_particle = 1000
MC_step = 10000
t = 0
n_left = total_particle
n_right = 0

particle_left = np.zeros(MC_step)
particle_right = np.zeros(MC_step)
time = np.zeros(MC_step)

n_analytic_left = np.zeros(MC_step)
n_analytic_right = np.zeros(MC_step)

for i in range(MC_step):

    particle_left[i] = n_left
    particle_right[i] = n_right
    time[i] = t

    x = random.random()
    prob = n_left / total_particle
    if prob > x:
        n_left = n_left - 1
        n_right = n_right + 1
    else:
        n_left = n_left + 1
        n_right = n_right - 1
    t = t + 1
    n_analytic_left[i] = total_particle * (1 + math.exp(-2 * t / total_particle)) / 2
    n_analytic_right[i] = total_particle * (1 - math.exp(-2 * t / total_particle)) / 2


def plot_loop1():
    plt.subplot(2, 2, 1)
    plt.plot(time, particle_left, label='Particle in the Left Box')
    plt.plot(time, particle_right, label="Particle in the Right Box")
    plt.ylabel("Particle In Box")
    plt.xlabel("Time")
    plt.title("Computational Solution for both Left and Right Box")
    plt.grid()
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(time, n_analytic_left, label="Analytic Solution for Left Box")
    plt.plot(time, n_analytic_right, label="Analytic Solution for Right Box")
    plt.ylabel("Particle In Box")
    plt.xlabel("Time")
    plt.title("Analytical Solution for both Left and Right Box")
    plt.grid()
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(time, particle_left, label='Computational Solution')
    plt.plot(time, n_analytic_left, label="Analytic Solution ")
    plt.ylabel("Particle In Box")
    plt.xlabel("Time")
    plt.title("Analytical & Computational Solution for  Left Box")
    plt.grid()
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(time, particle_right, label="Computational Solution")
    plt.plot(time, n_analytic_right, label="Analytic Solution")
    plt.ylabel("Particle In Box")
    plt.xlabel("Time")
    plt.title("Analytical & Computational Solution for Right Box")
    plt.grid()
    plt.legend()
    plt.suptitle(
        "Monte Carlo Simulation of Particles in a Box Reaching Equilibrium State.\n" + "Total Number of Particles:" + str(
            total_particle) + "\n" + "Number of MC MC_steps:" + str(MC_step))
    plt.subplots_adjust(0.12, 0.08, 0.90, 0.85, 0.20, 0.33)


def plot_loop2():
    plt.plot(time, particle_left, label='Particle in the Left Box')
    plt.plot(time, particle_right, label="Particle in the Right Box")
    plt.ylabel("Particle In Box")
    plt.xlabel("Time")
    plt.title(
        "Monte Carlo Simulation of Particles in a Box Reaching Equilibrium State.\n" + "Total Number of Particles:" + str(
            total_particle) + "\n" + "Number of MC MC_steps:" + str(MC_step))
    plt.grid()
    plt.legend()


plot_loop2()
plt.show()
