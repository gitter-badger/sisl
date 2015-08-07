"""
Helper functions for returning special geometries often encountered
"""
from __future__ import print_function, division

import numpy as np

from sids import Atom, Geometry, SuperCell

__all__ = ['diamond']


def diamond(alat=3.57,C=None):
    """
    Returns a geometry with the diamond unit-cell (2 atoms)
    """
    dist = alat * 3. ** .5 / 4
    if C is None:
        C = Atom(Z=6,R=dist * 1.01)
    sc = SuperCell(np.array([[0,1,1],
                             [1,0,1],
                             [1,1,0]],np.float64) * alat/2,
                   nsc=[3,3,3])
    dia = Geometry(np.array([[0,0,0],[1,1,1]],np.float64) * alat/4,
                   atoms=C , sc=sc)
    return dia


if __name__ == "__main__":
    g = diamond()
    
