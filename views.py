from flask import render_template, url_for, request


def start():
    return render_template('index.html')


def login():
    if request.method == 'POST':
        return 'Submitted'
    else:
        return render_template('index.html')
