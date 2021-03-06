"""
Biais vs Variance
=================

Fits the data with polynoms with increasing degrees.

"""
import numpy as np
import matplotlib.pyplot as plt


def test_func(x, err=0.5):
    return np.random.normal(10 - 1. / (x + 0.1), err)


def compute_error(x, y, p):
    yfit = np.polyval(p, x)
    return np.sqrt(np.mean((y - yfit) ** 2))


def plot_bias_variance(N=8, random_seed=42, err=0.5):
    x = 10 ** np.linspace(-2, 0, N)
    y = test_func(x)

    xfit = np.linspace(-0.2, 1.2, 1000)

    titles = ['d = 1 (under-fit; high bias)',
              'd = 2',
              'd = 6 (over-fit; high variance)']
    degrees = [1, 2, 6]

    fig = plt.figure(figsize=(9, 3.5))
    fig.subplots_adjust(left=0.06, right=0.98,
                        bottom=0.15, top=0.85,
                        wspace=0.05)
    for i, d in enumerate(degrees):
        ax = fig.add_subplot(131 + i, xticks=[], yticks=[])
        ax.scatter(x, y, marker='x', c='k', s=50)

        p = np.polyfit(x, y, d)
        yfit = np.polyval(p, xfit)
        ax.plot(xfit, yfit, '-b')

        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(0, 12)
        ax.set_xlabel('house size')
        if i == 0:
            ax.set_ylabel('price')

        ax.set_title(titles[i])


plot_bias_variance()
