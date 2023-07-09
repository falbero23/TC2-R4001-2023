#%% TRABAJO PRÁCTICO DE LABORATORIO N°1 %%#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:12:13 2023

@author: fede23
"""
# Modulos:
import scipy.signal as sig
import matplotlib.pyplot as plt
import math as m

from pytc2.sistemas_lineales import analyze_sys, tf2sos_analog, pretty_print_lti, tf2sos_analog, pretty_print_SOS
from pytc2.general import print_subtitle

# esto dejarlo así, no tocar, es para graficar
all_sys = []
filter_names = []

#%% Valores plantilla de diseño %%#

fo  = 50    # [Hz]
n   = 2     # [orden]
BW  = 10    # [Hz]

wo  = 2*m.pi*fo
Q   = fo/BW

#%% Función transferencia filtro notch %%#

num = [1, 0, 1]
den = [1, (1/Q), 1]

tf = sig.TransferFunction(num, den)
all_sys.append(tf)
sos = tf2sos_analog(num, den)
label1 = 'Filtro-notch'
print_subtitle('label1')
pretty_print_SOS(sos, mode='omegayq')
pretty_print_lti(num, den)
filter_names.append(label1)

#%% Grafico %%#

plt.close('all') # cierro todo antes de graficar nuevamente por las dudas
analyze_sys( all_sys, filter_names)

