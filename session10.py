from collections import namedtuple
from faker import Faker
import datetime
from datetime import date
from datetime import time
import operator
from decimal import Decimal
from decimal import getcontext
import decimal
import contextlib
import time
from collections import Counter
import math
from math import isclose
fake = Faker()

def calculateage(birthDate: "date of birthof person") -> "Returns Age in years":
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

class Fprofile(namedtuple('Fprofile', ('name', 'sex', 'birthdate', 'blood_group', 'current_location'))):
    @classmethod
    def calculateage(cls, fprofile) -> "Returns Age in years":
        'This class method calculates age of given list of profile'
        birthDate = fprofile.birthdate
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    @classmethod
    def aver_age(cls, fprofiles) -> 'This class method calculates average age of given list of profiles':
        'This class method calculates average age of given list of profiles'
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        return sum(cls.calculateage(fprofile) for fprofile in fprofiles) / len(fprofiles)

    @classmethod
    def max_age(cls, fprofiles) -> "Returns Max age of given list of profiles":
        'This class method calculates max age of given list of profiles'
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        return max(cls.calculateage(fprofile) for fprofile in fprofiles)

    @classmethod
    def mean_current_location(cls, fprofiles) -> "Returns Mean current Location of given list of profiles":
        "Returns Mean current Location of given list of profiles"
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        mean_lat = sum(fprofile.current_location[0] for fprofile in fprofiles) / len(fprofiles)
        mean_long = sum(fprofile.current_location[1] for fprofile in fprofiles) / len(fprofiles)
        return (mean_lat, mean_long)

    @classmethod
    def largest_blood_type(cls, fprofiles) -> "Returns Largest Blood Group of given list of profiles":
        'This class method returns largest blood group of given list of profiles'
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        Blood_group_count = Counter(fprofile.blood_group for fprofile in fprofiles)
        return max(Blood_group_count, key=Blood_group_count.get)

Fprofile.__doc__ = 'Profile of Employees/User'
Fprofile.name.__doc__ = 'Name of Employees/User '
Fprofile.sex.__doc__ = 'Sex of Employees/User'
Fprofile.birthdate.__doc__ = 'Date of birth of Employees/User'
Fprofile.blood_group.__doc__ = 'Blood group of Employees/User'
Fprofile.current_location.__doc__ = 'Current location of Employees/User'

def function_profile_creation(count: "Number of profile to be created using faker"):
    "Returns  profile stored in named tuple and dictionary in list for user defined count"
    LIST_tuple = []
    LIST_dict = []
    for n in range(count):
        x = fake.profile()
        # Tuple based
        LIST_tuple.append(Fprofile(x['name'], x['sex'], x['birthdate'], x['blood_group'], x['current_location']))
        # Dictionary based
        LIST_dict.append({'name': x['name'], 'sex': x['sex'], 'birthdate': x['birthdate'], 'blood_group': x['blood_group'],'current_location': x['current_location']})
    return LIST_tuple, LIST_dict

def function_profile_data_tuple_process(LIST: "List of Named tuple"):
    """
    This function returns following for given list of profiles stores in Namedtuple
    - Average age in given set of profiles
    - Age of oldest person in given set of profiles
    -mean location of  in given set of profiles
    -largest_blood_type  in given set of profiles
    """
    average_age = Fprofile.aver_age(LIST)
    oldest_person_age = Fprofile.max_age(LIST)
    mean_current_location = Fprofile.mean_current_location(LIST)
    largest_blood_type = Fprofile.largest_blood_type(LIST)
    return average_age, oldest_person_age, mean_current_location, largest_blood_type

def function_profile_data_dict_process(LIST_d: "List of dictionary"):
    """
    This function returns following for given list of profiles stores in Dictionary
    - Average age in given set of profiles
    - Age of oldest person in given set of profiles
    -mean location of  in given set of profiles
    -largest_blood_type  in given set of profiles
    """
    oldest_person_age_d = 0
    blood_group_count_d = {'O+': 0, 'B-': 0, 'AB+': 0, 'B+': 0, 'O-': 0, 'AB-': 0, 'A-': 0, 'A+': 0}
    average_age_d = 0
    mean_current_location_d = (0, 0)
    average_age_d = 0
    Num_profile = len(LIST_d)
    for n in range(Num_profile):
        ##Max age
        age = calculateage(LIST_d[n]['birthdate'])
        oldest_person_age_d = max(oldest_person_age_d, age)
        ##average age
        age = calculateage(LIST_d[n]['birthdate'])
        average_age_d = (average_age_d * n + age) / (n + 1)
        ##mean_current_location
        mean_current_location_d = Decimal(
            (mean_current_location_d[0] * n + LIST_d[n]['current_location'][0]) / (n + 1)), Decimal(
            (mean_current_location_d[1] * n + LIST_d[n]['current_location'][1]) / (n + 1))
        ###Max Blood group
        blood_group_count_d[LIST_d[n]['blood_group']] = blood_group_count_d[LIST_d[n]['blood_group']] + 1
    largest_blood_type_d = (max(blood_group_count_d.items(), key=operator.itemgetter(1))[0])
    return average_age_d, oldest_person_age_d, mean_current_location_d, largest_blood_type_d
