# %%
import os
from typing import NamedTuple
import pandas as pd
from sqlalchemy import create_engine

# %%
class DefaultValues(NamedTuple):
    MYSQL_DATA_HOST = os.environ.get("MYSQL_DATA_HOST", "db")
    MYSQL_DATA_PORT = 3306
    MYSQL_DATA_USER = os.environ.get("MYSQL_DATA_USER", "")
    MYSQL_DATA_PASSWORD = os.environ.get("MYSQL_DATA_PASSWORD", "")
    MYSQL_DATA_DATABASE = os.environ.get("MYSQL_DATA_DATABASE", "world")
    SQLQUERY_GetDataFromTable_City = "SELECT * FROM city;"
    SQLQUREY_CallProc_GetTopNCityByCountry = "CALL GetTopNCityByCountry({top_n}, {min_n});"

class ColumnNames(NamedTuple):
    population = "Population"
    name = "Name" 
    countrycode = "CountryCode"
    rank_in_country = "rank_in_country"
    count_in_country = "count_in_country"


def GetMySQLAddress():
    
    dv = DefaultValues()
    address = (
        f"mysql+pymysql://{dv.MYSQL_DATA_USER}:{dv.MYSQL_DATA_PASSWORD}"
        f"@{dv.MYSQL_DATA_HOST}:{dv.MYSQL_DATA_PORT}/{dv.MYSQL_DATA_DATABASE}"
    )
    # print(address)

    return address


def GetMySQLConnect():
    address = GetMySQLAddress()
    engine = create_engine(address)
    mysql_conn = engine.connect()

    return mysql_conn


def RunQueryAgainstMySQL(query: str) -> pd.DataFrame: 
    
    mysql_conn = GetMySQLConnect()
    df = pd.read_sql_query(query, mysql_conn)
    mysql_conn.close()

    return df


def SelectTopNByGroup(df_bygroup: pd.DataFrame, top_n: int, min_n: int):
    
    n_rows = df_bygroup.shape[0]
    if n_rows < min_n:
        output = None

    else:
        cols = ColumnNames()

        df_top_n = (df_bygroup
                    .sort_values([cols.population, cols.name], ascending=True)
                    .assign(rank_in_country = lambda x: x[cols.population].rank(method='first'))
                    .astype({cols.rank_in_country: int})
                    .assign(count_in_country = n_rows)
                    .head(top_n)
                    .reset_index(drop=True))
        output = df_top_n

    return output

def GetTopNCityByCountry_python(top_n: int, min_n: int) -> pd.DataFrame:

    dv = DefaultValues()
    query = dv.SQLQUERY_GetDataFromTable_City
    df = RunQueryAgainstMySQL(query)

    cols = ColumnNames
    result = (df
                .groupby(cols.countrycode, group_keys=False)
                .apply(lambda x: SelectTopNByGroup(x, top_n, min_n))
                .reset_index(drop = True)
                .sort_values(by = [cols.countrycode, cols.rank_in_country, cols.count_in_country], 
                            ascending = [True, True, True]))

    return result


def GetTopNCityByCountry_mysqlproc(top_n: int, min_n: int) -> pd.DataFrame:

    dv = DefaultValues()
    query = dv.SQLQUREY_CallProc_GetTopNCityByCountry.format(top_n = top_n, min_n = min_n);
    result = RunQueryAgainstMySQL(query)

    return result

# %%
if __name__ == '__main__':
    
    top_n = 3
    min_n = 20 

    result_py = GetTopNCityByCountry_python(top_n, min_n)
    result_mysql = GetTopNCityByCountry_mysqlproc(top_n, min_n)

    # pd.testing.assert_frame_equal(result_py, result_mysql)
    all_equals = result_py.equals(result_mysql)
    print(f'Are the results generated from python code and mysql the same? {all_equals}')
    