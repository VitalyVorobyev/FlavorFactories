#! /usr/bin/env python

from dataclasses import dataclass


@dataclass
class Experiment:
    collider_name: str
    detector_name: str
    luminocity_integral: float  # fb^-1
    luminocity: float  # cm^-2 s^-1
    year_start: int
    year_finish: int
    group: str  # ctau or b

    def __str__(self) -> str:
        return f'{self.name}: {self.year_start} - {self.year_finish}, {self.luminocity:.2e}'


def get_experiments() -> dict[str, Experiment]:
    return {
        'BESII'   : Experiment('BEPC'     , 'BESII'  , 0.11   , 1.26e31  , 1989, 2005, 'ctau'),
        'CLEO-c'  : Experiment('CESR-c'   , 'CLEO-c' , 2.     , 0.76e32  , 2002, 2008, 'ctau'),
        'BESIII'  : Experiment('BEPC-II'  , 'BESIII' , 30.    , 1.e33    , 2008, 2025, 'ctau'),
        'SCT'     : Experiment('SCT'      , 'SCTD'   , 10000. , 1.e35    , 2027, 2040, 'ctau'),
        'ALEPH'   : Experiment('LEP'      , 'ALEPH'  , 0.2    , 2.4e31   , 1989, 2000, 'Z'),
        'SLD'     : Experiment('SLC'      , 'SLD'    , 0.022  , 2.2e30   , 1989, 1998, 'Z'),
        'FCC-ee'  : Experiment('FCC-ee'   , 'FCC-ee' , 130000., 2.e36    , 2035, 2040, 'Z'),
        'CLEO'    : Experiment('CESR'     , 'CLEO'   , 41.5   , 1.28e33  , 1979, 2002, 'b'),
        'Belle'   : Experiment('KEKB'     , 'Belle'  , 1040.  , 2.1083e34, 1999, 2010, 'b'),
        'BaBar'   : Experiment('PEP-II'   , 'BaBar'  , 557.   , 1.2069e34, 1999, 2008, 'b'),
        'BelleII' : Experiment('SuperKEKB', 'BelleII', 50000. , 8.e35    , 2018, 2030, 'b'),
        'LHCb'    : Experiment('LHC'      , 'LHCb'   , 9.     , None     , 2011, 2021, 'p'),
        'LHCbUI'  : Experiment('LHC'      , 'LHCb'   , 50.    , None     , 2021, 2030, 'p'),
        'LHCbUII' : Experiment('LHC'      , 'LHCb'   , 300.   , None     , 2030, 2035, 'p'),
    }


def colliders_plot(data):
    pass
