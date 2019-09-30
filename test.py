from function_storage import *
import pytest
#this file has to run by pytest.
def test_example_5X5_chris():
    A = [
    [1,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [1,1,0,0,0],
    [0,0,0,0,0]]
    B = [
    [1,0,0,1,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
    C = [[-1] * 5 for i in range(5)]
    calculate(A,B,C,5)
    convert_to_one(C,5)
    assert C == [
        [1,0,0,1,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
        [1,0,0,1,0],
        [0,0,0,0,0]]

def test_example_2X2():
    A = [
    [1,0],
    [0,0]]
    B = [
    [1,1],
    [1,0]]
    calculate(A,B,C,2)
    convert_to_one(C,2)
    assert C == [
        [1,1],
        [0,0]]
