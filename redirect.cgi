#! /usr/bin/python3

import os
import cgi
import cgitb

cgitb.enable()

import json

def main():
    path_info = check_path()
    if (path_info == '' or path_info == '/'):
        apache_ok()
        html_section()
    elif (path_info == '/json_page'):
        json_page()
    else:
        google_redirect()

def check_path():
    if ('PATH_INFO' in os.environ):
        path_info = os.environ['PATH_INFO']
    else:
        path_info = ''
    
    return path_info

def apache_ok():
    print('Content-Type: text/html')
    print('Status: 200 OK')

def html_section():
    print('''
    <!DOCTYPE html>
    <html><head>
    <title>Redirecting or not</title>
    </head>
    <body>
    <p>Hello world</p>
    </body></html>
    ''')

main()