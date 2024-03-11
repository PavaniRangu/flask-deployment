from flask import Flask, render_template, request, jsonify
import re
import streamlit as st

app = Flask(_name_)

def match_pattern(input_string, pattern):
    matches = re.findall(pattern, input_string)
    return matches

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regex_results', methods=['POST'])
def regex_results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    regex_matches = match_pattern(test_string, regex_pattern)
    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern,
                           regex_matches=regex_matches)

@app.route('/email_results', methods=['POST'])
def email_results():
    email = request.form['email']
    email_validity = is_valid_email(email)
    return render_template('results.html', email=email, email_validity=email_validity)

if _name_ == '_main_':
    app.run(debug=True ,host='0.0.0.0', port=8501)