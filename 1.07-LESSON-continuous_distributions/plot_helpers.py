import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

def plot_continuous_pdf(low, high, dist_name = 'Continuous', xlabel = 'Time', stats_dist = None, lw = 5):

    x = np.arange(low, high + 1)

    fig, ax = plt.subplots(1, 1, figsize=(10,5))

    ax.set_xlim(low - 1, high + 1)
    ax.set_xlabel(xlabel, fontsize = 16)
    ax.set_ylabel('Probability Density Function (pdf)', fontsize = 16)
    ax.plot(x, stats_dist.pdf(x), color = 'darkred', lw = lw)
    ax.set_ylim(0, np.max(stats_dist.pdf(x)) + 0.03)

    plt.title(f'{dist_name} \n', fontsize = 20)

    plt.show()

def plot_continuous_cdf(low, high, dist_name = 'Continuous', xlabel = 'Time', stats_dist = None):

    x = np.linspace(low, high + 1, 300)

    fig, ax = plt.subplots(1, 1, figsize=(10,5))

    ax.set_ylim(0, 1.1)
    ax.set_xlim(low - 1, high + 1)
    ax.set_xlabel(xlabel, fontsize = 16)
    ax.set_ylabel('Cumulative Distribution Function (cdf)', fontsize = 16)

    ax.plot(x, stats_dist.cdf(x), lw = 4, color = 'darkblue')

    plt.title(f'{dist_name} \n', fontsize = 20)

    plt.show()
