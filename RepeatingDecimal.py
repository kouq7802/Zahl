#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = '0.0.2'

'''
Author: KouQ7802
Created on Wednesday, January 20th, 2016
'''

## import required libraries
import sys

## define functions
def read_param():
    ERROR_MESSAGE = '[Error] Program aborted!!\nPlease enter Natural Number'
    try:
        n = int(eval(sys.argv[1]))
        if n >= 0:
            return n
        else:
            raise ValueError
    except ValueError:
        print(ERROR_MESSAGE)
        sys.exit()
    except NameError:
        print(ERROR_MESSAGE)
        sys.exit()
    except SyntaxError:
        print(ERROR_MESSAGE)
        sys.exit()

def find_recurring_cycle(n):
    rabbit = 1
    turtle = 1
    s = 0
    g = 0

    while True:
        rabbit = (rabbit * 10) % n
        rabbit = (rabbit * 10) % n
        turtle = (turtle * 10) % n
        if rabbit == turtle:
            break
        else:
            continue

    if rabbit != 0:
        rabbit = 1
        s = 1
        while turtle != rabbit:
            s += 1
            turtle = (turtle * 10) % n
            rabbit = (rabbit * 10) % n

        rabbit = (rabbit *10) % n
        g = s

        while turtle != rabbit:
            g += 1
            rabbit = (rabbit * 10) % n

    return {'n':n, 'startpoint':s, 'endpoint':g}

def main():
    n = read_param()
    result = find_recurring_cycle(n)
    print('='*36+'[RESULT]'+'='*36)
    print(' 1 /', n)
    print('-'*80)
    if result['startpoint'] == 0:
        print(' Finite Decimal')
    elif result['startpoint'] == 1:
        print(' Pure Recurring Decimal')
    else:
        print(' Mixed Recurring Decimal')
    print('-'*80)
    print(' length of recurring cycle      :', result['endpoint']-result['startpoint']+1)
    print(' start point of recurring cycle :', result['startpoint'])
    print(' end point of recurring cycle   :', result['endpoint'])
    #print(result)
    print('='*80)

if __name__ == '__main__':
    main()
## end
