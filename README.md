# Readme File for Assignment for Session 10 - Tuples & Named Tuples and Modules
### Created by Sriram Iyengar
## Session 10 - Tuples & Named Tuples and Modules
- Tuples as a Data Structure
- Named Tuple
- Named Tuple - Modifying & Extending
- Named Tuple - DocString & Default Values
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Assignment Requirment 
- Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings). - 250
- Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250
- Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. 
  Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Functions/class in Assignment file


###  calculateage (birthDate: "date of birthof person") -> "Returns Age in years":
- calculates age of person based on date of birth as input
### class Fprofile (namedtuple('Fprofile', ('name', 'sex', 'birthdate', 'blood_group', 'current_location'))):
##  calculateage(cls, fprofile) -> "Returns Age in years":
- "This class method calculates age of given list of profile"
##  aver_age (cls, fprofiles) -> 'This class method calculates average age of given list of profiles':
-"This class method calculates average age of given list of profiles"
##  max_age (cls, fprofiles) -> "Returns Max age of given list of profiles":
- "This class method calculates max age of given list of profiles"
##  mean_current_location (cls, fprofiles)
- "This class methodReturns Mean current Location of given list of profiles"
##  largest_blood_type(cls, fprofiles)
- "Returns Largest Blood Group of given list of profiles"
***Docstring for variables ***
Fprofile.__doc__ = 'Profile of Employees/User'
Fprofile.name.__doc__ = 'Name of Employees/User '
Fprofile.sex.__doc__ = 'Sex of Employees/User'
Fprofile.birthdate.__doc__ = 'Date of birth of Employees/User'
Fprofile.blood_group.__doc__ = 'Blood group of Employees/User'
Fprofile.current_location.__doc__ = 'Current location of Employees/User'

###  function_profile_creation (count: "Number of profile to be created using faker"):
- "Returns  profile stored in named tuple and dictionary in list for user defined count"

###  function_profile_data_tuple_process (LIST: "List of Named tuple"):
    """
    This function returns following for given list of profiles stores in Namedtuple
    - Average age in given set of profiles
    - Age of oldest person in given set of profiles
    -mean location of  in given set of profiles
    -largest_blood_type  in given set of profiles
    """


###  function_profile_data_dict_process (LIST_d: "List of dictionary"):
    """
    This function returns following for given list of profiles stores in Dictionary
    - Average age in given set of profiles
    - Age of oldest person in given set of profiles
    -mean location of  in given set of profiles
    -largest_blood_type  in given set of profiles
    """
### Stock_weight_norm = namedtuple('Stock_weight_norm', ('name', 'nw'))
-Stock_weight_norm.__doc__ = 'Stock Weight Details for Day trade'
-Stock_weight_norm.name.__doc__ = 'Name of Stock'
-Stock_weight_norm.nw.__doc__ = 'Normilized weight of Stock that day'


### class Stock (namedtuple('Stock', ('name', 'symbol', 'open', 'high', 'close', 'low', 'weight'))):
## def normilized_weight(cls, stocks) -> "returns normalized values for ":
-'This class method calculates normalized weights for given set of weights '
## stock_ex_value(cls, stocks) -> "returns normalized values for ":
- 'This class method calculates normalized weights for given set of weights '
- Stock.__doc__ = 'Stock Detail for Day trade'
- Stock.name.__doc__ = 'Name of Stock'
- Stock.symbol.__doc__ = 'symbol of Stock'
- Stock.open.__doc__ = 'Opening Value of Stock that day'
- Stock.high.__doc__ = 'highest Value of Stock that day'
- Stock.close.__doc__ = 'closing highest Value of Stock that day'
- Stock.low.__doc__ = 'closing lowest Value of Stock that day'
- Stock.weight.__doc__ = 'weight Stock that day'

###  function_fstock_creation(count: "Number of stock to be created using faker"):
    "Returns  profile stored in named tuple in list for user defined count"


## Functions used in Test File
### test_readme_exists 
- checks if Readme files exists

### test_readme_contents length 
- checks the content length of  Readme file
### test_readme_proper_description 
- checks the content length of  Readme file

### test_readme_file_for_formatting 
- checks the formatting of  Readme file

### test_indentations 
- checks if the Assignment code is properly formated

### test_function_name_had_cap_letter 
- checks if the Assignment code is function has capital letters

###  test_creation_profile():
    """
    This Test function checks if created profile are stored properly
    """

###  test_output_named_tuple_vs_dictionary():
    """
    This Test checks speed of Named tuple vs dictionary for 10000 profiles and 100 runs
    """

###  test_output_named_tuple_vs_dictionary():
    """
    This Test checks content of Named tuple vs dictionary for 1 profiles.
    """

###  test_stock_named_tuple_functions():
    """
    This Test Function checks the output of stock named tupple and its class method for 100 stocks.
    """

***
> ![My Image](https://github.com/rsriramiyengar/EPAi-session10-rsriramiyengar/blob/master/images/Image01.JPG)
***

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder
