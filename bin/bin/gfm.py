#!/usr/bin/python3

import sys
import string
from decimal import Decimal


def get_atomic_mass(element):
    # The second integer is places after the decimal point.
    elements = {
        'H': (Decimal('1.0079'), 4),
        'Li': (Decimal('6.941'), 3),
        'Na': (Decimal('22.99'), 2),
        'K': (Decimal('39.10'), 2),
        'Rb': (Decimal('85.47'), 2),
        'Cs': (Decimal('132.91'), 2),
        'Fr': (Decimal('223'), 0),

        'Be': (Decimal('9.012'), 3),
        'Mg': (Decimal('24.30'), 2),
        'Ca': (Decimal('40.08'), 2),
        'Sr': (Decimal('87.62'), 2),
        'Ba': (Decimal('137.33'), 2),
        'Ra': (Decimal('226.02'), 2),

        'Sc': (Decimal('44.96'), 2),
        'Y': (Decimal('88.91'), 2),
        'La': (Decimal('138.91'), 2),
        'Ac': (Decimal('227.03'), 2),

        'Ti': (Decimal('47.90'), 2),
        'Zr': (Decimal('91.22'), 2),
        'Hf': (Decimal('178.49'), 2),
        'Rf': (Decimal('261'), 0),

        'V': (Decimal('50.94'), 2),
        'Nb': (Decimal('92.91'), 2),
        'Ta': (Decimal('180.95'), 2),
        'Db': (Decimal('262'), 0),

        'Cr': (Decimal('52.00'), 2),
        'Mo': (Decimal('95.94'), 2),
        'W': (Decimal('183.85'), 2),
        'Sg': (Decimal('266'), 0),

        'Mn': (Decimal('54.938'), 3),
        'Tc': (Decimal('98'), 0),
        'Re': (Decimal('186.21'), 2),
        'Bh': (Decimal('264'), 0),

        'Fe': (Decimal('55.85'), 2),
        'Ru': (Decimal('101.1'), 1),
        'Os': (Decimal('190.2'), 1),
        'Hs': (Decimal('277'), 0),

        'Co': (Decimal('58.93'), 2),
        'Rh': (Decimal('102.91'), 2),
        'Ir': (Decimal('192.2'), 1),
        'Mt': (Decimal('268'), 0),

        'Ni': (Decimal('58.69'), 2),
        'Pd': (Decimal('106.42'), 2),
        'Pt': (Decimal('195.08'), 2),
        'Ds': (Decimal('271'), 0),

        'Cu': (Decimal('63.55'), 2),
        'Ag': (Decimal('107.87'), 2),
        'Au': (Decimal('196.97'), 2),
        'Rg': (Decimal('272'), 0),

        'Zn': (Decimal('65.39'), 2),
        'Cd': (Decimal('112.41'), 2),
        'Hg': (Decimal('200.59'), 2),

        'Ga': (Decimal('69.72'), 2),
        'Al': (Decimal('26.98'), 2),
        'B': (Decimal('10.811'), 3),
        'In': (Decimal('114.82'), 2),
        'Tl': (Decimal('204.38'), 2),

        'C': (Decimal('12.011'), 3),
        'Si': (Decimal('28.09'), 2),
        'Ge': (Decimal('72.59'), 2),
        'Sn': (Decimal('118.71'), 2),
        'Pb': (Decimal('207.2'), 1),

        'N': (Decimal('14.007'), 3),
        'P': (Decimal('30.974'), 3),
        'As': (Decimal('74.92'), 2),
        'Sb': (Decimal('121.75'), 2),
        'Bi': (Decimal('208.98'), 2),

        'O': (Decimal('16.00'), 2),
        'S': (Decimal('32.06'), 2),
        'Se': (Decimal('78.96'), 2),
        'Te': (Decimal('127.60'), 2),
        'Po': (Decimal('209'), 0),

        'F': (Decimal('19.00'), 2),
        'Cl': (Decimal('35.453'), 3),
        'Br': (Decimal('79.90'), 2),
        'I': (Decimal('126.91'), 2),
        'At': (Decimal('210'), 0),

        'Ne': (Decimal('20.179'), 3),
        'He': (Decimal('4.0026'), 4),
        'Ar': (Decimal('39.948'), 3),
        'Kr': (Decimal('83.80'), 2),
        'Xe': (Decimal('131.29'), 2),
        'Ce': (Decimal('140.12'), 2),
        'Pr': (Decimal('140.91'), 2),
        'Nd': (Decimal('144.24'), 2),
        'Pm': (Decimal('145'), 0),
        'Sm': (Decimal('150.4'), 1),
        'Eu': (Decimal('151.97'), 2),
        'Gd': (Decimal('157.25'), 2),
        'Tb': (Decimal('158.93'), 2),
        'Dy': (Decimal('162.50'), 2),
        'Ho': (Decimal('164.93'), 2),
        'Tm': (Decimal('168.93'), 2),
        'Yb': (Decimal('173.04'), 2),
        'Lu': (Decimal('174.97'), 2),
        'Th': (Decimal('232.04'), 2),
        'Pa': (Decimal('231.04'), 2),
        'U': (Decimal('238.03'), 2),
        'Np': (Decimal('237'), 0),
        'Pu': (Decimal('244'), 0),
        'Am': (Decimal('243'), 0),
        'Cm': (Decimal('247'), 0),
        'Bk': (Decimal('247'), 0),
        'Cf': (Decimal('251'), 0),
        'Es': (Decimal('252'), 0),
        'Fm': (Decimal('257'), 0),
        'Md': (Decimal('258'), 0),
        'No': (Decimal('259'), 0),
        'Lr': (Decimal('262'), 0),
    }
    element_info = elements[element]
    return element_info[0]


def get_gfm_of_part(input_str):
    gfm = Decimal()
    l = 0
    for i in range(len(input_str)-2):
        l = i
        if input_str[l] not in string.ascii_uppercase:
            continue
        else:
            element = input_str[i]
            if input_str[l+1] in string.ascii_lowercase:
                element += input_str[l+1]
                l += 1
            if input_str[l+1] in string.digits:
                multiple_str = ''
                l += 1
                for j in range(l, len(input_str)):
                    if input_str[j] in string.digits:
                        multiple_str += input_str[j]
                        l += 1
                    else:
                        break
            else:
                multiple_str = '1'

            gfm += Decimal(multiple_str) * get_atomic_mass(element)

    if l < len(input_str):
        if input_str[-1] in string.ascii_uppercase:
            if input_str[-2] in string.ascii_uppercase:
                gfm += get_atomic_mass(input_str[-2])
            gfm += get_atomic_mass(input_str[-1])
        elif input_str[-2] in string.ascii_uppercase:
            if input_str[-1] in string.digits:
                gfm += get_atomic_mass(input_str[-2]) * Decimal(input_str[-1])
            else:
                gfm += get_atomic_mass(input_str[-2:])

    return gfm


def gfm_of_whole(input_str):
    gfm = Decimal()
    if '(' in input_str:
        split_list = input_str.split('(')
        for i in split_list:
            if ')' in i:
                temp_list = i.split(')')
                if temp_list[-1].isdigit():
                    gfm += get_gfm_of_part(temp_list[0]) * \
                        Decimal(temp_list[-1])

            else:
                gfm += get_gfm_of_part(i)
    else:
        gfm = get_gfm_of_part(input_str)

    return gfm


def main():
    print(gfm_of_whole(sys.argv[1]))

if __name__ == '__main__':
    main()
