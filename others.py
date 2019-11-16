import json
import urllib

def search_commit():
    commit = g.get_repo('jquery/jquery').get_commits()
    commit_information = vars(commit)
    #print('\n'.join("%s: %s" % item for item in commit_information.items()))
    commit_url = commit_information["_PaginatedList__firstUrl"]
    commit_content = urllib.request.urlopen(commit_url)
    commit_test = commit_content.read().decode('utf-8')
    commit_test = commit_test[1:len(commit_test)-2]
    commit_part = commit_test.split(',{"sha":')
    #print (commit_part[0])
    #test = json.loads(commit_part[0])
    #print('\n'.join("%s: %s" % item for item in test.items()))
    convert_to_dict(commit_part[0])
    print('\n')
    print(len(commit_part))

def convert_to_dict(string):
    result = json.loads(string)
    print('\n'.join("%s: %s" % item for item in result.items()))

def search_user():
    user = g.get_user(login='jquery')
    user_information = vars(user)
    user_rawData = user_information["_rawData"]
    print('\n'.join("%s: %s" % item for item in user_rawData.items()))

def search_repo():
    repo = g.get_user(login='jquery').get_repos()
    repo_information = vars(repo)
    print('\n'.join("%s: %s" % item for item in repo_information.items()))

def search_sepcific_repo():
    repo = g.get_user(login='jquery').get_repo('jquery')
    repo_information = vars(repo)
    repo_rawData = repo_information["_rawData"]
    print('\n'.join("%s: %s" % item for item in repo_rawData.items()))

def get_contributor():
    for c in g.get_repo('jquery/jqueyr').get_contributors():
        print(c.login)
    
    contributor_url = g.get_repo('jquery/jquery').contributors_url
    finish = False
    index=1
    while finish==False:
        url_index = str(index)
        with urllib.request.urlopen(contributor_url+'?page='+url_index+'&per_page=100') as response:
            html = response.read()
        contributor_json = html.decode('utf8')
        contributor_data = json.loads(contributor_json)
        contributor_output = json.dumps(contributor_data, indent=2)
        contributor_separate = contributor_output[1:len(contributor_output)-2].split("},")
        if(len(contributor_separate)<100):
            finish = True
        for i in contributor_separate:
            contributor_info_list.append(i)
        index = index + 1
    
    for info in contributor_info_list:
        login = info.find("login")
        idd = info.find("id")
        contributor_list.append(info[login+9:idd-8])
    print(contributor_list)

#this function returns the total number of pull request in the specific repo
def pull_request_total():
    pr = g.get_repo('jquery/jquery').get_pulls(state='all').totalCount
    return pr

def contributor_pr(name):
    open_count = 0
    closed_count = 0
    for cpr in g.get_repo('jquery/jquery').get_pulls(state='all'):
        if(cpr.user.login == name):
            if(cpr.state == 'open'):
                open_count = open_count + 1
            else:
                closed_count = closed_count + 1
    pr_dict = {'login': name, 'open_pr': open_count, 'closed_pr': closed_count, 'total_pr': open_count+closed_count}
    return pr_dict

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
