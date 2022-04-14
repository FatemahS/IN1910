#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:00:32 2020

@author: fatemahsyed
"""

"""Exercise 1"""
def add(x, y):
    return x+y

"""Exercise 4"""
def factorial_exercise_4(num):
    factorial = 1
    for i in range (1, int(num)+1):
        factorial = factorial * i
    return factorial

def sin_exercise_4(x, N):
    sin = 0
    for n in range (0, N+1):
        sin = sin + ((-1)**n*x**(2*n+1))/(factorial_exercise_4(2*n+1))
    return sin

def divide_exercise_4(x_, y_):
    return x_/y_

"""Two functions that I chose myself"""

def add_one_exercise_4(n1):
    """The function adds one to the input-number"""
    return n1+1

def double_number_exercise_4(n2):
    """The function doubles the input_number"""
    return n2*2

