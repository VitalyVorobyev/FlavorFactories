#! /usr/bin/env python

def get_tau_yelds():
    return {
        'ALEPH': 3.3e5,
        'Belle': 0.9e9,
        'BaBar': 0.5e9,
        'BelleII': 4.6e10,
        'SCT': 2.1e10,
    }

def get_jpsi_yields():
    return {
        'BESIII': 1.e10,
        'SCT': 1.e12,

    }

def get_charm_meson_yields():
    return {
        'LHCb': 8.e12,
        'BaBar': 8.e8,
        'Belle': 13.e8,
        'BelleII': 13.e8*40,
        'CLEOc': 5.e6,
        'BESIII': 2.e7,
        'SCT': 2.e7,
    }