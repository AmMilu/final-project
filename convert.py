from access import *
import csv

total_pr = 0
total_issue = 0

def make_list():
    keyword = input('Enter keyword(s) of the repo you want to analysis [format: username/repo]\n(e.g. jquery/jquery or PyGithub/PyGithub):\n')    
    get_contributor(keyword)
    contributor_pr(keyword)
    contributor_issue(keyword)
    contributor_commit(keyword)
    total_pr = pr_total(keyword)
    total_issue = issue_total(keyword) - total_pr
    commit = commit_total(keyword)
    for piece in contributor_list: #the issue result contains pull request numbers, this is used to print out the list and pure the issue data
        piece["assigned_issue"] = piece["assigned_issue"] - piece["assigned_pull_request"]
        piece["closed_issue"] = piece["closed_issue"] - piece["assigned_pull_request"]
        piece["create_issue"] = piece["create_issue"] - piece["total_pull_request"]
        impact_calculate(piece, total_pr, total_issue, commit)

def convert_pull_request_to_csv():
    with open("display/pull_request.csv",'w', newline='') as myfile:
        fieldnames = ['merged_pull_request']
        writer = csv.DictWriter(myfile, fieldnames=fieldnames)
        writer.writeheader()
        for piece in contributor_list:
            writer.writerow({'merged_pull_request': piece["closed_pull_request"]})

def convert_issue_to_csv():
    with open("display/issue.csv",'w', newline='') as myfile:
        fieldnames = ['username','issue_score']
        writer = csv.DictWriter(myfile, fieldnames=fieldnames)
        writer.writeheader()
        for piece in contributor_list:
            score = 0
            if(piece["assigned_issue"] != 0):
                score = 30 * piece["closed_issue"] / piece["assigned_issue"]
            if(total_issue != 0):
                score = score +30 * piece["create_issue"] / total_issue + \
                               30 * piece["assigned_issue"] / total_issue
            score = score / 100
            writer.writerow({'username': piece["login"], 'issue_score': score})

def convert_impact_to_csv():
    with open("display/impact.csv", 'w', newline='') as myfile:
        fieldnames = ['username','issue_level','issue','impact','pull_request', 'commit']
        writer = csv.DictWriter(myfile, fieldnames=fieldnames)
        writer.writeheader()
        for piece in contributor_list:
            if(piece["closed_issue"] + piece["create_issue"]<=10):
                writer.writerow({'username': piece["login"], 'issue_level': "< 10", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            elif(piece["closed_issue"] + piece["create_issue"]<=100):
                writer.writerow({'username': piece["login"], 'issue_level': "11 - 100", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            elif(piece["closed_issue"] + piece["create_issue"]<=200):
                writer.writerow({'username': piece["login"], 'issue_level': "101 - 200", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            elif(piece["closed_issue"] + piece["create_issue"]<=500):
                writer.writerow({'username': piece["login"], 'issue_level': "201 - 500", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit': piece["commit"]})
            else:
                writer.writerow({'username': piece["login"], 'issue_level': "> 500", 
                            'issue': piece["closed_issue"] + piece["create_issue"],'impact': round(piece["impact"]),
                            'pull_request': piece["merged_pull_request"], 'commit_count': piece["commit"]})

if __name__ == "__main__":
    make_list()
    convert_impact_to_csv()
    #convert_pull_request_to_csv()
    #convert_issue_to_csv()