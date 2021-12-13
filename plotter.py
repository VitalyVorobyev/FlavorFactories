#! /usr/bin/env python

import os
from colliders import Experiment, get_experiments
from colors import kelly_gen, pycol_gen
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 16})


def linestyle_gen():
    for item in ['-', ':', '--', '-.']:
        yield item


def yield_plot(data, expmap, ylbl, lbl, lmap=None, show=True):
    if lmap is None:
        lmap = {key: key for key in ['ctau', 'b', 'Z', 'p']}

    cgen = pycol_gen()
    cmap = {key: col for key, col in zip(['ctau', 'b', 'Z', 'p'], cgen)}
    sgen = linestyle_gen()
    smap = {key: col for key, col in zip(['ctau', 'b', 'Z', 'p'], sgen)}
    keys = set()

    fig, ax = plt.subplots(figsize=(8, 6))
    for exp, nevt in data.items():
        exp = expmap[exp]
        x = [exp.year_start, exp.year_finish]
        y = [nevt] * 2
        if exp.group in keys:
            ax.plot(x, y, color=cmap.get(exp.group, 'y'),
                    linestyle=smap.get(exp.group, '-'), linewidth=3)
        else:
            keys.add(exp.group)
            ax.plot(x, y, color=cmap.get(exp.group, 'y'),
                    linestyle=smap.get(exp.group, '-'), linewidth=3, label=exp.group)
        ax.text(x[0], y[0], exp.detector_name)

    ax.set_xlabel('Data collection', fontsize=18)
    ax.set_ylabel(ylbl, fontsize=18)
    ax.minorticks_on()
    ax.grid()
    ax.grid(which='minor', linestyle=':')
    ax.legend()
    ax.semilogy()

    fig.tight_layout()

    save_plot(f'yield{lbl}', ['png', 'pdf'])
    if show:
        plt.show()


def experiments_plot(data: dict[str: Experiment], lmap=None, show=True):
    if lmap is None:
        lmap = {key: key for key in ['ctau', 'b', 'Z']}

    cgen = kelly_gen()
    cmap = {key: col for key, col in zip(['ctau', 'b', 'Z'], cgen)}
    keys = set()

    fig, ax = plt.subplots(figsize=(8, 6))
    for exp in data.values():
        x = [exp.year_start, exp.year_finish]
        y = [exp.luminocity] * 2
        if exp.group in keys:
            ax.plot(x, y, color=cmap.get(exp.group, 'y'), linewidth=3)
        else:
            keys.add(exp.group)
            ax.plot(x, y, color=cmap.get(exp.group, 'y'), linewidth=3, label=lmap[exp.group])
        ax.text(x[0], y[0], exp.collider_name)

    ax.set_xlabel('Data collection', fontsize=18)
    ax.set_ylabel(r'Peak luminocity, $\mathrm{cm}^{-2}\mathrm{s}^{-1}$', fontsize=18)
    ax.minorticks_on()
    ax.grid()
    ax.grid(which='minor', linestyle=':')
    ax.legend()
    ax.semilogy()

    fig.tight_layout()

    save_plot('colliders', ['png', 'pdf'])
    if show:
        plt.show()


def save_plot(fname, ext=['png']):
    path = './plots' if os.path.isdir('./plots') else '.'
    for ex in ext:
        plt.savefig(f'{path}/{fname}.{ex}')


if __name__ == '__main__':
    expmap = get_experiments()
    
    data = {key: val for key, val in expmap.items()
            if val.group in ['ctau', 'b', 'Z']}

    experiments_plot(data, show=False)

    from yields import get_tau_yelds, get_charm_meson_yields
    yield_plot(get_tau_yelds(), expmap, 'Tau leptons yield', 'tau', show=False)
    yield_plot(get_charm_meson_yields(), expmap, 'Charm mesons yield', 'charm', show=False)

    plt.show()
