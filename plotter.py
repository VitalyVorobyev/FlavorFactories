from colliders import Experiment, get_experiments
from colors import kelly_gen
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 16})
import numpy as np

def yield_plot(data):
    pass


def experiments_plot(data: dict[str: Experiment]):
    fig, ax = plt.subplots(figsize=(8, 6))

    cgen = kelly_gen()
    cmap = {key: col for key, col in zip(['ctau', 'b', 'Z'], cgen)}
    # lmap = {'ctau', 'b', 'Z'}
    keys = set()

    for exp in data.values():
        x = [exp.year_start, exp.year_finish]
        y = [exp.luminocity] * 2
        if exp.group in keys:
            ax.plot(x, y, color=cmap.get(exp.group, 'y'), linewidth=3)
        else:
            keys.add(exp.group)
            ax.plot(x, y, color=cmap.get(exp.group, 'y'), linewidth=3, label=exp.group)
        ax.text(x[0], y[0], exp.collider_name)

    ax.set_xlabel('Operation period', fontsize=18)
    ax.set_ylabel(r'Peak luminocity, $\mathrm{cm}^{-2}\mathrm{s}^{-1}$', fontsize=18)
    ax.minorticks_on()
    ax.grid()
    ax.grid(which='minor', linestyle=':')
    ax.legend()
    ax.semilogy()

    fig.tight_layout()

    plt.savefig('colliders.png')
    plt.show()

if __name__ == '__main__':
    data = {key: val for key, val in get_experiments().items()
            if val.group in ['ctau', 'b', 'Z']}

    experiments_plot(data)
