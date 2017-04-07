import matplotlib.pyplot as plt
import numpy as np


def plot_bars(data, quantities, quantity_labels, xlabel, ylabel, figname='plot.png', title=None):
    means = {quantities[0]: [], quantities[1]: []}
    std = {quantities[0]: [], quantities[1]: []}

    keys = sorted(data.keys())
    for k in keys:
        for t in means.keys():
            means[t].append(data[k][t].mean())
            std[t].append(data[k][t].std())

    index = np.arange(len(data.keys()))
    bar_width = 0.35
    shift = bar_width / 2.0

    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    capsize = 2

    plt.bar(
        index + shift, means[quantities[0]], bar_width,
        alpha=opacity,
        color='b',
        yerr=std[quantities[0]],
        error_kw=error_config,
        label=quantity_labels[0],
        capsize=capsize
    )

    plt.bar(
        index + bar_width + shift, means[quantities[1]], bar_width,
        alpha=opacity,
        color='r',
        yerr=std[quantities[1]],
        error_kw=error_config,
        label=quantity_labels[1],
        capsize=capsize
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.xticks(index + bar_width, keys)
    plt.xlim(-0.3, 3)
    plt.legend(loc=0)
    plt.grid(color='gray', linestyle='dotted')

    plt.tight_layout()
    plt.savefig(figname)
    plt.show()
