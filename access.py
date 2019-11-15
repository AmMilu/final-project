#this file is used to access Github API


#this is just an example about how to get data from JSON
#some JSON:
#x = '{"name":"John"."age":30,"city":"New York"}'
#parse x:
#y = json.loads(x)
#the result is a python dictionary
#print(y["age"])

from github import Github
import urllib
import json

ACCESS_TOKEN = '43fa63c2ef98b7dd8e0c76ee4560aee7686960f'
g = Github(ACCESS_TOKEN+'6')

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

if __name__ == '__main__':
    search_commit()