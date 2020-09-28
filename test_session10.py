import pytest
import random
import string
import pytest


import session10
from session10 import Fprofile
from session10 import function_profile_creation
from session10 import function_profile_data_tuple_process
from session10 import function_profile_data_dict_process
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
    LIST_tuple, LIST_dict = function_profile_creation(1)
    assert LIST_tuple[0][0]==LIST_dict[0]['name'] ,"Name is not getting stored properly"
    assert LIST_tuple[0][1] == LIST_dict[0]['sex'], "sex of profile is not getting stored properly"
    assert LIST_tuple[0][2] == LIST_dict[0]['birthdate'], "birthdate of profile is not getting stored properly"
    assert LIST_tuple[0][3] == LIST_dict[0]['blood_group'], "blood_group of profile is not getting stored properly"
    assert LIST_tuple[0][4] == LIST_dict[0]['current_location'], "current_location' of profile is not getting stored properly"


def test_output_named_tuple_vs_dictionary():
    """
    This Test checks speed of Named tuple vs dictionary for 10000 profiles and 100 runs
    """
    Num_profile = 10000
    Num_run = 100
    LIST_tuple, LIST_dict = function_profile_creation(Num_profile)
    ### Named Tuple
    start1 = time.perf_counter()
    for n in range(Num_run):
        average_age, oldest_person_age, mean_current_location, largest_blood_type = function_profile_data_tuple_process(
            LIST_tuple)
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


