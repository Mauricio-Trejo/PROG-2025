# Simular el lanzamiento de un dado y una moneda

# Lanzamiento de una moneda

# Método 1
'''
import numpy as np
import scipy.stats as stats

p = 0.5  # probabilidad de cada caso

lanzamiento = stats.bernoulli.rvs(p)

print('Cara' if lanzamiento == 1 else 'Cruz')
'''

# Método 2

import random

opciones = ['Cara', 'Cruz']

lanzamiento = random.choice(opciones)

print(lanzamiento)