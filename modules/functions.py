import sys
import os 
import platform
import locale

def get_current_path():
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.dirname(directory)
    return directory
    
def set_locale(lokal):
    if platform.system() == 'Windows':
        mapper = {
            'deutsch':'deu_deu'
        }
    elif platform.system() == 'Linux':
        mapper = {
            'deutsch':'deu_deu'
        }
    locale.setlocale(locale.LC_ALL, mapper[lokal])
    
def total_keys(test_dict): 
    return (0 if not isinstance(test_dict, dict)  
    else len(test_dict) + sum(total_keys(val) for val in test_dict.values())) 

def dic_iterieren(x):
    for key in x.keys():
        return x[key]