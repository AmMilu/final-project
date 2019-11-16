#this file is used to access Github API
from github import Github

ACCESS_TOKEN = '43fa63c2ef98b7dd8e0c76ee4560aee7686960f'
g = Github(ACCESS_TOKEN+'6')

contributor_list = []

#this function is to get all the contributors login and save in the contributor_list
def get_contributor():
    contributor_count = 0
    for c in g.get_repo('jquery/jquery').get_contributors():
        contributor_dictionary = {'login': 'null', 'closed_pull_request': 0, 'total_pull_request': 0, 'assigned_pull_request': 0,
                                    'closed_issue': 0, 'assigned_issue': 0, 'create_issue': 0, 'commit': 0}
        contributor_dictionary["login"] = c.login
        contributor_list.append(contributor_dictionary)
        contributor_count = contributor_count + 1

#this function returns the total number of pull requests in a repo
def pr_total():
    return g.get_repo('jquery/jquery').get_pulls(state='all').totalCount
    
#this function takes a contributor's name as a parameter and returns a dict type
#with this contributor's pull request total number, closed pull request number 
#and open pull request number
def contributor_pr():
    for cpr in g.get_repo('jquery/jquery').get_pulls(state='all'):
        for piece in contributor_list:
            name = piece["login"]
            if(cpr.user.login == name):
                piece["total_pull_request"] = piece["total_pull_request"] + 1
                if(cpr.state == 'closed' and cpr.merged_at is not None):
                    piece["closed_pull_request"] = piece["closed_pull_request"] + 1
            if(cpr.assignee is not None and cpr.assignee.login == name):
                piece["assigned_pull_request"] = piece["assigned_pull_request"] + 1
            piece["assigned_issue"] = piece["assigned_issue"] - piece["assigned_pull_request"]
            piece["closed_issue"] = piece["closed_issue"] - piece["assigned_pull_request"]

#this function returns the total number of issues in a repo
def issue_total():
    return g.get_repo('jquery/jquery').get_issues(state='all').totalCount

#this function takes a contributor's name as a parameter and returns a dict type value with the
#total number of the issues assigned to him and the numbers of his closed and open issues
def contributor_issue():
    for issue in g.get_repo('jquery/jquery').get_issues(state='all'):
        for piece in contributor_list:
            name = piece["login"]
            if(issue.user.login == name):
                piece["create_issue"] = piece["create_issue"] + 1
            if(issue.assignee is not None and issue.assignee.login == name):
                piece["assigned_issue"] = piece["assigned_issue"] + 1
                if(issue.state == 'closed'):
                    piece["closed_issue"] = piece["closed_issue"] + 1

#this function returns the total commit number of the repo
def commit_total():
    return g.get_repo('jquery/jquery').get_commits().totalCount

#this function get the commit numbers of each contributor and save the result in the list
def contributor_commit():
    for piece in contributor_list:
        name = piece["login"]
        piece["commit"] = g.get_repo('jquery/jquery').get_commits(author=name).totalCount

if __name__ == "__main__":
    get_contributor()
    contributor_pr()
    contributor_issue()
    contributor_commit()
    print(contributor_list)
    print()
    print('pr_total: ' + str(pr_total()) + ' issue_total: ' + str(issue_total()) + ' commit_total: ' + str(commit_total()))