from src.myfuns import GetTopNCityByCountry_python, GetTopNCityByCountry_mysqlproc

def setup_module(module):
    print('\n *****SETUP*****')

def teardown_module(module):
    print('\n ******TEARDOWN******')
    
def test_ResultsBetweenPythonAndSQL():
    top_n = 3
    min_n = 20 

    result_py = GetTopNCityByCountry_python(top_n, min_n)
    result_mysql = GetTopNCityByCountry_mysqlproc(top_n, min_n)
    
    assert result_py.equals(result_mysql)
    