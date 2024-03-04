#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:32:05 2024

@author: fede23
"""
### ---- Imports ----

import sympy as sp
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s
### ---- Variable Compleja

s = sp.symbols('s ', complex=True)

from pytc2.remociones import remover_polo_infinito, remover_polo_jw

### ---- Función excitación ----

Z22=(2*(s**2+1/2))/(s*(s**2+2))

print_latex(a_equal_b_latex_s('Z_{22}', Z22))

remover_polo_jw()