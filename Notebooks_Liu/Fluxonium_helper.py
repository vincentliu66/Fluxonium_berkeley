"""
20230801, Chuan-Hong Liu, this is to help the numerical simulation such as
data saving, file saving.
"""

from os import listdir
from os.path import isfile, join
import numpy as np

def _getFileNumber(basepath, expname, file_format):
    """
    to save file automatically
    :param basepath: the working directory
    :param expname: the experiment name
    :return: the file number of the next file to be saved
    TODO: set max number
    """
    print('in _getFileNumber file_format=', file_format)
    file_number_int = 1000
    file_number = str(file_number_int)
    ### First find the directory,
    mypath = basepath+expname+'/'
    # print('expname+file_number+file_format=', expname+file_number+file_format)

    file_name_len = len(expname+'_'+file_number+file_format)
    onlyfiles = [f for f in listdir(mypath) if len(f)==file_name_len]

    # print('onlfiles=', onlyfiles)
    fileName = expname+'_'+file_number+file_format
    fileNameMax = expname+'_'+'1999'+file_format
    # if fileNameMax in onlyfiles: raise error
    if onlyfiles == []:
        print('I am here')
        file_number = str(file_number_int)
    else:   # not empty, need to find the largest file number already saved
        print('There are already some files saved')
        ### Find the largest file number
        file_numbers = np.array([])
        for f in onlyfiles:
            f_n = int(f[len(expname)+1:len(expname)+5])
            print('f_n=', f_n)
            file_numbers = np.append(file_numbers, f_n)
            print('file_numbers=', file_numbers)
        file_number_int = int(max(file_numbers))
        print('file_number_int=', file_number_int)
        file_number = str(file_number_int+1)
        print('file_number=', file_number)
    # open directory and find the files saved in there
    # if there is/are files, find the largest number and return the largest number + 1
    # if there is no file, give it 000

    return file_number

def get_file_dir_name(basepath, expname, f_t):
    print('file_format=', f_t)
    file_number = _getFileNumber(basepath, expname, file_format=f_t)
    file_dir_name = basepath+expname+'/'+expname+'_' +file_number+f_t
    return file_dir_name

