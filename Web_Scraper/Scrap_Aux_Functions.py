# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:59:51 2021

@author: FAKENAME
"""

import re, socket

def extract_string(all_str, pre_str, post_str):

    return_str = None
    
    r = re.compile(pre_str + '(.*?)' + post_str)
    m = r.search(all_str)
    if m:
        return_str = m.group(1)
    
    return return_str

def remove_non_ascii(string):
    
    return_str = string
    
    # only operate on objects that are strings
    if isinstance(return_str, str):
        # Remove non-Ascii characters
        return_str = return_str.encode("ascii", errors="ignore").decode()
        
        # Change all white space characters to spaces
        return_str = re.sub(r'\s+', ' ', return_str)
    
    return return_str

def is_connected_to_internet():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def compare_arr_str(arr1, arr2):
    """
    Function that takes two arrays of str or str and compares them.
    The string from one can be a sub string of the 
    """
    
    # Both str
    if (isinstance(arr1, str) and isinstance(arr2, str)):
        if arr1 in arr2:
            return True
    
    # First str
    elif (isinstance(arr1, str) and isinstance(arr2, list)):
        for string2 in arr2:
            if arr1 in string2:
                return True
        
        # if no match has been found return False
        return False
    
    # Second str
    elif (isinstance(arr1, list) and isinstance(arr2, str)):
        for string1 in arr1:
            if string1 in arr2:
                return True
        
        # if no match has been found return False
        return False            
    
    # Both arrays
    elif (isinstance(arr1, list) and isinstance(arr2, list)):
        for string1 in arr1:
            for string2 in arr2:
                if string1 in string2:
                    return True

        # if no match has been found return False
        return False  
    
    # If none of the previous options are matched test if both objects are equal otherwise return false
    elif (arr1 == arr2):
        return True
    else:
        return False