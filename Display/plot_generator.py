import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import poisson


# Private Helpers

def _plot_helper(title, x_label, y_label, block, show):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if show:
        plt.show(block)


# Plotting Tools

def plot_line(title, x, y, x_label="", y_label="", block=True, show=True):
    fig = plt.figure()
    plt.plot(x,y)
    _plot_helper(title, x_label, y_label, block, show)
    return fig

def plot_scatter(title, x, y, x_label="", y_label="", block=True, show=True, plabel=[]):
    fig = plt.figure()
    plt.scatter(x,y)

    for i in range(len(plabel)):
        plt.annotate(plabel[i], (x[i], y[i]))

    _plot_helper(title, x_label, y_label, block, show)
    return fig

def plot_bar(title, x, y, x_label="", y_label="", block=True, show=True):
    fig = plt.figure()
    plt.bar(x, y)
    _plot_helper(title, x_label, y_label, block, show)
    return fig

def plot_heatmap(title, x, y, z, x_label="", y_label="", z_label="", block=True, show=True):
    fig = plt.figure()
    plt.imshow(z, cmap='inferno', origin='lower')
    c = plt.colorbar()
    #c.set_ticks([]) # TODO: Normalize Ticks based on input data
    c.set_label(z_label)

    plt.xticks(np.arange(min(x), max(x)+1, step=1))
    plt.yticks(np.arange(min(y), max(y)+1, step=1))

    for i in range(len(x)):
        for j in range(len(y)):
            text = plt.text(j, i, z[i][j], ha="center", va="center", color="w")

    _plot_helper(title, x_label, y_label, block, show)

    return fig
