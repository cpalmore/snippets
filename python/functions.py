from typing import Union

def get_credentials(env_var:str=None, domain:str=None) -> tuple:
    '''
    Get user credentials via the following methods:

    ENVIRONMENT VARIABLE (RECOMMENDED)
        get_credentials(env_var='VARIABLE') reads an environment variable.
        The variable must be formatted as a Python dictionary:
            "{'username':'YOUR_USERNAME', 'password':'YOUR_PASSWORD'}"

    DOMAIN AUTHENTICATION
        get_credentials(domain='DOMAIN') to get username from system.
        User will be prompted for password.

    MANUAL AUTHENTICATION
        If authentication method not specified or fails user
        will be prompted to manually input credentials.
    '''

    from ast import literal_eval
    from getpass import getpass,getuser
    from os import getenv

    # try, except guarantees manual input if other methods fail
    try:

        if env_var:
            # ENVIRONMENT VARIABLE AUTHENTICATION
            credentials = literal_eval(getenv(env_var))
            uid = credentials['username']
            key = credentials['password']

        elif domain:
            # DOMAIN AUTHENTICATION
            uid = domain + getuser()
            key = getpass('Password for current user: ')

        else: raise Exception('Defaulting to manual authentication.')

    except:
        # MANUAL AUTHENTICATION
        uid = input('Username: ')
        key = getpass('Password: ')

    return (uid, key)

def prompt_choice(options:Union[dict, list, set, tuple]) -> tuple:
    '''
    Presents multiple choice prompt to user.
    '''

    # convert options to dictionary type
    if   type(options) in ['dict']: pass
    elif type(options) in ['list', 'set', 'tuple']:
        options = {i+1:item for i,item in enumerate(options)}
    else:
        raise Exception('Options type must be of: dict, list, set, tuple.')

    # convert all keys,values to strings
    options = {str(key):str(value) for key,value in options.items()}

    # prompt user
    while True:
        print('Select one: ')
        for key,value in options.items():
            print(key + '. ' + value)
        
        print('----------------')
        
        # input() waits until user presses 'enter'
        choice = str(input())
        
        if choice in options.keys(): break
        if choice == 'exit': return 'exit'
        else: print('\nInvalid. Retry or input "exit" to exit.')

    return (choice, options[choice])

def indicate_progress(i:int, total:int) -> None:
    '''Put this inside of an iterator.'''
    print(f'{100*i//total}%', end='\r')

class color:
    '''
    Print colored text.

    Examples
    --------
    - colors.[fore/back]ground.colorname
    - color.bg.black
    '''

    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'

    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

