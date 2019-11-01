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
    elif (path_info == '/persons/*'):
        path_info_user = ''
        if (path_info == '/persons' or path_info == '/persons/'):
            path_info_user = 'all'
        else:
            path_info_user = path_info[8:].strip('/')
        list_places(path_info_user)
    elif (path_info == '/newperson' or path_info == '/newperson/'):
        new_person()
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

def json_page():
    print('Content-Type: application/json')
    print('Status: 200 OK')
    print()

    x = [1, 2, 30, 20, {'foo':'bar'}]
    x_json = json.dumps(x, indent=2)
    print(x_json)

def get_entries(conn):
    # Helper function for list_places()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM {};'.format(passwords.SQL_DB))
    results = cursor.fetchall()
    cursor.close()
    return results

def list_persons(users):
    apache_ok()
    conn = MYSQLdb.connect(host = passwords.SQL_HOST,
                           user = passwords.SQL_USER,
                           passwd = passwords.SQL_PASSWD,
                           db = passwords.SQL_DB)

    results = get_entries(conn)
    if (users == 'all'):
        results_json = json.dumps(results, indent=2)
    else:
        for row in results:
            if (str(row[0]) == users):
                results_json = json.dumps(row, indent=2)
    print(results_json)

def new_person():
    apache_ok()
    print('''
    <p>Insert a new person!</p>
    <form method='POST' action='/display_new'>
        State of origin:
        <input type='text' name='currstate'><br>
        School state:
        <input type='text' name='unistate'><br>
        Future state:
        <input type='text' name='futurestate'><br>
        Graduation year:
        <input type='text' name='gradyear'><br>
        <input type='submit' value='Submit'>
    </form>''')

def display_new():
    conn = MYSQLdb.connect(host = passwords.SQL_HOST,
                           user = passwords.SQL_USER,
                           passwd = passwords.SQL_PASSWD,
                           db = passwords.SQL_DB)

    cursor = conn.cursor()
    cursor.execute('INSERT INTO {} 
    (current_state, uni_state, future_state, grad_year) 
    VALUES ({} {} {} {});')

def google_redirect():
    print('Status: 302 Redirect')
    print('Location: https://www.google.com')
    print()

    
main()