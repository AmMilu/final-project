from flask import Flask, render_template, request
from convert import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/", methods=['POST'])
def my_form_post():
    text=request.form['username']+'/'+request.form['reponame']
    make_list(text)
    convert_create_issue_to_csv()
    convert_close_issue_to_csv()
    convert_impact_to_csv()
    convert_pull_request_to_csv()
    return render_template('main.html')

@app.route("/impact")
def impact():
    return render_template('impact.html')

@app.route("/closed_issue")
def closed():
    return render_template('closed_issue.html')

@app.route("/create_issue")
def create():
    return render_template('create_issue.html')

@app.route("/pull_request")
def pull():
    return render_template('pull_request.html')

if __name__ == '__main__':
    app.run(debug=True) 