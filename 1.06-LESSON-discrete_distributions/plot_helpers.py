import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

def plot_discrete_pmf(low, high, p=None, n=None, dist_name='Discrete', stats_dist=None, lw=20):
    ## low = low end of distribution
    ## high = high end of distribution
    ## p = probability of success
    ## n = number of trials
    ## dist_name = name of distribution (included in title)
    ## stats_dist = statistical distribution
    ## lw = line width

    if stats_dist is None:
        discrete = stats.randint(low, high+1)
    else:
        discrete = stats_dist

    x = np.arange(low-1., high+1.)

    fig, ax = plt.subplots(1, 1, figsize=(10,5))

    ax.set_xlim(low-1, high+1)
    ax.set_xlabel('Outcomes', fontsize=16)
    ax.set_ylabel('Probability Mass Function (pmf)', fontsize=16)
    ax.vlines(x, 0, discrete.pmf(x), colors='darkred', lw=lw, alpha=0.6)
    ax.set_ylim(0, np.max(discrete.pmf(x))+0.03)

    if not p is None:
        p_format = ' p='+'{:.4f}'.format(p)
    else:
        p_format = ''
    if not n is None:
        n_format = ' n='+str(n)
    else:
        n_format = ''

    title = dist_name+n_format+p_format+'\n'
    plt.title(title, fontsize=20)

    plt.show()

def plot_discrete_cdf(low, high, p=None, n=None, dist_name='Discrete', stats_dist=None):

    if stats_dist is None:
        discrete = stats.randint(low, high+1)
    else:
        discrete = stats_dist

    x = np.linspace(low-1, high+1, 300)

    fig, ax = plt.subplots(1, 1, figsize=(10,5))

    ax.set_ylim(0, 1.1)
    ax.set_xlim(low-1, high+1)
    ax.set_xlabel('Outcomes', fontsize=16)
    ax.set_ylabel('Cumulative Distribution Function (cdf)', fontsize=16)

    ax.plot(x, discrete.cdf(x), lw=4, color='darkblue')

    if not p is None:
        p_format = ' p='+'{:.4f}'.format(p)
    else:
        p_format = ''
    if not n is None:
        n_format = ' n='+str(n)
    else:
        n_format = ''

    title = dist_name+n_format+p_format+'\n'
    plt.title(title, fontsize=20)

    plt.show()
