import os
from subprocess import PIPE, Popen

def get_api_key():
    dir_content = os.listdir('credentials')
    '''FIX ensure correct credential'''
    for content in dir_content:
        if 'api_key' in content:
            with open('credentials/' + content, 'r') as file:
                key = file.read()
                return key


def get_api_file():
    dir_content = os.listdir('credentials')
    '''FIX ensure correct credential'''
    for content in dir_content:
        if 'client_secret' in content:
            return 'credentials/' + content
