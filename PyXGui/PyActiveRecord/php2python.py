
"""
@author: Puall Liu
@author: Lex Li
@version: 0.2, 2015/12/18
@description: MIT License
"""

import locale
import time
import math

def ksort(d):
     return [(k,d[k]) for k in sorted(d.keys())]

def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())

def number_format(num, places=0):
    return locale.format("%.*f", (places, num), True)
