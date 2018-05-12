"""
Utility Functions.
"""
# Authors: N. Benjamin Erichson
#          Joseph Knox
# License: GNU General Public License v3.0
from functools import partial

import numpy as np
from scipy import linalg


def get_sdist_func(sdist):
    """wrapper for sampling distributions"""
    if sdist == 'uniform':
        return partial(np.random.uniform, -1, 1)
    return np.random.standard_normal


def conjugate_transpose(A):
    """Performs conjugate transpose of A"""
    if A.dtype == np.complexfloating:
        return A.conj().T
    return A.T


def nmf_data(m, n, k, factor_type='normal', noise_type='normal', noiselevel=0):
    _factor_types = ('normal', 'unif')

    if factor_type not in _factor_types:
        raise ValueError('factor_type must be one of %s, not %s'
                         % (' '.join(_factor_types), factor_type))

    if noise_type != 'normal':
        raise ValueError('noise type must be "normal", not %s' % noise_type)

    if factor_type == 'normal':
        #Normal
        Wtue = np.maximum(0, np.random.standard_normal((m, k)))
        Htrue = np.maximum(0, np.random.standard_normal((k, n)))
    else:
        #Unif
        Wtue = np.random.rand(m, k)
        Htrue =  np.random.rand(k, n)

    A = Anoisy = Wtue.dot(Htrue)

    # noise
    Anoisy += noiselevel * np.maximum(0, np.random.standard_normal((m,n)))

    return A, Anoisy
