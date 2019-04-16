from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

import time


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def answer_all():
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select toppings',
            'name': 'toppings',
            'choices': [
                Separator('Do you want to download all playlists or just some specific?'),
                {
                    'name': 'fetch all playlists'
                },
                {
                    'name': 'fetch specific playlist'
                }
            ]
        }
    ]
    answer = prompt(questions, style=style)
    if len(answer['toppings']) == 0:
        print('\x1b[6;30;42m' + 'You have to choose ONE option!' + '\x1b[0m')
        time.sleep(2)
        answer_all()
    if len(answer['toppings']) == 2:
        print('\x1b[6;30;42m' + 'Both options are forbidden. You have to choose ONE option!' + '\x1b[0m')
        time.sleep(2)
        answer_all()
    return answer['toppings']


def answer_choose_playlist(response):
    choices = list()
    choices.append(Separator('Select your playlists pls'))
    for item in response:
        choices.append(item)
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select your playlists you want to fetch for',
            'name': 'toppings',
            'choices': choices
        }
    ]
    answer = prompt(questions, style=style)
    if len(answer['toppings']) == 0:
        print('\x1b[6;30;42m' + 'You have to choose at least one option!' + '\x1b[0m')
        time.sleep(2)
        answer_choose_playlist(response)
    return answer['toppings']

def answer_private_public():
    questions = [
        {
            'type': 'checkbox',
            'message': 'Are your playlists public or private?',
            'name': 'toppings',
            'choices': [
                Separator('Are your playlists public or private?'),
                {
                    'name': 'public'
                },
                {
                    'name': 'private'
                }
            ]
        }
    ]
    answer = prompt(questions, style=style)
    if len(answer['toppings']) == 0:
        print('\x1b[6;30;42m' + 'You have to choose ONE option!' + '\x1b[0m')
        time.sleep(2)
        answer_private_public()
    if len(answer['toppings']) == 2:
        print('\x1b[6;30;42m' + 'Both options are forbidden. You have to choose ONE option!' + '\x1b[0m')
        time.sleep(2)
        answer_private_public()
    return answer['toppings']

