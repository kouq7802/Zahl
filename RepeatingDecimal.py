#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = '0.0.1'

'''
Author: KouQ7802
Created on Wednesday, January 20th, 2016
'''

## import required libraries
import sys

## define functions
def read_param():
    try:
        n = int(eval(sys.argv[1]))
        if n >= 0:
            return n
        else:
            print('[Error] Program aborted!!')
            print('Please enter natural number')
            return None
    except ValueError:
        print('[Error] Program aborted!!')
        print('Please enter natural number')
    except NameError:
        print('[Error] Program aborted!!')
        print('Please enter natural number')

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
        
    return {'n':n, 's':s, 'g':g}

def main():
    n = read_param()
    if isinstance(n, int):
        result = find_recurring_cycle(n)
        print('='*36+'[RESULT]'+'='*36)
        print(' 1/', n)
        print('-'*80)
        print(' length of recurring cycle      :', result['g']-result['s']+1)
        print(' start point of recurring cycle :', result['s'])
        print(' end point of recurring cycle   :', result['g'])
        #print(result)
        print('='*80)
    else:
        pass

if __name__ == '__main__':
    main()
## end
