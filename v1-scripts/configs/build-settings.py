#!/usr/bin/python

# Bash 4.0 has associative arrays, but if it's available everywhere so Python it is

MACHINES = {
  'MPCNC/Archim1_T8_16T_LCD': { 'env': 'DUE', 'out': 'firmware.bin' },
  'MPCNC/Archim1_T8_16T_LCD_DualEndstop': { 'env': 'DUE', 'out': 'firmware.bin' },
  'MPCNC/Archim2_T8_16T_LCD_16step': { 'env': 'DUE', 'out': 'firmware.bin' },
  'MPCNC/Rambo_T8_16T_LCD': { 'env': 'rambo', 'out': 'firmware.hex' },
  'MPCNC/Rambo_T8_16T_LCD_DualEndstop': { 'env': 'rambo', 'out': 'firmware.hex' },
  'MPCNC/Ramps_T8_16T_LCD_32step': { 'env': 'megaatmega2560', 'out': 'firmware.hex' },
  'MPCNC/Ramps_T8_16T_LCD_32step_DualEndstop': { 'env': 'megaatmega2560', 'out': 'firmware.hex' },
  'MPCNC/MRambo_T8_16T_LCD': { 'env': 'rambo', 'out': 'firmware.hex' },
  'MP3DP/Ramps_16T_MK': { 'env': 'megaatmega2560', 'out': 'firmware.hex' },
  'MP3DP/MRambo_16T_aero': { 'env': 'rambo', 'out': 'firmware.hex' },
  'MPCNC/SKR1.3_T8_16T_LCD_32step': { 'env': 'LPC1768', 'out': 'firmware.bin' },
  'MPCNC/SKR1.3_T8_16T_LCD_32step_DualEndstop': { 'env': 'LPC1768', 'out': 'firmware.bin' },
  'MPCNC/SKRPro1.1_T8_16T_LCD_32step_DualEndstop': { 'env': 'BIGTREE_SKR_PRO', 'out': 'firmware.bin' },
  'ZenXY/Ramps_16T_LCD_32': { 'env': 'megaatmega2560', 'out': 'firmware.hex' },
  'ZenXY/MiniRambo_16T': { 'env': 'rambo', 'out': 'firmware.hex' }
}

import sys

machine = sys.argv[1]
print 'env="{env}"\nout="{out}"'.format(**MACHINES[machine])
