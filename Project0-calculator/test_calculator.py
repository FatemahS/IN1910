#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:00:03 2020

@author: fatemahsyed
"""
import calculator
import math
import pytest

"""Exercise 1"""
def test_add_int_exercise_1():
    integral_ = calculator.add(1,2)
    assert integral_ == 3 

"""Exercise 2""" 
def test_add_float_exercise_2():
    float_ = calculator.add(0.1, 0.2)
    assert  abs(float_ - 0.3) < 1e-10
    
"""Exercise 3"""       
def test_add_string_exercise_3():
    string_ = calculator.add('s1', 's2')
    assert string_ == 's1' + 's2'
    
"""Exercise 4"""
def test_factorial_exercise_4():
    fact = calculator.factorial_exercise_4(5) 
    assert fact == math.factorial(5)

def test_sin_exercise_4():
    sinus = calculator.sin_exercise_4(2,50)
    epsilon = 1e-10
    assert abs(math.sin(2) -sinus) < epsilon
    
def test_divide_exercise_4():
    number = calculator.divide_exercise_4(10, 2)
    assert number == int(5)
    
"""Test-functions for the two functions that I chose myself"""

def test_add_one_exercise_4():
    num_ = calculator.add_one_exercise_4(8)
    assert num_ == int(9)

def test_double_number_exercise_4():
    double_num = calculator.double_number_exercise_4(10)
    assert double_num == int(20)

"""Exercise 5"""
def test_add_TypeError_exercise_5():
    """Test passes only if TypeError is raised"""
    with pytest.raises(TypeError):
        assert calculator.add("High", 5)
 
def test_divide_ZeroDivision_exercise_5():
    """Test passes only if ZeroDivisionError is raised"""
    with pytest.raises(ZeroDivisionError):
         assert calculator.divide_exercise_4(3,0)

"""Exercise 6"""
"""Parameterized test functions for the add-function"""
@pytest.mark.parametrize("input_, exp_output", [[(1,2), 3], [(0.1, 0.2), 0.1+0.2],[('s1','s2'),'s1'+'s2']])
def test_add_exercise_6(input_, exp_output):
    assert calculator.add(input_[0],input_[1]) == exp_output

"""Parameterized test function for factorial-function"""
@pytest.mark.parametrize("input_, exp_output", [(5, 120)])
def test_factorial_exercise_6(input_, exp_output):
    assert calculator.factorial_exercise_4(input_) == exp_output
    
"""Parameterized test function for sin-function"""
@pytest.mark.parametrize("input_, exp_output", [((2,50), math.sin(2))])
def test_sin_exercise_6(input_, exp_output):
    assert calculator.sin_exercise_4(input_[0],input_[1]) == exp_output 

"""Parameterized test function for divide-function"""
@pytest.mark.parametrize("input_, exp_output", [((10,2), 5)])
def test_divide_exercise_6(input_, exp_output):
    assert calculator.divide_exercise_4(input_[0],input_[1]) == exp_output
    
"""Parameterized test function for my own 'add_one'-function"""
@pytest.mark.parametrize("input_, exp_output", [(8, 9)])
def test_add_one_exercise_6(input_, exp_output):
    assert calculator.add_one_exercise_4(input_) == exp_output
    
"""Parameterized test function for my own 'double_number'-function"""
@pytest.mark.parametrize("input_, exp_output", [(10, 20)])
def test_double_number_exercise_6(input_, exp_output):
    assert calculator.double_number_exercise_4(input_) == exp_output

"""Parameterized test function for add_TypeError-function using pytest"""
@pytest.mark.parametrize("input_, exp_output", [(("High ", 5), "High 5")])
def test_add_TypeError_exercise_6(input_, exp_output):
        with pytest.raises(TypeError):
            assert calculator.add(input_[0],input_[1]) == exp_output

"""Parameterized test function for divide_ZeroDivision-function using pytest"""
@pytest.mark.parametrize("input_, exp_output", [((3, 0), 3)])
def test_divide_ZeroDivision_exercise_6(input_, exp_output):
    with pytest.raises(ZeroDivisionError):
        assert calculator.divide_exercise_4(input_[0],input_[1]) == exp_output


