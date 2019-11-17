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
        fieldnames = ['username', 'merged_pull_request']
        writer = csv.DictWriter(myfile, fieldnames=fieldnames)
        writer.writeheader()
        for piece in contributor_list:
            if(piece["merged_pull_request"]!=0):
                writer.writerow({'username': piece["login"], 'merged_pull_request': piece["merged_pull_request"]})

def convert_create_issue_to_csv():
    with open("display/create_issue.csv",'w', newline='') as myfile:
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
    with open("display/closed_issue.csv",'w', newline='') as myfile:
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


def convert_impact_to_csv():
    with open("display/impact.csv", 'w', newline='') as myfile:
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

if __name__ == "__main__":
    make_list()
    #convert_create_issue_to_csv()
    #convert_close_issue_to_csv()
    #convert_impact_to_csv()
    convert_pull_request_to_csv()