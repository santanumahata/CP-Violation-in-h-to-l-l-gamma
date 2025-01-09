# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Thu 23 Jan 2020 12:32:56



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
dgZlR = Parameter(name = 'dgZlR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZlR}',
                  lhablock = 'DIM6',
                  lhacode = [ 1 ])

dgZlL = Parameter(name = 'dgZlL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZlL}',
                  lhablock = 'DIM6',
                  lhacode = [ 2 ])

dgZuR = Parameter(name = 'dgZuR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZuR}',
                  lhablock = 'DIM6',
                  lhacode = [ 3 ])

dgZuL = Parameter(name = 'dgZuL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZuL}',
                  lhablock = 'DIM6',
                  lhacode = [ 4 ])

dgZdR = Parameter(name = 'dgZdR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZdR}',
                  lhablock = 'DIM6',
                  lhacode = [ 5 ])

dgZdL = Parameter(name = 'dgZdL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZdL}',
                  lhablock = 'DIM6',
                  lhacode = [ 6 ])

dgZcR = Parameter(name = 'dgZcR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZcR}',
                  lhablock = 'DIM6',
                  lhacode = [ 7 ])

dgZcL = Parameter(name = 'dgZcL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZcL}',
                  lhablock = 'DIM6',
                  lhacode = [ 8 ])

dgZsR = Parameter(name = 'dgZsR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZsR}',
                  lhablock = 'DIM6',
                  lhacode = [ 9 ])

dgZsL = Parameter(name = 'dgZsL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZsL}',
                  lhablock = 'DIM6',
                  lhacode = [ 10 ])

dgZbR = Parameter(name = 'dgZbR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZbR}',
                  lhablock = 'DIM6',
                  lhacode = [ 11 ])

dgZbL = Parameter(name = 'dgZbL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZbL}',
                  lhablock = 'DIM6',
                  lhacode = [ 12 ])

dgZtR = Parameter(name = 'dgZtR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZtR}',
                  lhablock = 'DIM6',
                  lhacode = [ 13 ])

dgZtL = Parameter(name = 'dgZtL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $gZtL}',
                  lhablock = 'DIM6',
                  lhacode = [ 14 ])

dghVV = Parameter(name = 'dghVV',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $ghVV}',
                  lhablock = 'DIM6',
                  lhacode = [ 15 ])

dghZZ = Parameter(name = 'dghZZ',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{$\\delta $ghZZ}',
                  lhablock = 'DIM6',
                  lhacode = [ 16 ])

ghZlR = Parameter(name = 'ghZlR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZlR}',
                  lhablock = 'DIM6',
                  lhacode = [ 17 ])

ghZlL = Parameter(name = 'ghZlL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZlL}',
                  lhablock = 'DIM6',
                  lhacode = [ 18 ])

ghZuR = Parameter(name = 'ghZuR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZuR}',
                  lhablock = 'DIM6',
                  lhacode = [ 19 ])

ghZuL = Parameter(name = 'ghZuL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZuL}',
                  lhablock = 'DIM6',
                  lhacode = [ 20 ])

ghZdR = Parameter(name = 'ghZdR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZdR}',
                  lhablock = 'DIM6',
                  lhacode = [ 21 ])

ghZdL = Parameter(name = 'ghZdL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZdL}',
                  lhablock = 'DIM6',
                  lhacode = [ 22 ])

ghZcR = Parameter(name = 'ghZcR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZcR}',
                  lhablock = 'DIM6',
                  lhacode = [ 23 ])

ghZcL = Parameter(name = 'ghZcL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZcL}',
                  lhablock = 'DIM6',
                  lhacode = [ 24 ])

ghZsR = Parameter(name = 'ghZsR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZsR}',
                  lhablock = 'DIM6',
                  lhacode = [ 25 ])

ghZsL = Parameter(name = 'ghZsL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZsL}',
                  lhablock = 'DIM6',
                  lhacode = [ 26 ])

ghZbR = Parameter(name = 'ghZbR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZbR}',
                  lhablock = 'DIM6',
                  lhacode = [ 27 ])

ghZbL = Parameter(name = 'ghZbL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZbL}',
                  lhablock = 'DIM6',
                  lhacode = [ 28 ])

ghZtR = Parameter(name = 'ghZtR',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZtR}',
                  lhablock = 'DIM6',
                  lhacode = [ 29 ])

ghZtL = Parameter(name = 'ghZtL',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{gHZtL}',
                  lhablock = 'DIM6',
                  lhacode = [ 30 ])

kZZ = Parameter(name = 'kZZ',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\kappa $ZZ}',
                lhablock = 'DIM6',
                lhacode = [ 31 ])

kZa = Parameter(name = 'kZa',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\kappa $Z$\\gamma $}',
                lhablock = 'DIM6',
                lhacode = [ 32 ])

kWW = Parameter(name = 'kWW',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\kappa $WW}',
                lhablock = 'DIM6',
                lhacode = [ 33 ])

g1Z = Parameter(name = 'g1Z',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{g1z}',
                lhablock = 'DIM6',
                lhacode = [ 34 ])

kZ = Parameter(name = 'kZ',
               nature = 'external',
               type = 'real',
               value = 2.,
               texname = '\\text{$\\kappa $Z}',
               lhablock = 'DIM6',
               lhacode = [ 35 ])

ka = Parameter(name = 'ka',
               nature = 'external',
               type = 'real',
               value = 2.,
               texname = '\\kappa \\gamma',
               lhablock = 'DIM6',
               lhacode = [ 36 ])

LZ = Parameter(name = 'LZ',
               nature = 'external',
               type = 'real',
               value = 2.,
               texname = '\\text{$\\lambda $Z}',
               lhablock = 'DIM6',
               lhacode = [ 37 ])

La = Parameter(name = 'La',
               nature = 'external',
               type = 'real',
               value = 2.,
               texname = '\\lambda \\gamma',
               lhablock = 'DIM6',
               lhacode = [ 38 ])

kZt = Parameter(name = 'kZt',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\kappa $Ztil}',
                lhablock = 'DIM6',
                lhacode = [ 39 ])

kat = Parameter(name = 'kat',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\kappa \\gamma $til}',
                lhablock = 'DIM6',
                lhacode = [ 40 ])

LZt = Parameter(name = 'LZt',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\lambda $Ztil}',
                lhablock = 'DIM6',
                lhacode = [ 41 ])

Lat = Parameter(name = 'Lat',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{$\\lambda \\gamma $til}',
                lhablock = 'DIM6',
                lhacode = [ 42 ])

kZZt = Parameter(name = 'kZZt',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{$\\kappa $ZZ}',
                 lhablock = 'DIM6',
                 lhacode = [ 43 ])

kZat = Parameter(name = 'kZat',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{$\\kappa $Z$\\gamma $}',
                 lhablock = 'DIM6',
                 lhacode = [ 44 ])

kWWt = Parameter(name = 'kWWt',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{$\\kappa $WW}',
                 lhablock = 'DIM6',
                 lhacode = [ 45 ])

dgWudL = Parameter(name = 'dgWudL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWudL}',
                   lhablock = 'DIM6',
                   lhacode = [ 46 ])

dgWudR = Parameter(name = 'dgWudR',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWudR}',
                   lhablock = 'DIM6',
                   lhacode = [ 47 ])

dgWcsL = Parameter(name = 'dgWcsL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWcsL}',
                   lhablock = 'DIM6',
                   lhacode = [ 48 ])

dgWcsR = Parameter(name = 'dgWcsR',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWcsR}',
                   lhablock = 'DIM6',
                   lhacode = [ 49 ])

dgWtbL = Parameter(name = 'dgWtbL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWtbL}',
                   lhablock = 'DIM6',
                   lhacode = [ 50 ])

dgWtbR = Parameter(name = 'dgWtbR',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWtbR}',
                   lhablock = 'DIM6',
                   lhacode = [ 51 ])

dgWlvL = Parameter(name = 'dgWlvL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{$\\delta $gWlvL}',
                   lhablock = 'DIM6',
                   lhacode = [ 52 ])

ghWudL = Parameter(name = 'ghWudL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWudL}',
                   lhablock = 'DIM6',
                   lhacode = [ 53 ])

ghWudR = Parameter(name = 'ghWudR',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWudR}',
                   lhablock = 'DIM6',
                   lhacode = [ 54 ])

ghWcsL = Parameter(name = 'ghWcsL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWcsL}',
                   lhablock = 'DIM6',
                   lhacode = [ 55 ])

ghWcsR = Parameter(name = 'ghWcsR',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWcsR}',
                   lhablock = 'DIM6',
                   lhacode = [ 56 ])

ghWtbL = Parameter(name = 'ghWtbL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWtbL}',
                   lhablock = 'DIM6',
                   lhacode = [ 57 ])

ghWtbR = Parameter(name = 'ghWtbR',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWtbR}',
                   lhablock = 'DIM6',
                   lhacode = [ 58 ])

ghWlvL = Parameter(name = 'ghWlvL',
                   nature = 'external',
                   type = 'real',
                   value = 2.,
                   texname = '\\text{gHWlvL}',
                   lhablock = 'DIM6',
                   lhacode = [ 59 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

kHgg = Parameter(name = 'kHgg',
                 nature = 'internal',
                 type = 'real',
                 value = '-(aS*(-1.2361770333333333 - (8*MH**8)/(51975.*MT**8) - (13*MH**6)/(12600.*MT**6) - MH**4/(126.*MT**4) - (7*MH**2)/(90.*MT**2)))/(4.*cmath.pi*vev)',
                 texname = 'k_{\\text{Hgg}}')

kHyy = Parameter(name = 'kHyy',
                 nature = 'internal',
                 type = 'real',
                 value = '(aEW*(7.0713033 + (4*(-1.3333333333333333 - (8*MH**8)/(51975.*MT**8) - (13*MH**6)/(12600.*MT**6) - MH**4/(126.*MT**4) - (7*MH**2)/(90.*MT**2)))/3. + (41*MH**8)/(34650.*MW**8) + (29*MH**6)/(4200.*MW**6) + (19*MH**4)/(420.*MW**4) + (11*MH**2)/(30.*MW**2)))/(2.*cmath.pi*vev)',
                 texname = 'k_{\\text{Hyy}}')

kHZy = Parameter(name = 'kHZy',
                 nature = 'internal',
                 type = 'real',
                 value = '(aEW*(-12.0102136 - (4*(-0.3333333333333333 - (2*MH**8)/(51975.*MT**8) - (11*MZ**2)/(360.*MT**2) - (11*MZ**4)/(2520.*MT**4) - (37*MZ**6)/(50400.*MT**6) - MZ**8/(7425.*MT**8) - (MH**6*(0.01650793650793651 + (208*MZ**2)/(51975.*MT**2)))/(64.*MT**6) - (MH**4*(0.031746031746031744 + MZ**2/(150.*MT**2) + (8*MZ**4)/(5775.*MT**4)))/(16.*MT**4) - (MH**2*(0.07777777777777778 + (4*MZ**2)/(315.*MT**2) + (29*MZ**4)/(12600.*MT**4) + (23*MZ**6)/(51975.*MT**6)))/(4.*MT**2))*(0.5 - (4*sw2)/3.))/(cw*sw)))/(2.*cmath.pi*vev)',
                 texname = 'k_{\\text{HZy}}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

