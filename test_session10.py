import pytest
import random
import string
import pytest


import session10
from session10 import Fprofile
from session10 import function_profile_creation
from session10 import function_profile_data_tuple_process
from session10 import function_profile_data_dict_process
from session10 import Stock_weight_norm
from session10 import Stock
from session10 import function_fstock_creation
import os
import inspect
import re
import math
from math import isclose
import random
import decimal
from decimal import Decimal
import time


README_CONTENT_CHECK_FOR = [
    'calculateage',
    'Fprofile',
    'calculateage',
    'aver_age',
    'max_age',
    'mean_current_location',
    'largest_blood_type',
    'function_profile_creation',
    'function_profile_data_tuple_process',
    'function_profile_data_dict_process',
    'Stock_weight_norm',
    'Stock',
    'function_fstock_creation'
]



def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_creation_profile():
    """
    This Test function checks if created profile are stored properly
    """
    tuple_NT, LIST_dict = function_profile_creation(1)
    assert tuple_NT[0][0]==LIST_dict[0]['name'] ,"Name is not getting stored properly"
    assert tuple_NT[0][1] == LIST_dict[0]['sex'], "sex of profile is not getting stored properly"
    assert tuple_NT[0][2] == LIST_dict[0]['birthdate'], "birthdate of profile is not getting stored properly"
    assert tuple_NT[0][3] == LIST_dict[0]['blood_group'], "blood_group of profile is not getting stored properly"
    assert tuple_NT[0][4] == LIST_dict[0]['current_location'], "current_location' of profile is not getting stored properly"


def test_output_named_tuple_vs_dictionary():
    """
    This Test checks speed of tuple of Named tuple vs List dictionary for 10000 profiles and 100 runs
    """
    Num_profile = 10000
    Num_run = 1000
    tuple_NT, LIST_dict = function_profile_creation(Num_profile)
    ### Named Tuple
    start1 = time.perf_counter()
    for n in range(Num_run):
        average_age, oldest_person_age, mean_current_location, largest_blood_type = function_profile_data_tuple_process(
            tuple_NT)
    end1 = time.perf_counter()
    delta1 = (end1 - start1) / Num_run
    ####
    start2 = time.perf_counter()
    for n in range(Num_run):
        average_age_d, oldest_person_age_d, mean_current_location_d, largest_blood_type_d = function_profile_data_dict_process(
            LIST_dict)
    end2 = time.perf_counter()
    delta2 = (end2 - start2) / Num_run
    #print(f"Named tuple is faster than dictionary by  {((delta2 / delta1 - 1) * 100):0.2f}% ")
    assert isclose(average_age,average_age_d), "Average age cannot be different for Named Tuple and Dictionary list"
    assert oldest_person_age == oldest_person_age_d, "Max age cannot be different for Named Tuple and Dictionary list"
    assert isclose(mean_current_location[0], mean_current_location_d[0]), "Mean location cannot be different for Named Tuple and Dictionary list"
    assert isclose(mean_current_location[1], mean_current_location_d[1]), "Mean location cannot be different for Named Tuple and Dictionary list"
    assert largest_blood_type == largest_blood_type_d, "Max Blood Type cannot be different for same group"
    assert delta2>delta1 ,"Dictionary cannot be faster than named tuple"


def test_output_named_tuple_vs_dictionary():
    """
    This Test checks content of Named tuple vs dictionary for 1 profiles.
    """
    Stock_tuple,Stock_list_dict = function_fstock_creation(1)
    assert Stock_tuple[0][0]==Stock_list_dict[0]['name'] ,"Name is not getting stored properly"
    assert Stock_tuple[0][1] == Stock_list_dict[0]["symbol"], "symbol is not getting stored properly"
    assert Stock_tuple[0][2] == Stock_list_dict[0]["open"], "open is not getting stored properly"
    assert Stock_tuple[0][3] == Stock_list_dict[0]["high"], "high is not getting stored properly"
    assert Stock_tuple[0][4] == Stock_list_dict[0]["close"], "close is not getting stored properly"
    assert Stock_tuple[0][5] == Stock_list_dict[0]["low"], "low is not getting stored properly"
    assert Stock_tuple[0][6] == Stock_list_dict[0]["weight"], "weight is not getting stored properly"

def test_stock_named_tuple_functions():
    """
    This Test Function checks the output of stock named tuple and its class method for 100 stocks.
    """
    Stock_100, Stock_list_dic = function_fstock_creation(100)
    nw_tab = Stock.normilized_weight(Stock_100)
    Exch_open, Exch_high, Exch_close, Exch_low = Stock.stock_ex_value(Stock_100)
    Exch_open1, Exch_high1, Exch_close1, Exch_low1 = 0, 0, 0, 0
    for n in range(len(Stock_100)):
        Exch_open1 += Stock_100[n][2] * nw_tab[n][1]
        Exch_high1 += Stock_100[n][3] * nw_tab[n][1]
        Exch_close1 += Stock_100[n][4] * nw_tab[n][1]
        Exch_low1 += Stock_100[n][5] * nw_tab[n][1]
    assert isclose(Exch_open,Exch_open1),"calculation of Exchange open value is wrong"
    assert isclose(Exch_high,Exch_high1),"calculation of Exchange  high value is wrong"
    assert isclose(Exch_close,Exch_close1),"calculation of Exchange close value is wrong"
    assert isclose(Exch_low,Exch_low1),"calculation of Exchange low value is wrong"





