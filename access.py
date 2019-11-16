#this file is used to access Github API
from github import Github
import json

ACCESS_TOKEN = '43fa63c2ef98b7dd8e0c76ee4560aee7686960f'
g = Github(ACCESS_TOKEN+'6')

contributor_list = []

#this function is to get all the contributors login and save in the contributor_list
def get_contributor():
    contributor_count = 0
    for c in g.get_repo('jquery/jquery').get_contributors():
        contributor_list.append(c)
        contributor_count = contributor_count + 1
    
#this function takes a contributor's name as a parameter and returns a dict type
#with this contributor's pull request total number, closed pull request number 
#and open pull request number
def contributor_pr(name):
    total_count = 0
    open_count = 0
    closed_count = 0
    for cpr in g.get_repo('jquery/jquery').get_pulls(state='all'):
        total_count = total_count + 1
        if(cpr.user.login == name):
            if(cpr.state == 'open'):
                open_count = open_count + 1
            else:
                closed_count = closed_count + 1
    pr_dict = {'login': name, 'open_pr': open_count, 'closed_count': closed_count, 'total_count': open_count+closed_count, 'total_pr': total_count}
    return pr_dict

#this function returns the total number of issues in a repo
def issues_total():
    return g.get_repo('jquery/jquery').get_issues(state='all').totalCount

#this function takes a contributor's name as a parameter and returns a dict type value with the
#total number of the issues assigned to him and the numbers of his closed and open issues
def contributor_issue(name):
    open_count = 0
    closed_count = 0
    for issue in g.get_repo('jquery/jquery').get_issues(state='all', assignee=name):
        if(issue.state == 'open'):
            open_count = open_count + 1
        if(issue.state == 'closed'):
            closed_count = closed_count + 1
    issue_dict = {'assignee': name, 'open_issue': open_count, 'closed_issue': closed_count, 'total_issue': open_count+closed_count}
    return issue_dict

#this function returns the total commit number of the repo
def commit_total():
    return g.get_repo('jquery/jquery').get_commits().totalCount

#this function takes a contributor's name as a parameter and returns his total commit amount in the repo
def contributor_commit(name):
    return g.get_repo('jquery/jquery').get_commits(author=name).totalCount
