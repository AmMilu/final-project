#this file is used to access Github API
from github import Github

ACCESS_TOKEN = '43fa63c2ef98b7dd8e0c76ee4560aee7686960f'
g = Github(ACCESS_TOKEN+'6')

contributor_list = []

#this function is to get all the contributors login and save in the contributor_list
def get_contributor(keyword):
    contributor_count = 0
    for c in g.get_repo(keyword).get_contributors():
        contributor_dictionary = {'login': 'null', 'merged_pull_request': 0, 'total_pull_request': 0, 'assigned_pull_request': 0,
                                    'closed_issue': 0, 'assigned_issue': 0, 'create_issue': 0, 'commit': 0, 'impact': 0}
        contributor_dictionary["login"] = c.login
        contributor_list.append(contributor_dictionary)
        contributor_count = contributor_count + 1

#this function returns the total number of pull requests in a repo
def pr_total(keyword):
    return g.get_repo(keyword).get_pulls(state='all').totalCount
    
#this function takes a contributor's name as a parameter and returns a dict type
#with this contributor's pull request total number, closed pull request number 
#and open pull request number
def contributor_pr(keyword):
    for cpr in g.get_repo(keyword).get_pulls(state='all'):
        for piece in contributor_list:
            name = piece["login"]
            if(cpr.user.login == name):
                piece["total_pull_request"] = piece["total_pull_request"] + 1
                if(cpr.state == 'closed' and cpr.merged_at is not None):                #if a pull request is not merge, then it doesn't count in the compact
                    piece["merged_pull_request"] = piece["merged_pull_request"] + 1
            if(cpr.assignee is not None and cpr.assignee.login == name):
                piece["assigned_pull_request"] = piece["assigned_pull_request"] + 1

#this function returns the total number of issues in a repo
def issue_total(keyword):
    return g.get_repo(keyword).get_issues(state='all').totalCount

#this function takes a contributor's name as a parameter and returns a dict type value with the
#total number of the issues assigned to him and the numbers of his closed and open issues
def contributor_issue(keyword):
    for issue in g.get_repo(keyword).get_issues(state='all'):
        for piece in contributor_list:
            name = piece["login"]
            if(issue.user.login == name):
                piece["create_issue"] = piece["create_issue"] + 1
            if(issue.assignee is not None and issue.assignee.login == name):
                piece["assigned_issue"] = piece["assigned_issue"] + 1
                if(issue.state == 'closed'):
                    piece["closed_issue"] = piece["closed_issue"] + 1

#this function returns the total commit number of the repo
def commit_total(keyword):
    return g.get_repo(keyword).get_commits().totalCount

#this function get the commit numbers of each contributor and save the result in the list
def contributor_commit(keyword):
    for piece in contributor_list:
        name = piece["login"]
        piece["commit"] = g.get_repo(keyword).get_commits(author=name).totalCount

def impact_calculate(info, total_pr, total_issue, commit):
    if(total_pr != 0):
        info["impact"] = 25 * info["merged_pull_request"] / total_pr + 15 * info["assigned_pull_request"] / total_pr
    if(info["assigned_issue"] != 0):
        info["impact"] = info["impact"] + 20 * info["closed_issue"] / info["assigned_issue"]
    if(total_issue != 0):
        info["impact"] = info["impact"] + 15 * info["assigned_issue"] / total_issue + 15 * info["create_issue"] / total_issue
    if(commit != 0):
        info["impact"] = info["impact"] + 10 * info["commit"] / commit
    info["impact"] = 100 * info["impact"]

#if __name__ == "__main__":
#    keyword = input('Enter keyword(s) of the repo you want to analysis [format: username/repo]\n(e.g. jquery/jquery or PyGithub/PyGithub):\n')    
#    get_contributor(keyword)
#    contributor_pr(keyword)
#    contributor_issue(keyword)
#    contributor_commit(keyword)
#    total_pr = pr_total(keyword)
#    total_issue = issue_total(keyword) - total_pr
#    commit = commit_total(keyword)
#    for piece in contributor_list: #the issue result contains pull request numbers, this is used to print out the list and pure the issue data
#        piece["assigned_issue"] = piece["assigned_issue"] - piece["assigned_pull_request"]
#        piece["closed_issue"] = piece["closed_issue"] - piece["assigned_pull_request"]
#        piece["create_issue"] = piece["create_issue"] - piece["total_pull_request"]
#        impact_calculate(piece, total_pr, total_issue, commit)
#        print(piece)
#    print('pr_total: ' + str(total_pr) + ' issue_total: ' + str(total_issue) + ' commit_total: ' + str(commit))