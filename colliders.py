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


def experiments() -> dict[str, Experiment]:
    return {
        Experiment('CESR', 'CLEO', ?, ?, 1978, ),
        Experiment('CESR-c', 'CLEO-c', ),
        Experiment('BEPC', 'BESII', 0.11, 12.6e30, 1989, 2005, 'ctau'),
        Experiment('BEPC-II', 'BESIII', 30, 12.6e30, 1989, 2005, 'ctau')
    }


def colliders_plot(data):
    pass
