from flask import Flask, render_template, request
from convert import *
from access import *

app = Flask(__name__)

exist = True

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/", methods=['POST'])
def my_form_post():
    text=request.form['username']+'/'+request.form['reponame']
    try:
        make_list(text)
        convert_create_issue_to_csv()
        convert_close_issue_to_csv()
        convert_impact_to_csv(most[0])
        convert_pull_request_to_csv(most[1])
        return render_template('main.html')
    except:
        return render_template('not_found.html', user=request.form['username'], repo=request.form['reponame'])

@app.route("/impact")
def impact():
    return render_template('impact.html', impact = most[0], commit = most[2], pull_request = most[1])

@app.route("/closed_issue")
def closed():
    return render_template('closed_issue.html')

@app.route("/create_issue")
def create():
    return render_template('create_issue.html')

@app.route("/pull_request")
def pull():
    return render_template('pull_request.html', pull_request = most[1])

if __name__ == '__main__':
    app.run(debug=True) 