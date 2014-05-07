import numpy as np
import datetime
import dateutil

import sunpy.lightcurve

def check_float(test, varname=None):
    """Raises Exception if input isn't numpy array of dtype float64.

    Parameters
    ----------
    test : variable to test
    varname : string, optional
              name of variable.  (Printed if exception is raised.)
    """
    if type(varname) is not str:
        varname = "This variable"
    if type(test) is not np.ndarray or (test.dtype.type is not np.float64 and \
      test.dtype.type is not np.float32 and test.dtype.type is not np.float16):
        raise TypeError(varname + " must be a numpy array of type float.")

def check_goessat(test, varname=None):
    """Raises Exception if test isn't an int of a GOES satellite, i.e > 1.

    Parameters
    ----------
    test : variable to test
    varname : string, optional
              name of variable.  Default = 'satellite'
              (Printed if exception is raised.)

    Returns
    -------
    test : int
           Returned as original int if exceptions aren't raised, or a
           new int converted from input if input is a valid date string.
    """
    if type(varname) is not str:
        varname = "satellite"
    if type(test) is not int:
        if type(test) is str:
            try:
                test = int(test)
            except ValueError:
                raise TypeError(varname + " must be an integer.")
        else:
            raise TypeError(varname + " must be an integer.")
    if test < 1:
        raise ValueError(varname + " must be the number (integer) of a " + \
                         "valid GOES satellite.")
    return test

def check_photospheric(test, varname=None):
    """Raises Exception if photospheric keyword isn't True or False.

    Parameters
    ----------
    test : variable to test
    varname : string, optional
              name of variable.  Default = 'photospheric'
              (Printed if exception is raised.)
    """
    if type(varname) is not str:
        varname = "photospheric"
    if type(test) is not bool:
        raise TypeError(varname + " must be True or False.  \n" +
                        "False: assume coronal abundances (default).  \n" +
                        "True: assume photosperic abundances.")

def check_date(test, varname=None):
    """
    Raise Exception if test isn't/can't be converted to datetime object.

    Parameters
    ----------
    test : variable to test
    varname : string, optional
              name of variable.  Default = 'date'
              (Printed if exception is raised.)

    Returns
    -------
    test : datetime object
           Returned as original datetime object if exceptions aren't
           raised, or a new datetime object converted from input if
           input is a valid date string.
    """
    if type(varname) is not str:
        varname = "date"
    if type(test) is not datetime.datetime:
        if type(test) is str:
            try: 
                test = dateutil.parser.parse(test)
            except TypeError:
                raise TypeError(varname + " must be a datetime object.")
        else:
            raise TypeError(varname + " must be a datetime object.")
    return test
    
def check_goeslc(test, varname=None):
    """Raise Exception if test is not a GOESLightCurve object.

    Parameters
    ----------
    test : variable to test
    varname : string, optional
              name of variable.  (Printed if exception is raised.)
    """
    if type(varname) is not str:
        varname = "This variable"
    if type(test) is not sunpy.lightcurve.sources.goes.GOESLightCurve:
        raise TypeError(varname + " must be GOESLightCurve object.")
