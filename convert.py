from access import *
import csv

total_pr = 0
total_issue = 0
most = []  #index = 0 impact index = 1 pull request  index = 2 commit


def make_list(keyword):
    #keyword = input('Enter keyword(s) of the repo you want to analysis [format: username/repo]\n(e.g. jquery/jquery or PyGithub/PyGithub):\n')    
    get_contributor(keyword)
    contributor_pr(keyword)
    contributor_issue(keyword)
    contributor_commit(keyword)
    total_pr = pr_total(keyword)
    total_issue = issue_total(keyword) - total_pr
    commit = commit_total(keyword)
    most.append(0)
    most.append(0)
    most.append(0)
    for piece in contributor_list: #the issue result contains pull request numbers, this is used to print out the list and pure the issue data
        #piece["assigned_issue"] = piece["assigned_issue"] - piece["assigned_pull_request"]
        #piece["closed_issue"] = piece["closed_issue"] - piece["assigned_pull_request"]
        #piece["create_issue"] = piece["create_issue"] - piece["total_pull_request"]
        if(piece["assigned_issue"] > piece["assigned_pull_request"]):
            piece["assigned_issue"] = piece["assigned_issue"] - piece["assigned_pull_request"]
        if(piece["closed_issue"] > piece["assigned_pull_request"]):
            piece["closed_issue"] = piece["closed_issue"] - piece["assigned_pull_request"]
        if(piece["create_issue"] > piece["total_pull_request"]):
            piece["create_issue"] = piece["create_issue"] - piece["total_pull_request"]
        impact_calculate(piece, total_pr, total_issue, commit)
        if(piece["merged_pull_request"] > most[1]):
            most[1] = piece["merged_pull_request"]
        if(round(piece["impact"]) > most[0]):
            most[0] = round(piece["impact"])
        if(piece["commit"] > most[2]):
            most[2] = piece["commit"]

def convert_pull_request_to_csv(pull_request):
    myfile = open("static/pull_request.csv",'w+', newline='')
    fieldnames = ['username', 'merged_pull_request']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)
    writer.writeheader()
    for piece in contributor_list:
        if(piece["merged_pull_request"]!=0):
            writer.writerow({'username': piece["login"], 'merged_pull_request': piece["merged_pull_request"]})

def convert_create_issue_to_csv():
    myfile = open("static/create_issue.csv",'w+', newline='')
    fieldnames = ['username', 'issue_level', 'create_issue']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)
    writer.writeheader()
    for piece in contributor_list:
        tmp=piece["create_issue"]
        if(tmp != 0):
            if(tmp < 10):
                writer.writerow({'username': piece["login"], 'issue_level': "<10", 'create_issue': piece["create_issue"]})
            elif(tmp < 50):
                writer.writerow({'username': piece["login"], 'issue_level': "10-50", 'create_issue': piece["create_issue"]})
            elif(tmp < 100):
                writer.writerow({'username': piece["login"], 'issue_level': "50-100", 'create_issue': piece["create_issue"]})
            elif(tmp < 150):
                writer.writerow({'username': piece["login"], 'issue_level': "100-150", 'create_issue': piece["create_issue"]})
            else:
                writer.writerow({'username': piece["login"], 'issue_level': "150-200", 'create_issue': piece["create_issue"]})

def convert_close_issue_to_csv():
    myfile = open("static/closed_issue.csv",'w+', newline='')
    fieldnames = ['username','issue_level', 'closed_issue']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)
    writer.writeheader()
    for piece in contributor_list:
        tmp=piece["closed_issue"]
        if(tmp != 0):
            if(tmp < 10):
                writer.writerow({'username': piece["login"], 'issue_level': "<10", 'closed_issue': tmp})
            elif(tmp < 50):
                writer.writerow({'username': piece["login"], 'issue_level': "10-50", 'closed_issue': tmp})
            elif(tmp < 100):
                writer.writerow({'username': piece["login"], 'issue_level': "50-100", 'closed_issue': tmp})
            elif(tmp < 150):
                writer.writerow({'username': piece["login"], 'issue_level': "100-150", 'closed_issue': tmp})
            else:
                writer.writerow({'username': piece["login"], 'issue_level': "150-200", 'closed_issue': tmp})


def convert_impact_to_csv(most_impact):
    myfile = open("static/impact.csv", 'w+', newline='')
    fieldnames = ['username','issue_level','issue','impact','pull_request', 'commit']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)
    writer.writeheader()
    for piece in contributor_list:
        if(piece["impact"] != 0):
            if(piece["closed_issue"] + piece["create_issue"]<10):
                writer.writerow({'username': piece["login"], 'issue_level': "< 10", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            elif(piece["closed_issue"] + piece["create_issue"]<100):
                writer.writerow({'username': piece["login"], 'issue_level': "10 - 100", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            elif(piece["closed_issue"] + piece["create_issue"]<200):
                writer.writerow({'username': piece["login"], 'issue_level': "100 - 200", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            elif(piece["closed_issue"] + piece["create_issue"]<500):
                writer.writerow({'username': piece["login"], 'issue_level': "200 - 500", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            else:
                writer.writerow({'username': piece["login"], 'issue_level': "> 500", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})