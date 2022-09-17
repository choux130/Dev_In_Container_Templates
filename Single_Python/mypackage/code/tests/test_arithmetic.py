from mypackage.arithmetic import arithmetic

def setup_module(module):
    print('\n *****SETUP*****')

def teardown_module(module):
    print('\n ******TEARDOWN******')
    
def test_addition():
    assert arithmetic.add(1, 2) == 3
    
def test_subtraction():
    assert arithmetic.subtract(2, 1) == 1

def test_multiplication():
    assert arithmetic.multiply(5, 5) == 25

def test_division():
    assert arithmetic.divide(8, 2) == 4