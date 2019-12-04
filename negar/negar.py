# Copyright SYS113 2019. MIT license , see README.md file.

# import libraries ...

from tzlocal import get_localzone
from datetime import datetime
from platform import system, release, machine
from getpass import getuser
from os.path import isfile
from inspect import getframeinfo, stack
from json import load


# create log function ...

def log(text=None, save=None, size=None):
    # helper function for negar module errors printing
    def err_temp_func(file_, line, problem):
        error_template = 'negar module - error | python file : {} | line : {} | problem : {}'
        return error_template.format(file_, line, problem)

    # find (filename or line) python file ...

    x = stack()[1]
    x = x[0]
    get_log_file_python_file_name_or_line = getframeinfo(x)

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    '''                                                    
                                                    'find line in python file' variable is 'line_python_file'
                                                    'find python file name' variable is 'python_file'
                                                    'save log in a file' variable is 'log_file'
                                                    'log text' variable is 'log_text'
                                                    'set log file size' variable is 'log_file_size'
    '''
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # set value for find line in python file ...

    line_python_file = str(get_log_file_python_file_name_or_line.lineno)

    # set value for find python file name ...

    python_file_name = str(get_log_file_python_file_name_or_line.filename)

    if python_file_name == '<stdin>':
        python_file = 'interpreter'
    elif len(python_file_name) < 18:
        python_file = python_file_name
    else:
        print(err_temp_func(python_file_name, line_python_file, 'maximum size of python file name is 15 character ...'))
        return

    # set value for save log in a file ...

    if isinstance(save, str):
        log_file = save
    elif save is None:
        log_file = 'log.txt'
    else:
        print(err_temp_func(python_file_name, line_python_file, '\'save\' type is not str ...'))
        return

    # set value for log text ...

    if text is None:
        print(err_temp_func(python_file_name, line_python_file, '\'text\' value is empty ...'))
        return
    elif not isinstance(text, str):
        print(err_temp_func(python_file_name, line_python_file, '\'text\' type is not str ...'))
        return
    elif text == '':
        print(err_temp_func(python_file_name, line_python_file, '\'text\' value is empty ...'))
        return
    else:
        log_text = text

    # set value for log file size ...

    if size is None:
        log_size = 2
    elif not isinstance(size, int):
        print(err_temp_func(python_file_name, line_python_file, '\'size\' type is not str ...'))
        return
    elif size > 5:
        print(err_temp_func(python_file_name, line_python_file, '\'size\' value range is not (1 ... 5) ...'))
        return
    elif size == 0:
        print(err_temp_func(python_file_name, line_python_file, '\'size\' value is not in range (1 ... 5) ...'))
        return
    else:
        log_size = size

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
                                        'write python file name in log file' variable is 'log_file_python_file_name'
                                        'write line of python file in log file' variable is 'log_file_python_file_line'
                                        'write log text in log file' variable is 'log_file_text'
                                        'log file name' variable is 'log_file_name'
                                        'log file size' variable is 'log_file_size'
    '''
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # check cheacter size ...

    if (log_size == 1) and (len(log_text) > 69):
        print(err_temp_func(python_file_name, line_python_file, '\'size = 1\' maximum 69 character support ...'))
        return
    elif (log_size == 2) and (len(log_text) > 93):
        print(err_temp_func(python_file_name, line_python_file, '\'size = 2\' maximum 93 character support ...'))
        return
    elif (log_size == 3) and (len(log_text) > 131):
        print(err_temp_func(python_file_name, line_python_file, '\'size = 3\' maximum 131 character support ...'))
        return
    elif (log_size == 4) and (len(log_text) > 199):
        print(err_temp_func(python_file_name, line_python_file, '\'size = 4\' maximum 199 character support ...'))
        return
    elif (log_size == 5) and (len(log_text) > 397):
        print(err_temp_func(python_file_name, line_python_file, '\'size = 5\' maximum 397 character support ...'))
        return

    # set value for write python file name in log file ...

    spaces = (18 - len(python_file))
    log_file_python_file_name = int(spaces / 2) * ' ' + str(python_file) + int((spaces + 1) / 2) * ' '

    # set value for write line of python file in log file ...

    if len(line_python_file) <= 6:
        spaces = (6 - len(line_python_file))
        log_file_python_file_line = int((spaces + 1) / 2) * ' ' + str(line_python_file) + int(spaces / 2) * ' '
    else:
        print(err_temp_func(python_file_name, line_python_file, 'maximum python line number support is 999999 ...'))
        return

    # set value for write log text in log file ...

    log_file_text = log_text

    # set value for log file name ...

    log_file_name = log_file

    # set value for log file size ...

    log_file_size = round(((6 - 0.3) / 100) * ((5 - [0.1, 2.9, 3.9, 4.4, 4.7][log_size - 1]) * 20), 1)
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # get continent ...

    continent = str(get_localzone()).lower().split('/')[0]

    # get city ...

    city = str(get_localzone()).lower().split('/')[1]

    # get country ...

    def get_country(_city):
        data = load(open('negar/countriesWithTheirCapital.json', 'r'))
        if _city in data:
            return data[_city]
        else:
            return 'unknown'

    country = str(get_country(city))

    # get username ...

    username = str(getuser())

    # get os ...

    os = str(system().lower())

    # get version ...

    version = str(release().lower())

    # get architecture

    architecture = str(machine().lower())

    # get date ...

    date = str(datetime.now()).split(' ')[0]

    # get time ...

    time = str(datetime.now()).split(' ')[1].split('.')[0]

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # show city , country , continent , username , os , version , architecture in log file ...

    specifications_center = '%s < %s < %s | %s | %s > %s > %s' % (
        city, country, continent, username, os, version, architecture)
    specifications = ' |  num  |    date    |   time   |' + ' ' * int(
        len(specifications_center) / log_file_size) + specifications_center + ' ' * int(
        len(specifications_center) / log_file_size) + '|       file       | line | '

    # if is not log file ...

    if not isfile(log_file_name):

        # create log file ...

        log_file = open(log_file_name, 'w')

        # write ' ___ ' to log file ...

        log_file.write('\n' + '  .' + '_' * (len(specifications) - 4) + '.' + '\n')

        # write 'specifications' to log file ...

        log_file.write(' ' + specifications + '\n')

        # write ' ___ ' to log file ...

        log_file.write('  .' + '_' * (len(specifications) - 4) + '.' + '\n')

        # write 'log' to log file ...

        log_file.write('  |   ' + str(1) + '   | ' + date + ' | ' + time + ' | ' + str(text) + ' ' * (
                len(specifications) - (len(log_file_text) + len(
            log_file_python_file_name) + 45)) + '|' + log_file_python_file_name + '|' + log_file_python_file_line + '|' + '\n')

        # write ' ___ ' to log file ...

        log_file.write('  .' + '_' * (len(specifications) - 4) + '.' + '\n')

        # save and close log file ..

        log_file.close()

    # if is log file ...

    elif isfile(log_file_name):

        with open(log_file_name, 'r') as f:
            if f.read().splitlines()[-1] != '  .' + '_' * (len(specifications) - 4) + '.':
                print(err_temp_func(python_file_name, line_python_file,
                                    'previously defined log file size , can\'not be resized ...'))
                return

        # find line number ...

        with open(log_file_name, 'r') as f:
            number_line = f.read().splitlines()[-2].split('| ' + str(datetime.now().year) + '-', 1)[0]
            number_line = number_line.replace('|', '')
            number_line = number_line.replace(' ', '')
            number_line = int(number_line) + 1

        # ckeck log file line number ...

        if len(str(number_line)) > 7:
            print(err_temp_func(python_file_name, line_python_file,
                                '\'size = 5\' maximum line number support is 9999999 ...'))
            return

        # set value for log file line number ...
        if len(str(number_line)) <= 7:
            spaces = (7 - len(str(number_line)))
            log_file_number = int(spaces / 2) * ' ' + str(number_line) + int((spaces + 1) / 2) * ' '
        else:
            print(err_temp_func(python_file_name, line_python_file,
                                'maximum number to numbering lines support is 9999999 ...'))
            return

        # open log file ...

        log_file = open(log_file_name, 'a')

        # add new 'log' to log file ...

        log_file.write('  |' + log_file_number + '| ' + date + ' | ' + time + ' | ' + str(text) + ' ' * (
                len(specifications) - (len(log_file_text) +
                                       len(
                                           log_file_python_file_name) + 45)) + '|' + log_file_python_file_name + '|' + log_file_python_file_line + '|' + '\n')

        # write ' ___ ' to log file ...

        log_file.write('  .' + '_' * (len(specifications) - 4) + '.' + '\n')

        # save and close log file ..

        log_file.close()
