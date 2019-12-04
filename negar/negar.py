# Copyright SYS113 2019. MIT license , see README.md file.

# import libraries ...

from tzlocal import get_localzone
from datetime import datetime
from platform import system, release, machine
from getpass import getuser
from os.path import isfile
from inspect import getframeinfo, stack


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

    # get country ...

    def get_country():
        data = {'kabul': 'afghanistan', 'tirana': 'albania', 'alger': 'algeria', 'fagatogo': 'american samoa', 'andorra la vella': 'andorra', 'luanda': 'angola', 'the valley': 'anguilla', 'null': 'united states minor outlying islands', "saint john's": 'antigua and barbuda', 'buenos aires': 'argentina', 'yerevan': 'armenia', 'oranjestad': 'aruba', 'canberra': 'australia', 'wien': 'austria', 'baku': 'azerbaijan', 'nassau': 'bahamas', 'al-manama': 'bahrain', 'dhaka': 'bangladesh', 'bridgetown': 'barbados', 'minsk': 'belarus', 'bruxelles [brussel]': 'belgium', 'belmopan': 'belize', 'porto-novo': 'benin', 'hamilton': 'bermuda', 'thimphu': 'bhutan', 'la paz': 'bolivia', 'sarajevo': 'bosnia and herzegovina', 'gaborone': 'botswana', 'brasília': 'brazil', 'bandar seri begawan': 'brunei', 'sofia': 'bulgaria', 'ouagadougou': 'burkina faso', 'bujumbura': 'burundi', 'phnom penh': 'cambodia', 'yaound': 'cameroon', 'ottawa': 'canada', 'praia': 'cape verde', 'george town': 'cayman islands', 'bangui': 'central african republic', "n'djam": 'chad', 'santiago de chile': 'chile', 'peking': 'china', 'flying fish cove': 'christmas island', 'west island': 'cocos (keeling) islands', 'santaf': 'colombia', 'moroni': 'comoros', 'brazzaville': 'congo', 'avarua': 'cook islands', 'san jos': 'costa rica', 'zagreb': 'croatia', 'la habana': 'cuba', 'nicosia': 'cyprus', 'praha': 'czech republic', 'copenhagen': 'denmark', 'djibouti': 'djibouti', 'roseau': 'dominica', 'santo domingo de guzm': 'dominican republic', 'dili': 'east timor', 'quito': 'ecuador', 'cairo': 'egypt', 'san salvador': 'el salvador', 'london': 'united kingdom', 'malabo': 'equatorial guinea', 'asmara': 'eritrea', 'tallinn': 'estonia', 'addis abeba': 'ethiopia', 'stanley': 'falkland islands', 'tórshavn': 'faroe islands', 'suva': 'fiji islands', 'helsinki [helsingfors]': 'finland', 'paris': 'france', 'cayenne': 'french guiana', 'papeete': 'french polynesia', 'libreville': 'gabon', 'banjul': 'gambia', 'tbilisi': 'georgia', 'berlin': 'germany', 'accra': 'ghana', 'gibraltar': 'gibraltar', 'athenai': 'greece', 'nuuk': 'greenland', "saint george's": 'grenada', 'basse-terre': 'guadeloupe', 'aga': 'guam', 'ciudad de guatemala': 'guatemala', 'conakry': 'guinea', 'bissau': 'guinea-bissau', 'georgetown': 'guyana', 'port-au-prince': 'haiti', 'citt': 'holy see (vatican capital state)', 'tegucigalpa': 'honduras', 'victoria': 'seychelles', 'budapest': 'hungary', 'reykjav': 'iceland', 'new delhi': 'india', 'jakarta': 'indonesia', 'tehran': 'iran', 'baghdad': 'iraq', 'dublin': 'ireland', 'jerusalem': 'israel', 'roma': 'italy', 'yamoussoukro': 'ivory coast', 'kingston': 'norfolk island', 'tokyo': 'japan', 'amman': 'jordan', 'astana': 'kazakhstan', 'nairobi': 'kenya', 'bairiki': 'kiribati', 'kuwait': 'kuwait', 'bishkek': 'kyrgyzstan', 'vientiane': 'laos', 'riga': 'latvia', 'beirut': 'lebanon', 'maseru': 'lesotho', 'monrovia': 'liberia', 'tripoli': 'libyan arab jamahiriya', 'vaduz': 'liechtenstein', 'vilnius': 'lithuania',
                'luxembourg [luxemburg/l': 'luxembourg', 'macao': 'macao', 'skopje': 'north macedonia', 'antananarivo': 'madagascar', 'lilongwe': 'malawi', 'kuala lumpur': 'malaysia', 'male': 'maldives', 'bamako': 'mali', 'valletta': 'malta', 'dalap-uliga-darrit': 'marshall islands', 'fort-de-france': 'martinique', 'nouakchott': 'mauritania', 'port-louis': 'mauritius', 'mamoutzou': 'mayotte', 'ciudad de m': 'mexico', 'palikir': 'micronesia, federated states of', 'chisinau': 'moldova', 'monaco-ville': 'monaco', 'ulan bator': 'mongolia', 'plymouth': 'montserrat', 'rabat': 'morocco', 'maputo': 'mozambique', 'rangoon (yangon)': 'myanmar', 'windhoek': 'namibia', 'yaren': 'nauru', 'kathmandu': 'nepal', 'amsterdam': 'netherlands', 'willemstad': 'netherlands antilles', 'noum': 'new caledonia', 'wellington': 'new zealand', 'managua': 'nicaragua', 'niamey': 'niger', 'abuja': 'nigeria', 'alofi': 'niue', 'pyongyang': 'north korea', 'belfast': 'northern ireland', 'garapan': 'northern mariana islands', 'oslo': 'norway', 'masqat': 'oman', 'islamabad': 'pakistan', 'koror': 'palau', 'gaza': 'palestine', 'ciudad de panam': 'panama', 'port moresby': 'papua new guinea', 'asunci': 'paraguay', 'lima': 'peru', 'manila': 'philippines', 'adamstown': 'pitcairn', 'warszawa': 'poland', 'lisboa': 'portugal', 'san juan': 'puerto rico', 'doha': 'qatar', 'saint-denis': 'reunion', 'bucuresti': 'romania', 'moscow': 'russian federation', 'kigali': 'rwanda', 'jamestown': 'saint helena', 'basseterre': 'saint kitts and nevis', 'castries': 'saint lucia', 'saint-pierre': 'saint pierre and miquelon', 'kingstown': 'saint vincent and the grenadines', 'apia': 'samoa', 'san marino': 'san marino', 's': 'sao tome and principe', 'riyadh': 'saudi arabia', 'edinburgh': 'scotland', 'dakar': 'senegal', 'freetown': 'sierra leone', 'singapore': 'singapore', 'bratislava': 'slovakia', 'ljubljana': 'slovenia', 'honiara': 'solomon islands', 'mogadishu': 'somalia', 'pretoria': 'south africa', 'seoul': 'south korea', 'juba': 'south sudan', 'madrid': 'spain', 'khartum': 'sudan', 'paramaribo': 'suriname', 'longyearbyen': 'svalbard and jan mayen', 'mbabane': 'swaziland', 'stockholm': 'sweden', 'bern': 'switzerland', 'damascus': 'syria', 'dushanbe': 'tajikistan', 'dodoma': 'tanzania', 'bangkok': 'thailand', 'lom': 'togo', 'fakaofo': 'tokelau', "nuku'alofa": 'tonga', 'port-of-spain': 'trinidad and tobago', 'tunis': 'tunisia', 'ankara': 'turkey', 'ashgabat': 'turkmenistan', 'cockburn town': 'turks and caicos islands', 'funafuti': 'tuvalu', 'kampala': 'uganda', 'kyiv': 'ukraine', 'abu dhabi': 'united arab emirates', 'washington': 'united states', 'montevideo': 'uruguay', 'toskent': 'uzbekistan', 'port-vila': 'vanuatu', 'caracas': 'venezuela', 'hanoi': 'vietnam', 'road town': 'virgin islands, british', 'charlotte amalie': 'virgin islands, u.s.', 'cardiff': 'wales', 'mata-utu': 'wallis and futuna', 'el-aai': 'western sahara', 'sanaa': 'yemen', 'beograd': 'yugoslavia', 'lusaka': 'zambia', 'harare': 'zimbabwe'}
        if city in data:
            return data[city]
        else:
            return 'unknown'

    country = str(get_country())

    # get city ...

    city = str(get_localzone()).lower().split('/')[1]

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
