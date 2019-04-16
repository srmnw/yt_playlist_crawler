import json
from subprocess import PIPE, Popen

def get_api_key():
    p = Popen(['./key_ini'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output.decode('utf-8')


def get_api_file():
    p = Popen(['./keyfile_ini'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output.decode('utf-8')
